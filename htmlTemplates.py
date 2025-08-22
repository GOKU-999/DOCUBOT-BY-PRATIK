css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
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

/* Header styles */
.main-header {
    color: white;
    text-align: center;
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    background: rgba(0, 0, 0, 0.3);
    padding: 15px;
    border-radius: 15px;
    backdrop-filter: blur(5px);
}

.sub-header {
    color: white;
    text-align: center;
    font-size: 1.5rem;
    font-weight: 400;
    margin-bottom: 2rem;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    background: rgba(0, 0, 0, 0.3);
    padding: 10px;
    border-radius: 10px;
    backdrop-filter: blur(5px);
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
    border: 2px solid rgba(255, 255, 255, 0.3);
    background: rgba(255, 255, 255, 0.9);
    transition: all 0.3s ease;
}

.stTextInput input:focus {
    border-color: #00ffff;
    box-shadow: 0 0 0 3px rgba(0, 255, 255, 0.3);
    background: rgba(255, 255, 255, 1);
}

/* Chat container */
.chat-container {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 15px;
    padding: 25px;
    margin-bottom: 20px;
    backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.5);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
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
    color: white;
    text-align: center;
    margin-top: 2rem;
    font-size: 0.9rem;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    background: rgba(0, 0, 0, 0.3);
    padding: 10px;
    border-radius: 10px;
    backdrop-filter: blur(5px);
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
    background: rgba(255, 255, 255, 0.9);
    border-radius: 10px;
    padding: 10px;
    backdrop-filter: blur(5px);
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
