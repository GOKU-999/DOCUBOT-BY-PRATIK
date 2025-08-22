css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
    color: #ffffff;
}

/* Main app background - RGB animation */
.stApp {
    background: linear-gradient(-45deg, #ff0000, #ff8000, #ffff00, #80ff00, #00ff00, #00ff80, #00ffff, #0080ff, #0000ff, #8000ff, #ff00ff, #ff0080);
    background-size: 1000% 1000%;
    animation: rgbBackground 30s ease infinite;
    background-attachment: fixed;
}

@keyframes rgbBackground {
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

/* Sidebar with different RGB gradient */
.stSidebar {
    background: linear-gradient(-45deg, #00ffaa, #00aaff, #aa00ff, #ff00aa);
    background-size: 400% 400%;
    animation: sidebarGradient 15s ease infinite;
    border-radius: 15px;
    padding: 20px;
    margin: 10px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
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

/* Ensure text is readable against background */
.stSidebar * {
    color: #ffffff !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
}

/* Header styles with improved readability */
.main-header {
    background: rgba(0, 0, 0, 0.7);
    text-align: center;
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    padding: 15px;
    border-radius: 15px;
    backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

.sub-header {
    background: rgba(0, 0, 0, 0.7);
    text-align: center;
    font-size: 1.5rem;
    font-weight: 400;
    margin-bottom: 2rem;
    padding: 10px;
    border-radius: 10px;
    backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

/* Button styles */
.stButton button {
    background: linear-gradient(-45deg, #ff0000, #00ff00, #0000ff);
    background-size: 400% 400%;
    animation: buttonGradient 10s ease infinite;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-weight: 600;
    width: 100%;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
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
    transform: translateY(-3px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}

/* Input field styles */
.stTextInput input {
    border-radius: 10px;
    padding: 12px;
    border: 2px solid rgba(255, 255, 255, 0.5);
    background: rgba(0, 0, 0, 0.7);
    transition: all 0.3s ease;
    color: white !important;
    backdrop-filter: blur(5px);
}

.stTextInput input:focus {
    border-color: #00ffff;
    box-shadow: 0 0 0 3px rgba(0, 255, 255, 0.3);
    background: rgba(0, 0, 0, 0.8);
}

.stTextInput input::placeholder {
    color: rgba(255, 255, 255, 0.7) !important;
}

/* Chat container */
.chat-container {
    background: rgba(0, 0, 0, 0.7);
    border-radius: 15px;
    padding: 25px;
    margin-bottom: 20px;
    backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}

/* Message styles */
.user-message {
    background: linear-gradient(-45deg, #ff0080, #8000ff, #0080ff);
    background-size: 400% 400%;
    animation: userMessage 8s ease infinite;
    color: white;
    border-radius: 18px 18px 0 18px;
    padding: 15px;
    margin: 12px 0;
    max-width: 80%;
    margin-left: auto;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
}

@keyframes userMessage {
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

.bot-message {
    background: linear-gradient(-45deg, #00ffaa, #00aaff, #aa00ff);
    background-size: 400% 400%;
    animation: botMessage 8s ease infinite;
    color: white;
    border-radius: 18px 18px 18px 0;
    padding: 15px;
    margin: 12px 0;
    max-width: 80%;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
}

@keyframes botMessage {
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

/* Footer */
.footer {
    text-align: center;
    margin-top: 2rem;
    font-size: 0.9rem;
    background: rgba(0, 0, 0, 0.7);
    padding: 10px;
    border-radius: 10px;
    backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
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
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: rgba(255, 0, 128, 0.6);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 0, 128, 0.8);
}

/* Pulse animation for important elements */
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.pulse {
    animation: pulse 2s infinite;
}

/* File uploader styling */
.stFileUploader {
    background: rgba(0, 0, 0, 0.7);
    border-radius: 10px;
    padding: 10px;
    backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

/* Ensure all text in the app is readable */
.stMarkdown, p, h1, h2, h3, h4, h5, h6, li, ul, ol, span, div {
    color: #ffffff !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
}

/* Specific styling for sidebar text elements */
.stSidebar h1, .stSidebar h2, .stSidebar h3, 
.stSidebar h4, .stSidebar h5, .stSidebar h6,
.stSidebar p, .stSidebar label, .stSidebar div {
    color: #ffffff !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
}

/* Make success/error messages readable */
.stAlert {
    background: rgba(0, 0, 0, 0.8) !important;
    backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.stAlert p {
    color: #ffffff !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
}

/* Progress bar styling */
.stProgress > div > div {
    background: linear-gradient(-45deg, #ff0000, #00ff00, #0000ff);
    background-size: 400% 400%;
    animation: buttonGradient 10s ease infinite;
}
</style>
"""

# HTML templates for chat messages
bot_template = """
<div class="bot-message">
    🤖 DOCUBOT: {{MSG}}
</div>
"""

user_template = """
<div class="user-message">
    👤 You: {{MSG}}
</div>
"""
