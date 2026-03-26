# To run use: streamlit run app.py If not working then use: python -m streamlit run app.py

import streamlit as st
from dotenv import load_dotenv
import pdfplumber
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_core.messages import HumanMessage, AIMessage
from htmlTemplates import css, bot_template, user_template
import asyncio
import nest_asyncio
import os

nest_asyncio.apply()

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        try:
            with pdfplumber.open(pdf) as pdf_file:
                for page in pdf_file.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
        except Exception as e:
            st.warning(f"Could not read {pdf.name} with pdfplumber: {str(e)}. Trying fallback method...")
            try:
                from PyPDF2 import PdfReader
                pdf_reader = PdfReader(pdf)
                for page in pdf_reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
            except Exception as e:
                st.error(f"Failed to read {pdf.name}: {str(e)}")
                continue
    return text

def get_text_chunks(text):
    if not text or not text.strip():
        return []
    
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    if not text_chunks:
        raise ValueError("No text chunks to create vector store")
    
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", 
        temperature=0.3,
        convert_system_message_to_human=True
    )
    
    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True,
        output_key='answer'
    )
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        memory=memory,
        verbose=True,
        return_source_documents=True
    )
    return conversation_chain

def handle_userinput(user_question):
    if st.session_state.conversation is None:
        st.warning("⚠️ Please process your PDFs first before asking questions.")
        return
    
    if not user_question or not user_question.strip():
        st.warning("⚠️ Please enter a question.")
        return
    
    try:
        with st.spinner("🤔 Thinking..."):
            response = st.session_state.conversation.invoke({"question": user_question})
        
        # Store the question and answer in session state for display
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        st.session_state.messages.append({"role": "user", "content": user_question})
        st.session_state.messages.append({"role": "assistant", "content": response['answer']})
        
        # Display the conversation
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(user_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
            else:
                st.markdown(bot_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
                
    except Exception as e:
        st.error(f"❌ Error getting response: {str(e)}")
        st.info("💡 Tip: Make sure your PDFs are processed and contain readable text.")

def main():
    # Ensure event loop exists
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

    # Load environment variables
    load_dotenv()
    
    # Check for API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("""
        ❌ **Google API Key Not Found!**
        
        Please create a `.env` file in the same directory as `app.py` with:
