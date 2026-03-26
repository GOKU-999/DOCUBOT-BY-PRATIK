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
<h1>📚 PDF DocuBot 🤖</h1>
<p>Chat with your PDF documents using AI</p>
<p style="font-size: 0.9rem;">BY ᴹʳ<ᴘʀᴀᴛɪᴋ࿐></p>
</div>
""", unsafe_allow_html=True)

# Main content area
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
st.markdown('<div class="feature-card" style="text-align: center;">', unsafe_allow_html=True)
st.markdown("💡 **Ask questions about your PDFs and get instant answers!**")
st.markdown("Upload documents, process them, and start chatting.")
st.markdown('</div>', unsafe_allow_html=True)

# Chat interface
st.markdown('<div class="feature-card">', unsafe_allow_html=True)
st.subheader("💬 Chat with Your Documents")
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
st.markdown("## 📁 Document Upload")
st.markdown("---")

pdf_docs = st.file_uploader(
    "Upload PDF files",
    accept_multiple_files=True,
    type=["pdf"],
    help="Upload one or more PDF files"
)

if st.button("🚀 Process Documents", use_container_width=True):
    if not pdf_docs:
        st.warning("⚠️ Please upload at least one PDF file.")
    else:
        with st.spinner("📊 Processing PDFs..."):
            try:
                # Extract text
                raw_text = get_pdf_text(pdf_docs)
                
                if not raw_text.strip():
                    st.error("❌ No text could be extracted from the PDFs.")
                else:
                    # Create chunks
                    text_chunks = get_text_chunks(raw_text)
                    st.info(f"📝 Created {len(text_chunks)} text chunks")
                    
                    # Create vector store
                    vectorstore = get_vectorstore(text_chunks)
                    
                    # Create conversation chain
                    st.session_state.conversation = get_conversation_chain(vectorstore)
                    st.session_state.processed = True
                    
                    st.success(f"✅ Successfully processed {len(pdf_docs)} PDF(s)!")
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.session_state.processed = False

st.markdown("---")

# Status
if st.session_state.processed:
    st.success("✅ **Status:** Ready to answer questions!")
else:
    st.warning("⏳ **Status:** No documents processed")

st.markdown("---")

# How to use
st.markdown("### 📖 How to Use")
st.markdown("""
1. **Upload** PDF files
2. **Click** 'Process Documents'
3. **Ask** questions about your documents
4. **Get** AI-powered answers
""")

st.markdown("---")

# Features
st.markdown("### ✨ Features")
st.markdown("""
- 📚 Multiple PDF support
- 💡 Intelligent Q&A
- 🔍 Context-aware responses
- 💾 Conversation memory
- 🎨 Beautiful UI
- ⚡ Fast processing
""")

st.markdown("---")

# Team
st.markdown("### 👥 Team Members")
team_data = {
    "ANKIT SOME": "24100124089",
    "SOURADIP GHOSH": "24100124178",
    "PRATIK ACHARYA": "24100124057"
}
for name, roll in team_data.items():
    st.markdown(f"**{name}** - {roll}")

st.markdown("---")

# Tips
st.markdown("### 💡 Tips")
st.markdown("""
- Ask specific questions
- Use follow-up questions
- Upload related documents
- Clear and reprocess for new topics
""")

# Footer
st.markdown("""
<div class="footer">
<p>✨ Powered by Google Gemini AI | Made with ❤️ by Team PDF DocuBot ✨</p>
</div>
""", unsafe_allow_html=True)

if __name__ == "__main__":
main()
