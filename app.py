import streamlit as st
import pdfplumber
import os
from dotenv import load_dotenv

# Page config
st.set_page_config(
    page_title="PDF DocuBot",
    page_icon="📚",
    layout="wide"
)

# Load environment variables
load_dotenv()

# Simple CSS
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
        width: 100%;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

def extract_text_from_pdf(pdf_file):
    """Extract text from a single PDF file"""
    text = ""
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
    return text

def search_in_text(text, query):
    """Simple search function (without AI)"""
    if not text:
        return "No text available to search."
    
    text_lower = text.lower()
    query_lower = query.lower()
    
    if query_lower in text_lower:
        # Find context around the query
        words = text.split()
        found_contexts = []
        
        for i, word in enumerate(words):
            if query_lower in word.lower():
                start = max(0, i - 20)
                end = min(len(words), i + 20)
                context = " ".join(words[start:end])
                found_contexts.append("..." + context + "...")
                
                if len(found_contexts) >= 3:
                    break
        
        if found_contexts:
            return "\n\n".join(found_contexts)
        else:
            return "Found the query in the document, but couldn't extract context."
    else:
        return "The query was not found in any of the uploaded documents."

def main():
    # Check for API key (optional for this simple version)
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.info("Note: Add your Google API key to .env file for AI-powered responses. Using basic search for now.")
    
    # Initialize session state
    if "processed_text" not in st.session_state:
        st.session_state.processed_text = ""
    if "processed" not in st.session_state:
        st.session_state.processed = False
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>PDF DocuBot</h1>
        <p>Chat with your PDF documents</p>
        <p>BY MR PRATIK</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content area
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("**Ask questions about your PDFs and get answers!**")
        st.markdown("Upload documents, process them, and start chatting.")
    
    # Chat interface
    st.markdown("---")
    st.subheader("Chat with Your Documents")
    st.markdown("---")
    
    # Display chat history
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="user-message">
                <strong>You:</strong><br>{message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="bot-message">
                <strong>DocuBot:</strong><br>{message["content"]}
            </div>
            """, unsafe_allow_html=True)
    
    # Question input
    user_question = st.text_input(
        "Ask a question:",
        placeholder="e.g., What is this document about?",
        disabled=not st.session_state.processed,
        key="question_input"
    )
    
    if user_question and st.session_state.processed:
        # Add user question to chat
        st.session_state.chat_history.append({"role": "user", "content": user_question})
        
        # Get answer
        with st.spinner("Searching..."):
            answer = search_in_text(st.session_state.processed_text, user_question)
        
        # Add bot response to chat
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        
        # Rerun to update display
        st.rerun()
    
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
                        all_text = ""
                        for pdf in pdf_docs:
                            text = extract_text_from_pdf(pdf)
                            if text:
                                all_text += f"\n\n--- {pdf.name} ---\n\n{text}"
                        
                        if not all_text.strip():
                            st.error("No text could be extracted from the PDFs.")
                        else:
                            st.session_state.processed_text = all_text
                            st.session_state.processed = True
                            st.session_state.chat_history = []  # Clear chat history
                            st.success(f"Successfully processed {len(pdf_docs)} PDF(s)!")
                            
                            # Show preview
                            with st.expander("Text Preview"):
                                st.text(all_text[:1000] + "...")
                            
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
        3. Ask questions
        4. Get answers
        """)
        
        st.markdown("---")
        
        # Features
        st.markdown("### Features")
        st.markdown("""
        - PDF text extraction
        - Keyword search
        - Chat interface
        - Multiple PDF support
        """)
        
        st.markdown("---")
        
        # Team
        st.markdown("### Team Members")
        st.markdown("**ANKIT SOME** - 24100124089")
        st.markdown("**SOURADIP GHOSH** - 24100124178")
        st.markdown("**PRATIK ACHARYA** - 24100124057")
        
        st.markdown("---")
        
        # Tips
        st.markdown("### Tips")
        st.markdown("""
        - Ask specific questions
        - Use keywords from your documents
        - Upload clear, text-based PDFs
        - For scanned PDFs, text extraction may be limited
        """)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>Made with Love by Team PDF DocuBot</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
