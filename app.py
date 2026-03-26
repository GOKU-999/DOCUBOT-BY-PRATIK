# To run use: streamlit run app.py If not working then use: python -m streamlit run app.py

import streamlit as st
from dotenv import load_dotenv
import pdfplumber
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
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
                    text += page.extract_text() or ""
        except Exception as e:
            st.warning(f"Could not read {pdf.name} with pdfplumber: {str(e)}. Trying fallback method...")
            try:
                from PyPDF2 import PdfReader
                pdf_reader = PdfReader(pdf)
                for page in pdf_reader.pages:
                    text += page.extract_text() or ""
            except Exception as e:
                st.error(f"Failed to read {pdf.name}: {str(e)}")
                continue
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
    memory = ConversationBufferMemory(
        memory_key='chat_history', 
        return_messages=True
    )
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
        verbose=True
    )
    return conversation_chain

def handle_userinput(user_question):
    if st.session_state.conversation is None:
        st.warning("Please process your PDFs first before asking questions.")
        return
    
    try:
        response = st.session_state.conversation.invoke({'question': user_question})
        st.session_state.chat_history = response['chat_history']

        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(user_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error getting response: {str(e)}")

def main():
    # Ensure event loop exists
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

    load_dotenv()
    
    # Check for API key
    if not os.getenv("GOOGLE_API_KEY"):
        st.error("Please set your GOOGLE_API_KEY in the .env file")
        return
    
    st.set_page_config(page_title="PDF DOCUBOT BY ᴹʳ<ᴘʀᴀᴛɪᴋ࿐",
                     page_icon=":books:",
                     layout="wide")
    
    # Custom CSS injection
    st.markdown(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    # Custom Header with animation
    st.markdown("""
    <div class="main-header-container">
        <div class="main-header">📚 PDF DOCUBOT 🤖</div>
        <div class="sub-header">Chat with your PDFs and gain more knowledge 📜🪄📖✨</div>
        <div class="sub-header" style="font-size: 1.2rem;">BY ᴹʳ<ᴘʀᴀᴛɪᴋ࿐</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin: 20px 0;">
        <p style="font-size: 1.1rem; font-weight: 500;">💡 I will help you skill up your knowledge! I love consuming PDFs and answering your queries 😊</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Chat input
    user_question = st.text_input("💬 Ask a question about your documents:", key="user_question", placeholder="e.g., What is the main topic of these documents?")
    if user_question:
        handle_userinput(user_question)
    
    # Chat history display area
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown("### 💭 Conversation")
    st.markdown("---")
    
    # Display chat history if exists
    if st.session_state.chat_history:
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.markdown(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.markdown(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
    else:
        st.info("💡 Ask a question to start the conversation!")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown('<div class="info-section">', unsafe_allow_html=True)
        st.markdown("### 📁 Document Upload")
        st.markdown("---")
        
        pdf_docs = st.file_uploader(
            "📄 Upload your PDFs here and click on 'Process'", 
            accept_multiple_files=True,
            type=["pdf"],
            help="Upload one or more PDF files to start chatting with them"
        )
        
        if st.button("🔄 PROCESS DOCUMENTS", type="primary", use_container_width=True):
            if not pdf_docs:
                st.warning("⚠️ Please upload at least one PDF file")
                return

            with st.spinner("📊 Processing your documents... This may take a moment."):
                try:
                    raw_text = get_pdf_text(pdf_docs)
                    
                    if not raw_text.strip():
                        st.error("❌ Could not extract any text from the PDFs. They may be scanned images or corrupted.")
                        return

                    text_chunks = get_text_chunks(raw_text)
                    st.info(f"📝 Created {len(text_chunks)} text chunks from your documents")
                    
                    vectorstore = get_vectorstore(text_chunks)
                    st.session_state.conversation = get_conversation_chain(vectorstore)
                    st.success("✅ PDFs processed successfully! You can now ask questions.")
                    
                    # Clear chat history when new documents are processed
                    st.session_state.chat_history = None
                    
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")
        
        st.markdown("---")
        st.markdown("### ℹ️ How to use")
        st.markdown("""
        1. 📁 Upload one or more PDF files
        2. 🔄 Click 'Process Documents'
        3. 💬 Ask questions about your documents
        4. 🤖 Get instant answers from your PDFs
        """)
        
        st.markdown("---")
        st.markdown("### 🚀 Features")
        st.markdown("""
        - 📚 Multiple PDF support
        - 💡 Intelligent Q&A
        - 🔍 Context-aware responses
        - 💾 Conversation memory
        - 🎨 Beautiful UI
        """)
        
        st.markdown("---")
        st.markdown("### 👥 Team")
        st.markdown("""
        - **ANKIT SOME** (24100124089)
        - **SOURADIP GHOSH** (24100124178)
        - **PRATIK ACHARYA** (24100124057)
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        <p>✨ Powered by Google Gemini AI | Made with ❤️ by Team PDF DOCUBOT ✨</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
