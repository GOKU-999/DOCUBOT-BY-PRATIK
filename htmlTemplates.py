css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    background-attachment: fixed;
}

@keyframes gradient {
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

.main-header {
    color: white;
    text-align: center;
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.sub-header {
    color: white;
    text-align: center;
    font-size: 1.5rem;
    font-weight: 400;
    margin-bottom: 2rem;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
}

.stSidebar {
    background: rgba(255, 255, 255, 0.95) !important;
    border-radius: 15px;
    padding: 20px;
    margin: 10px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.5);
}

.stButton button {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-weight: 600;
    width: 100%;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.stButton button:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

.stTextInput input {
    border-radius: 10px;
    padding: 12px;
    border: 2px solid #ddd;
    transition: all 0.3s ease;
}

.stTextInput input:focus {
    border-color: #23a6d5;
    box-shadow: 0 0 0 2px rgba(35, 166, 213, 0.2);
}

.chat-container {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 15px;
    padding: 25px;
    margin-bottom: 20px;
    backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.5);
}

.user-message {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    color: white;
    border-radius: 18px 18px 0 18px;
    padding: 15px;
    margin: 12px 0;
    max-width: 80%;
    margin-left: auto;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.bot-message {
    background: #f0f2f6;
    color: #333;
    border-radius: 18px 18px 18px 0;
    padding: 15px;
    margin: 12px 0;
    max-width: 80%;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
}

.footer {
    color: white;
    text-align: center;
    margin-top: 2rem;
    font-size: 0.9rem;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
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
    background: rgba(35, 166, 213, 0.6);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(35, 166, 213, 0.8);
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

.rgb-text {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
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
