css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, 
        rgba(255, 0, 0, 0.7), 
        rgba(0, 255, 0, 0.7), 
        rgba(0, 0, 255, 0.7));
    background-attachment: fixed;
    background-size: cover;
}

.main-header {
    color: white;
    text-align: center;
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    background: rgba(0, 0, 0, 0.6);
    padding: 15px;
    border-radius: 10px;
}

.sub-header {
    color: white;
    text-align: center;
    font-size: 1.5rem;
    font-weight: 400;
    margin-bottom: 2rem;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    background: rgba(0, 0, 0, 0.6);
    padding: 10px;
    border-radius: 8px;
}

.stSidebar {
    background: linear-gradient(135deg, 
        rgba(255, 105, 180, 0.9), 
        rgba(255, 215, 0, 0.9), 
        rgba(135, 206, 250, 0.9)) !important;
    border-radius: 15px;
    padding: 20px;
    margin: 10px;
    border: 2px solid white;
}

.stSidebar .stMarkdown, 
.stSidebar .stSubheader, 
.stSidebar .stText, 
.stSidebar .stInfo {
    color: #000 !important;
    font-weight: 500;
}

.stButton button {
    background: linear-gradient(135deg, #ff0000, #00ff00, #0000ff);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-weight: 600;
    width: 100%;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

.stButton button:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
    background: linear-gradient(135deg, #0000ff, #00ff00, #ff0000);
}

.stTextInput input {
    border-radius: 10px;
    padding: 12px;
    border: 2px solid #ddd;
    transition: all 0.3s ease;
    background: rgba(255, 255, 255, 0.9);
}

.stTextInput input:focus {
    border-color: #ff0000;
    box-shadow: 0 0 0 2px rgba(255, 0, 0, 0.2);
}

.chat-container {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 15px;
    padding: 25px;
    margin-bottom: 20px;
    border: 2px solid #00ff00;
}

.user-message {
    background: linear-gradient(135deg, #ff0000, #0000ff);
    color: white;
    border-radius: 18px 18px 0 18px;
    padding: 15px;
    margin: 12px 0;
    max-width: 80%;
    margin-left: auto;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    border: 1px solid #00ff00;
}

.bot-message {
    background: linear-gradient(135deg, #00ff00, #0000ff);
    color: white;
    border-radius: 18px 18px 18px 0;
    padding: 15px;
    margin: 12px 0;
    max-width: 80%;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    border: 1px solid #ff0000;
}

.footer {
    color: white;
    text-align: center;
    margin-top: 2rem;
    font-size: 0.9rem;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    background: rgba(0, 0, 0, 0.6);
    padding: 10px;
    border-radius: 8px;
}

/* Animation for RGB effect */
@keyframes rgbFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stApp {
    background-size: 400% 400%;
    animation: rgbFlow 15s ease infinite;
}

.stButton button {
    background-size: 400% 400%;
    animation: rgbFlow 8s ease infinite;
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
    background: linear-gradient(#ff0000, #00ff00, #0000ff);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(#0000ff, #00ff00, #ff0000);
}
</style>
"""
