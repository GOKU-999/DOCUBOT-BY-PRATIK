# To run use: streamlit run app.py If not working then use: python -m streamlit run app.py

import streamlit as st
from dotenv import load_dotenv
import pdfplumber
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
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
        temperature=0.3
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
        st.error("❌ Google API Key Not Found! Please create a .env file with GOOGLE_API_KEY=your_key_here")
        return
    
    # Page configuration
    st.set_page_config(
        page_title="PDF DOCUBOT - Chat with Your PDFs",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS
    st.markdown(css, unsafe_allow_html=True)

    # Initialize session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "processed_files" not in st.session_state:
        st.session_state.processed_files = False

    # Main header
    st.markdown("""
    <div class="main-header-container">
        <div class="main-header">
            📚 PDF DOCUBOT 🤖
        </div>
        <div class="sub-header">
            Chat with your PDFs and gain more knowledge 📜🪄📖✨
        </div>
        <div class="sub-header" style="font-size: 1.2rem;">
            BY ᴹʳ<ᴘʀᴀᴛɪᴋ࿐>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Description
    st.markdown("""
    <div style="text-align: center; margin: 20px 0; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 15px;">
        <p style="font-size: 1.1rem; font-weight: 500;">
            💡 I will help you skill up your knowledge! I love consuming PDFs and answering your queries 😊
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Chat input area
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown("### 💭 Chat with Your Documents")
    st.markdown("---")
    
    # Display chat messages
    if st.session_state.messages:
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(user_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
            else:
                st.markdown(bot_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
    else:
        st.info("💡 Upload and process your PDFs, then start asking questions!")
    
    # Question input
    user_question = st.text_input(
        "💬 Ask a question about your documents:",
        key="user_question",
        placeholder="e.g., What is the main topic of these documents?",
        disabled=not st.session_state.processed_files
    )
    
    if user_question and st.session_state.processed_files:
        handle_userinput(user_question)
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown('<div class="info-section">', unsafe_allow_html=True)
        st.markdown("### 📁 Document Upload")
        st.markdown("---")
        
        pdf_docs = st.file_uploader(
            "📄 Upload your PDFs here", 
            accept_multiple_files=True,
            type=["pdf"],
            help="Upload one or more PDF files to start chatting with them"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            process_button = st.button("🔄 PROCESS", type="primary", use_container_width=True)
        with col2:
            if st.button("🗑️ CLEAR", use_container_width=True):
                st.session_state.conversation = None
                st.session_state.messages = []
                st.session_state.processed_files = False
                st.success("✅ Cleared! Upload new PDFs to start fresh.")
                st.rerun()
        
        if process_button:
            if not pdf_docs:
                st.warning("⚠️ Please upload at least one PDF file")
            else:
                with st.spinner("📊 Processing your documents... This may take a moment."):
                    try:
                        # Extract text from PDFs
                        raw_text = get_pdf_text(pdf_docs)
                        
                        if not raw_text or not raw_text.strip():
                            st.error("❌ Could not extract any text from the PDFs. They may be scanned images or corrupted.")
                        else:
                            # Create text chunks
                            text_chunks = get_text_chunks(raw_text)
                            
                            if not text_chunks:
                                st.error("❌ No text chunks created. The PDFs may be empty or corrupted.")
                            else:
                                st.info(f"📝 Created {len(text_chunks)} text chunks from your documents")
                                
                                # Create vector store
                                vectorstore = get_vectorstore(text_chunks)
                                
                                # Create conversation chain
                                st.session_state.conversation = get_conversation_chain(vectorstore)
                                st.session_state.processed_files = True
                                st.session_state.messages = []  # Clear previous messages
                                
                                st.success(f"✅ Successfully processed {len(pdf_docs)} PDF(s)! You can now ask questions.")
                                
                    except Exception as e:
                        st.error(f"❌ An error occurred: {str(e)}")
                        st.session_state.processed_files = False
        
        st.markdown("---")
        
        # Status indicator
        if st.session_state.processed_files:
            st.success("✅ Status: Ready to answer questions!")
        else:
            st.warning("⏳ Status: No documents processed")
        
        st.markdown("---")
        st.markdown("### ℹ️ How to use")
        st.markdown("""
        1. 📁 **Upload** one or more PDF files
        2. 🔄 **Click** 'PROCESS' to analyze documents
        3. 💬 **Ask** questions about your documents
        4. 🤖 **Get** instant answers from your PDFs
        """)
        
        st.markdown("---")
        st.markdown("### 🚀 Features")
        st.markdown("""
        - 📚 Multiple PDF support
        - 💡 Intelligent Q&A
        - 🔍 Context-aware responses
        - 💾 Conversation memory
        - 🎨 Beautiful animated UI
        - ⚡ Fast document processing
        """)
        
        st.markdown("---")
        st.markdown("### 👥 Team Members")
        st.markdown("""
        | Name | Roll No. |
        |------|----------|
        | **ANKIT SOME** | 24100124089 |
        | **SOURADIP GHOSH** | 24100124178 |
        | **PRATIK ACHARYA** | 24100124057 |
        """)
        
        st.markdown("---")
        st.markdown("### 💡 Tips")
        st.markdown("""
        - Ask specific questions for better answers
        - You can ask follow-up questions
        - The bot remembers conversation context
        - Upload multiple PDFs for cross-reference
        """)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>✨ Powered by Google Gemini AI | Made with ❤️ by Team PDF DOCUBOT ✨</p>
        <p style="font-size: 0.85rem; margin-top: 10px;">© 2024 PDF DOCUBOT - Your Intelligent Document Assistant</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
