import streamlit as st
from dotenv import load_dotenv
import pdfplumber
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import os

# Page config - MUST be the first Streamlit command
st.set_page_config(
    page_title="PDF DocuBot",
    page_icon="📚",
    layout="wide"
)

# Load environment variables
load_dotenv()

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .main-header {
        text-align: center;
        padding: 2rem;
        background: rgba(255,255,255,0.1);
        border-radius: 20px;
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
    }
    
    .main-header h1 {
        font-size: 3rem;
        color: white;
        margin-bottom: 0.5rem;
    }
    
    .main-header p {
        color: white;
        font-size: 1.2rem;
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 1rem;
        border-radius: 20px;
        margin: 0.5rem 0;
        max-width: 70%;
        margin-left: auto;
    }
    
    .bot-message {
        background: rgba(255,255,255,0.95);
        color: #333;
        padding: 1rem;
        border-radius: 20px;
        margin: 0.5rem 0;
        max-width: 70%;
        border-left: 4px solid #667eea;
    }
    
    .feature-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .footer {
        text-align: center;
        padding: 1rem;
        margin-top: 2rem;
        background: rgba(0,0,0,0.2);
        border-radius: 10px;
        color: white;
    }
    
    .stButton button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

def get_pdf_text(pdf_docs):
    """Extract text from uploaded PDF files"""
    text = ""
    for pdf in pdf_docs:
        try:
            with pdfplumber.open(pdf) as pdf_file:
                for page in pdf_file.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
        except Exception as e:
            st.error(f"Error reading {pdf.name}: {str(e)}")
            continue
    return text

def get_text_chunks(text):
    """Split text into manageable chunks"""
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    """Create vector store from text chunks"""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    """Create conversation chain with memory"""
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.3
    )
    
    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True
    )
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        memory=memory
    )
    return conversation_chain

def handle_user_input(user_question):
    """Process user question and generate response"""
    if st.session_state.conversation is None:
        st.warning("Please upload and process PDF files first.")
        return
    
    try:
        with st.spinner("Thinking..."):
            response = st.session_state.conversation({"question": user_question})
        
        # Display user question
        st.markdown(f"""
        <div class="user-message">
            <strong>You:</strong><br>{user_question}
        </div>
        """, unsafe_allow_html=True)
        
        # Display bot response
        st.markdown(f"""
        <div class="bot-message">
            <strong>DocuBot:</strong><br>{response['answer']}
        </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error: {str(e)}")

def main():
    # Check API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("""
        Google API Key Not Found!
        
        Please create a .env file in the same folder with:
        GOOGLE_API_KEY=AIzaSyDENDOYn0e3BF7fTxLr6m1C4XbKrzXAuk4
        
        Get your API key from: https://makersuite.google.com/app/apikey
        """)
        return
    
    # Initialize session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "processed" not in st.session_state:
        st.session_state.processed = False
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>PDF DocuBot</h1>
        <p>Chat with your PDF documents using AI</p>
        <p style="font-size: 0.9rem;">BY MR PRATIK</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content area
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="feature-card" style="text-align: center;">', unsafe_allow_html=True)
        st.markdown("**Ask questions about your PDFs and get instant answers!**")
        st.markdown("Upload documents, process them, and start chatting.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Chat interface
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("Chat with Your Documents")
    st.markdown("---")
    
    user_question = st.text_input(
        "Ask a question:",
        placeholder="e.g., What is the main topic of these documents?",
        disabled=not st.session_state.processed,
        key="question_input"
    )
    
    if user_question and st.session_state.processed:
        handle_user_input(user_question)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("## Document Upload")
        st.markdown("---")
        
        pdf_docs = st.file_uploader(
            "Upload PDF files",
            accept_multiple_files=True,
            type=["pdf"],
            help="Upload one or more PDF files"
        )
        
        if st.button("Process Documents", use_container_width=True):
            if not pdf_docs:
                st.warning("Please upload at least one PDF file.")
            else:
                with st.spinner("Processing PDFs..."):
                    try:
                        # Extract text
                        raw_text = get_pdf_text(pdf_docs)
                        
                        if not raw_text.strip():
                            st.error("No text could be extracted from the PDFs.")
                        else:
                            # Create chunks
                            text_chunks = get_text_chunks(raw_text)
                            st.info(f"Created {len(text_chunks)} text chunks")
                            
                            # Create vector store
                            vectorstore = get_vectorstore(text_chunks)
                            
                            # Create conversation chain
                            st.session_state.conversation = get_conversation_chain(vectorstore)
                            st.session_state.processed = True
                            
                            st.success(f"Successfully processed {len(pdf_docs)} PDF(s)!")
                            
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
                        st.session_state.processed = False
        
        st.markdown("---")
        
        # Status
        if st.session_state.processed:
            st.success("Status: Ready to answer questions!")
        else:
            st.warning("Status: No documents processed")
        
        st.markdown("---")
        
        # How to use
        st.markdown("### How to Use")
        st.markdown("""
        1. Upload PDF files
        2. Click 'Process Documents'
        3. Ask questions about your documents
        4. Get AI-powered answers
        """)
        
        st.markdown("---")
        
        # Features
        st.markdown("### Features")
        st.markdown("""
        - Multiple PDF support
        - Intelligent Q&A
        - Context-aware responses
        - Conversation memory
        - Beautiful UI
        - Fast processing
        """)
        
        st.markdown("---")
        
        # Team
        st.markdown("### Team Members")
        team_data = {
            "ANKIT SOME": "24100124089",
            "SOURADIP GHOSH": "24100124178",
            "PRATIK ACHARYA": "24100124057"
        }
        for name, roll in team_data.items():
            st.markdown(f"**{name}** - {roll}")
        
        st.markdown("---")
        
        # Tips
        st.markdown("### Tips")
        st.markdown("""
        - Ask specific questions
        - Use follow-up questions
        - Upload related documents
        - Clear and reprocess for new topics
        """)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>Powered by Google Gemini AI | Made with Love by Team PDF DocuBot</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
