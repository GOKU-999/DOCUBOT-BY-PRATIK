css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

/* Main app background - RGB gradient animation */
.stApp {
    background: linear-gradient(-45deg, #ff0000, #00ff00, #0000ff, #ffff00, #ff00ff, #00ffff);
    background-size: 400% 400%;
    animation: rgbWave 20s ease infinite;
    background-attachment: fixed;
}

@keyframes rgbWave {
    0% {
        background-position: 0% 50%;
        background: linear-gradient(-45deg, #ff0000, #00ff00, #0000ff, #ffff00);
    }
    25% {
        background-position: 50% 100%;
        background: linear-gradient(-45deg, #00ff00, #0000ff, #ffff00, #ff00ff);
    }
    50% {
        background-position: 100% 50%;
        background: linear-gradient(-45deg, #0000ff, #ffff00, #ff00ff, #00ffff);
    }
    75% {
        background-position: 50% 0%;
        background: linear-gradient(-45deg, #ffff00, #ff00ff, #00ffff, #ff0000);
    }
    100% {
        background-position: 0% 50%;
        background: linear-gradient(-45deg, #ff00ff, #00ffff, #ff0000, #00ff00);
    }
}

/* Headers with different RGB effects */
.main-header {
    background: linear-gradient(135deg, #ff0000, #ff8000, #ffff00);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    font-size: 2.8rem;
    font-weight: 800;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    animation: headerGlow 3s ease-in-out infinite alternate;
}

@keyframes headerGlow {
    from {
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2), 0 0 20px rgba(255, 0, 0, 0.5);
    }
    to {
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2), 0 0 30px rgba(0, 255, 0, 0.5), 0 0 40px rgba(0, 0, 255, 0.3);
    }
}

.sub-header {
    background: linear-gradient(135deg, #00ff00, #00ffff, #0000ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    font-size: 1.8rem;
    font-weight: 600;
    margin-bottom: 2rem;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
}

/* Sidebar with unique RGB gradient */
.stSidebar {
    background: linear-gradient(135deg, rgba(255, 0, 0, 0.9), rgba(0, 255, 0, 0.9), rgba(0, 0, 255, 0.9)) !important;
    border-radius: 20px;
    padding: 25px;
    margin: 15px;
    backdrop-filter: blur(15px);
    border: 2px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    animation: sidebarPulse 8s ease-in-out infinite;
}

@keyframes sidebarPulse {
    0% { background: linear-gradient(135deg, rgba(255, 0, 0, 0.9), rgba(0, 255, 0, 0.9)); }
    33% { background: linear-gradient(135deg, rgba(0, 255, 0, 0.9), rgba(0, 0, 255, 0.9)); }
    66% { background: linear-gradient(135deg, rgba(0, 0, 255, 0.9), rgba(255, 0, 255, 0.9)); }
    100% { background: linear-gradient(135deg, rgba(255, 0, 255, 0.9), rgba(255, 0, 0, 0.9)); }
}

/* Button with RGB animation */
.stButton button {
    background: linear-gradient(-45deg, #ff0000, #00ff00, #0000ff, #ff00ff);
    background-size: 400% 400%;
    animation: buttonRGB 6s ease infinite;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 15px 30px;
    font-weight: 700;
    width: 100%;
    transition: all 0.4s ease;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    text-transform: uppercase;
    letter-spacing: 1px;
}

@keyframes buttonRGB {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stButton button:hover {
    transform: translateY(-5px) scale(1.05);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
    animation: buttonRGB 3s ease infinite;
}

/* Input field with RGB border */
.stTextInput input {
    border-radius: 12px;
    padding: 15px;
    border: 3px solid;
    border-image: linear-gradient(45deg, #ff0000, #00ff00, #0000ff) 1;
    background: rgba(255, 255, 255, 0.95);
    transition: all 0.3s ease;
    font-size: 1rem;
}

.stTextInput input:focus {
    border-image: linear-gradient(45deg, #ff00ff, #ffff00, #00ffff) 1;
    box-shadow: 0 0 20px rgba(255, 0, 255, 0.3);
    background: rgba(255, 255, 255, 1);
}

/* Chat container with RGB gradient */
.chat-container {
    background: linear-gradient(135deg, rgba(255, 0, 255, 0.9), rgba(0, 255, 255, 0.9), rgba(255, 255, 0, 0.9));
    border-radius: 20px;
    padding: 30px;
    margin-bottom: 25px;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255, 255, 255, 0.4);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    animation: chatGlow 10s ease-in-out infinite;
}

@keyframes chatGlow {
    0% { box-shadow: 0 10px 30px rgba(255, 0, 0, 0.3); }
    33% { box-shadow: 0 10px 30px rgba(0, 255, 0, 0.3); }
    66% { box-shadow: 0 10px 30px rgba(0, 0, 255, 0.3); }
    100% { box-shadow: 0 10px 30px rgba(255, 0, 255, 0.3); }
}

/* User message with RGB gradient */
.user-message {
    background: linear-gradient(135deg, #ff0000, #ff8000, #ffff00);
    color: white;
    border-radius: 20px 20px 0 20px;
    padding: 18px;
    margin: 15px 0;
    max-width: 80%;
    margin-left: auto;
    box-shadow: 0 8px 25px rgba(255, 0, 0, 0.3);
    animation: messageSlide 0.5s ease-out;
    border: 2px solid rgba(255, 255, 255, 0.3);
}

/* Bot message with different RGB gradient */
.bot-message {
    background: linear-gradient(135deg, #0000ff, #8000ff, #ff00ff);
    color: white;
    border-radius: 20px 20px 20px 0;
    padding: 18px;
    margin: 15px 0;
    max-width: 80%;
    box-shadow: 0 8px 25px rgba(0, 0, 255, 0.3);
    animation: messageSlide 0.5s ease-out;
    border: 2px solid rgba(255, 255, 255, 0.3);
}

@keyframes messageSlide {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Footer with RGB text */
.footer {
    background: linear-gradient(135deg, #ff0000, #00ff00, #0000ff, #ff00ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    margin-top: 3rem;
    font-size: 1.1rem;
    font-weight: 600;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    animation: footerRGB 8s ease-in-out infinite;
}

@keyframes footerRGB {
    0% { background: linear-gradient(135deg, #ff0000, #00ff00); }
    33% { background: linear-gradient(135deg, #00ff00, #0000ff); }
    66% { background: linear-gradient(135deg, #0000ff, #ff00ff); }
    100% { background: linear-gradient(135deg, #ff00ff, #ff0000); }
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 12px;
}

::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #ff0000, #00ff00, #0000ff);
    border-radius: 10px;
    border: 2px solid rgba(255, 255, 255, 0.3);
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #ff00ff, #ffff00, #00ffff);
}

/* Progress bar styling */
.stProgress > div > div {
    background: linear-gradient(135deg, #ff0000, #00ff00, #0000ff);
    animation: progressRGB 4s ease-in-out infinite;
}

@keyframes progressRGB {
    0% { background: linear-gradient(135deg, #ff0000, #00ff00); }
    50% { background: linear-gradient(135deg, #00ff00, #0000ff); }
    100% { background: linear-gradient(135deg, #0000ff, #ff0000); }
}

/* Success message styling */
.stSuccess {
    background: linear-gradient(135deg, rgba(0, 255, 0, 0.9), rgba(0, 200, 0, 0.9));
    border-radius: 15px;
    border-left: 5px solid #00ff00;
}

/* Error message styling */
.stError {
    background: linear-gradient(135deg, rgba(255, 0, 0, 0.9), rgba(200, 0, 0, 0.9));
    border-radius: 15px;
    border-left: 5px solid #ff0000;
}

/* Warning message styling */
.stWarning {
    background: linear-gradient(135deg, rgba(255, 165, 0, 0.9), rgba(200, 120, 0, 0.9));
    border-radius: 15px;
    border-left: 5px solid #ffa500;
}

/* Info message styling */
.stInfo {
    background: linear-gradient(135deg, rgba(0, 191, 255, 0.9), rgba(0, 150, 200, 0.9));
    border-radius: 15px;
    border-left: 5px solid #00bfff;
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
