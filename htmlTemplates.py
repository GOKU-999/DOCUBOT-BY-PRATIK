css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
    color: #2c3e50; /* Dark text for readability */
}

/* Main app background - Light RGB animation */
.stApp {
    background: linear-gradient(-45deg, 
        rgba(255, 200, 200, 0.7), 
        rgba(200, 255, 200, 0.7), 
        rgba(200, 200, 255, 0.7),
        rgba(255, 255, 200, 0.7));
    background-size: 400% 400%;
    animation: lightBackground 20s ease infinite;
    background-attachment: fixed;
}

@keyframes lightBackground {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

/* Sidebar with different light RGB gradient */
.stSidebar {
    background: linear-gradient(-45deg, 
        rgba(230, 240, 255, 0.9), 
        rgba(240, 230, 255, 0.9), 
        rgba(255, 240, 230, 0.9));
    background-size: 400% 400%;
    animation: sidebarGradient 15s ease infinite;
    border-radius: 15px;
    padding: 20px;
    margin: 10px;
    border: 1px solid rgba(255, 255, 255, 0.5);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

@keyframes sidebarGradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

/* Header styles with good contrast */
.main-header {
    color: #2c3e50;
    text-align: center;
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    background: rgba(255, 255, 255, 0.8);
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.sub-header {
    color: #2c3e50;
    text-align: center;
    font-size: 1.5rem;
    font-weight: 500;
    margin-bottom: 2rem;
    background: rgba(255, 255, 255, 0.8);
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Button styles with good contrast */
.stButton button {
    background: linear-gradient(-45deg, 
        rgba(100, 150, 255, 0.8), 
        rgba(150, 100, 255, 0.8), 
        rgba(255, 100, 150, 0.8));
    background-size: 400% 400%;
    animation: buttonGradient 10s ease infinite;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-weight: 600;
    width: 100%;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
}

@keyframes buttonGradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

/* Input field styles */
.stTextInput input {
    border-radius: 10px;
    padding: 12px;
    border: 2px solid #ddd;
    background: rgba(255, 255, 255, 0.95);
    transition: all 0.3s ease;
    color: #2c3e50;
}

.stTextInput input:focus {
    border-color: #6c5ce7;
    box-shadow: 0 0 0 3px rgba(108, 92, 231, 0.2);
    background: rgba(255, 255, 255, 1);
}

/* Chat container */
.chat-container {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 15px;
    padding: 25px;
    margin-bottom: 20px;
    border: 1px solid rgba(255, 255, 255, 0.5);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

/* Message styles with good contrast */
.user-message {
    background: linear-gradient(-45deg, 
        rgba(100, 180, 255, 0.9), 
        rgba(150, 120, 255, 0.9));
    color: white;
    border-radius: 18px 18px 0 18px;
    padding: 15px;
    margin: 12px 0;
    max-width: 80%;
    margin-left: auto;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.bot-message {
    background: linear-gradient(-45deg, 
        rgba(120, 220, 200, 0.9), 
        rgba(100, 180, 220, 0.9));
    color: white;
    border-radius: 18px 18px 18px 0;
    padding: 15px;
    margin: 12px 0;
    max-width: 80%;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

/* Footer */
.footer {
    color: #2c3e50;
    text-align: center;
    margin-top: 2rem;
    font-size: 0.9rem;
    background: rgba(255, 255, 255, 0.8);
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Animation for the header */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}

.main-header {
    animation: fadeIn 1s ease-out;
}

.sub-header {
    animation: fadeIn 1s ease-out 0.3s both;
}

/* Custom scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.3);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: rgba(100, 150, 255, 0.6);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(100, 150, 255, 0.8);
}

/* Text elements with good contrast */
h1, h2, h3, h4, h5, h6 {
    color: #2c3e50 !important;
}

p, div, span {
    color: #2c3e50 !important;
}

/* File uploader styling */
.stFileUploader {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 10px;
    padding: 10px;
}

/* Additional contrast for sidebar text */
.stSidebar h1, .stSidebar h2, .stSidebar h3, 
.stSidebar h4, .stSidebar h5, .stSidebar h6,
.stSidebar p, .stSidebar div, .stSidebar span {
    color: #2c3e50 !important;
}

/* Ensure all text in the app has good contrast */
.stApp h1, .stApp h2, .stApp h3, 
.stApp h4, .stApp h5, .stApp h6,
.stApp p, .stApp div, .stApp span,
.stApp label, .stApp input {
    color: #2c3e50 !important;
}

/* Specific styling for text in input areas */
.stTextInput>div>div>input {
    color: #2c3e50 !important;
}

/* Make sure placeholders are also visible */
.stTextInput>div>div>input::placeholder {
    color: #7f8c8d !important;
}
</style>
"""

# HTML templates for chat messages - use string formatting instead of template variables
bot_template = """
<div class="bot-message">
    🤖 DOCUBOT: {MSG}
</div>
"""

user_template = """
<div class="user-message">
    👤 You: {MSG}
</div>
"""
