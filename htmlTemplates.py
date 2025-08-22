css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, rgb(0, 123, 255), rgb(255, 0, 150));
    background-attachment: fixed;
    background-size: cover;
}

.main-header {
    color: white;
    text-align: center;
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.sub-header {
    color: white;
    text-align: center;
    font-size: 1.5rem;
    font-weight: 400;
    margin-bottom: 2rem;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
}

.stSidebar {
    background: rgba(255, 255, 255, 0.9) !important;
    border-radius: 15px;
    padding: 20px;
    margin: 10px;
}

.stButton button {
    background: linear-gradient(135deg, rgb(0, 123, 255), rgb(255, 0, 150));
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: 500;
    width: 100%;
    transition: all 0.3s ease;
}

.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.stTextInput input {
    border-radius: 8px;
    padding: 10px;
}

.chat-container {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 20px;
}

.user-message {
    background: linear-gradient(135deg, rgb(0, 123, 255), rgb(255, 0, 150));
    color: white;
    border-radius: 15px 15px 0 15px;
    padding: 12px;
    margin: 10px 0;
    max-width: 80%;
    margin-left: auto;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.bot-message {
    background: #f0f2f6;
    color: #333;
    border-radius: 15px 15px 15px 0;
    padding: 12px;
    margin: 10px 0;
    max-width: 80%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.footer {
    color: white;
    text-align: center;
    margin-top: 2rem;
    font-size: 0.9rem;
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
