css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Main app background with RGB animation */
.stApp {
    background: linear-gradient(-45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #ffeaa7, #fd79a8, #fdcb6e, #00cec9);
    background-size: 400% 400%;
    animation: rgbGradient 20s ease infinite;
    background-attachment: fixed;
    min-height: 100vh;
}

@keyframes rgbGradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Header section with different RGB colors */
.main-header-container {
    background: linear-gradient(135deg, rgba(255, 107, 107, 0.9), rgba(78, 205, 196, 0.9));
    padding: 2rem;
    border-radius: 20px;
    margin: 1rem;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.main-header {
    color: white;
    text-align: center;
    font-size: 2.8rem;
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.4);
}

.sub-header {
    color: white;
    text-align: center;
    font-size: 1.6rem;
    font-weight: 500;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

/* Sidebar with different RGB colors */
.stSidebar {
    background: linear-gradient(135deg, rgba(69, 183, 209, 0.95), rgba(150, 206, 180, 0.95)) !important;
    border-radius: 20px;
    padding: 25px;
    margin: 15px;
    backdrop-filter: blur(15px);
    border: 2px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
}

.stSidebar h3 {
    color: white !important;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
    font-size: 1.4rem;
    margin-bottom: 1rem;
}

.stSidebar p, .stSidebar li {
    color: #2d3436 !important;
    font-weight: 500;
}

/* Buttons with RGB animation */
.stButton button {
    background: linear-gradient(-45deg, #fd79a8, #fdcb6e, #00cec9, #74b9ff);
    background-size: 300% 300%;
    animation: buttonGradient 8s ease infinite;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 14px 28px;
    font-weight: 600;
    width: 100%;
    transition: all 0.4s ease;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
}

.stButton button:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.3);
}

@keyframes buttonGradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Input field with RGB border */
.stTextInput input {
    border-radius: 12px;
    padding: 14px;
    border: 3px solid;
    border-image: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1) 1;
    background: rgba(255, 255, 255, 0.95);
    transition: all 0.3s ease;
    font-weight: 500;
}

.stTextInput input:focus {
    border-image: linear-gradient(45deg, #fd79a8, #fdcb6e, #00cec9) 1;
    box-shadow: 0 0 20px rgba(253, 121, 168, 0.3);
    background: rgba(255, 255, 255, 1);
}

/* Chat container with different RGB colors */
.chat-container {
    background: linear-gradient(135deg, rgba(253, 203, 110, 0.95), rgba(0, 206, 201, 0.95));
    border-radius: 20px;
    padding: 30px;
    margin: 20px;
    backdrop-filter: blur(12px);
    border: 2px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
}

/* User message with RGB gradient */
.user-message {
    background: linear-gradient(135deg, #74b9ff, #0984e3, #6c5ce7);
    color: white;
    border-radius: 20px 20px 5px 20px;
    padding: 16px;
    margin: 15px 0;
    max-width: 80%;
    margin-left: auto;
    box-shadow: 0 8px 25px rgba(116, 185, 255, 0.3);
    border: 2px solid rgba(255, 255, 255, 0.2);
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
}

/* Bot message with different RGB gradient */
.bot-message {
    background: linear-gradient(135deg, #ffeaa7, #fab1a0, #e17055);
    color: #2d3436;
    border-radius: 20px 20px 20px 5px;
    padding: 16px;
    margin: 15px 0;
    max-width: 80%;
    box-shadow: 0 8px 25px rgba(254, 202, 87, 0.3);
    border: 2px solid rgba(255, 255, 255, 0.2);
    font-weight: 500;
}

/* Footer with RGB gradient */
.footer {
    background: linear-gradient(135deg, rgba(131, 96, 195, 0.9), rgba(46, 191, 145, 0.9));
    color: white;
    text-align: center;
    padding: 1.5rem;
    margin: 2rem 1rem 1rem 1rem;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255, 255, 255, 0.2);
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    font-size: 1rem;
    font-weight: 500;
}

/* Progress bar styling */
.stProgress > div > div {
    background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1, #fd79a8);
    border-radius: 10px;
}

/* Success message styling */
.stSuccess {
    background: linear-gradient(135deg, rgba(46, 213, 115, 0.9), rgba(39, 174, 96, 0.9));
    color: white;
    border-radius: 12px;
    padding: 1rem;
    border: 2px solid rgba(255, 255, 255, 0.3);
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
}

/* Warning message styling */
.stWarning {
    background: linear-gradient(135deg, rgba(254, 202, 87, 0.9), rgba(241, 196, 15, 0.9));
    color: #2d3436;
    border-radius: 12px;
    padding: 1rem;
    border: 2px solid rgba(255, 255, 255, 0.3);
}

/* Error message styling */
.stError {
    background: linear-gradient(135deg, rgba(255, 118, 117, 0.9), rgba(235, 77, 75, 0.9));
    color: white;
    border-radius: 12px;
    padding: 1rem;
    border: 2px solid rgba(255, 255, 255, 0.3);
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
}

/* Info section in sidebar */
.stSidebar .info-section {
    background: rgba(255, 255, 255, 0.2);
    padding: 15px;
    border-radius: 12px;
    margin: 10px 0;
    border: 1px solid rgba(255, 255, 255, 0.3);
}

/* Custom scrollbar */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #ff6b6b, #4ecdc4, #45b7d1);
    border-radius: 10px;
    border: 2px solid rgba(255, 255, 255, 0.3);
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #fd79a8, #fdcb6e, #00cec9);
}

/* Animation for the header */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-30px); }
    to { opacity: 1; transform: translateY(0); }
}

.main-header-container {
    animation: fadeIn 1.2s ease-out;
}

/* Pulse animation for interactive elements */
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.pulse:hover {
    animation: pulse 2s infinite;
}

/* Responsive design */
@media (max-width: 768px) {
    .main-header {
        font-size: 2rem;
    }
    .sub-header {
        font-size: 1.2rem;
    }
    .stSidebar {
        margin: 10px;
        padding: 20px;
    }
    .chat-container {
        margin: 10px;
        padding: 20px;
    }
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
