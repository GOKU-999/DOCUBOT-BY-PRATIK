<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Chat Interface</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            min-height: 100vh;
            background: linear-gradient(-45deg, #1a1a2e, #16213e, #0f3460);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            color: #f0f0f0;
            display: flex;
            overflow-x: hidden;
        }
        
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .container {
            display: flex;
            width: 100%;
            max-width: 1400px;
            margin: 0 auto;
            height: 100vh;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
        }
        
        .sidebar {
            width: 280px;
            background: rgba(25, 25, 45, 0.85);
            padding: 25px 15px;
            border-right: 1px solid rgba(255, 255, 255, 0.1);
            display: flex;
            flex-direction: column;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
            z-index: 10;
        }
        
        .logo {
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .logo h1 {
            font-size: 24px;
            font-weight: 700;
            background: linear-gradient(to right, #ff7ae9, #7a8cff, #5ef1e3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { text-shadow: 0 0 5px rgba(122, 140, 255, 0.5); }
            50% { text-shadow: 0 0 20px rgba(122, 140, 255, 0.8); }
            100% { text-shadow: 0 0 5px rgba(122, 140, 255, 0.5); }
        }
        
        .sidebar-menu {
            list-style: none;
            margin-top: 20px;
        }
        
        .sidebar-menu li {
            padding: 12px 15px;
            margin-bottom: 8px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
        }
        
        .sidebar-menu li:hover {
            background: rgba(122, 140, 255, 0.2);
            transform: translateX(5px);
        }
        
        .sidebar-menu li.active {
            background: rgba(122, 140, 255, 0.3);
            box-shadow: 0 0 10px rgba(122, 140, 255, 0.3);
        }
        
        .sidebar-menu i {
            margin-right: 10px;
            font-size: 18px;
            color: #7a8cff;
        }
        
        .main-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            padding: 20px;
            position: relative;
        }
        
        .chat-header {
            padding: 15px 20px;
            background: rgba(25, 25, 45, 0.7);
            border-radius: 12px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }
        
        .chat-title h2 {
            font-size: 20px;
            font-weight: 600;
        }
        
        .chat-title p {
            font-size: 14px;
            color: #7a8cff;
            margin-top: 4px;
        }
        
        .chat-container {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            background: rgba(25, 25, 45, 0.6);
            border-radius: 12px;
            margin-bottom: 20px;
            box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.2);
        }
        
        .message {
            margin-bottom: 25px;
            max-width: 80%;
            animation: fadeIn 0.5s ease;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .user-message {
            margin-left: auto;
        }
        
        .message-inner {
            padding: 15px 20px;
            border-radius: 18px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        
        .bot-message .message-inner {
            background: rgba(35, 35, 65, 0.9);
            border-bottom-left-radius: 5px;
        }
        
        .user-message .message-inner {
            background: rgba(94, 241, 227, 0.15);
            border-bottom-right-radius: 5px;
            border: 1px solid rgba(94, 241, 227, 0.3);
        }
        
        .message-header {
            display: flex;
            align-items: center;
            margin-bottom: 8px;
        }
        
        .message-header img {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            margin-right: 10px;
            object-fit: cover;
        }
        
        .message-header h3 {
            font-size: 14px;
            font-weight: 600;
        }
        
        .bot-message .message-header h3 {
            color: #ff7ae9;
        }
        
        .user-message .message-header h3 {
            color: #5ef1e3;
        }
        
        .message-content {
            line-height: 1.5;
            font-size: 15px;
        }
        
        .message-content p {
            margin-bottom: 10px;
        }
        
        .input-area {
            display: flex;
            background: rgba(25, 25, 45, 0.7);
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }
        
        .input-area input {
            flex: 1;
            padding: 16px 20px;
            background: transparent;
            border: none;
            color: #f0f0f0;
            font-size: 15px;
        }
        
        .input-area input:focus {
            outline: none;
        }
        
        .input-area input::placeholder {
            color: rgba(240, 240, 240, 0.6);
        }
        
        .input-area button {
            padding: 0 25px;
            background: linear-gradient(to right, #ff7ae9, #7a8cff);
            border: none;
            color: white;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .input-area button:hover {
            background: linear-gradient(to right, #ff94ee, #8f9eff);
            box-shadow: 0 0 15px rgba(122, 140, 255, 0.5);
        }
        
        .floating-particles {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            pointer-events: none;
            z-index: -1;
        }
        
        .particle {
            position: absolute;
            border-radius: 50%;
            background: rgba(122, 140, 255, 0.3);
            animation: float 15s infinite linear;
        }
        
        @keyframes float {
            0% { transform: translateY(0) translateX(0) rotate(0deg); }
            100% { transform: translateY(-100vh) translateX(100px) rotate(360deg); }
        }
        
        @media (max-width: 768px) {
            .container {
                flex-direction: column;
            }
            
            .sidebar {
                width: 100%;
                height: auto;
                padding: 15px;
            }
            
            .sidebar-menu {
                display: flex;
                overflow-x: auto;
                margin-bottom: 10px;
            }
            
            .sidebar-menu li {
                white-space: nowrap;
            }
            
            .message {
                max-width: 90%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="sidebar">
            <div class="logo">
                <h1>DocuBot Assistant</h1>
            </div>
            
            <ul class="sidebar-menu">
                <li class="active"><i>💬</i> New Chat</li>
                <li><i>📁</i> Documents</li>
                <li><i>⚙️</i> Settings</li>
                <li><i>🔍</i> Search</li>
                <li><i>📊</i> Analytics</li>
                <li><i>🙋</i> Help</li>
            </ul>
            
            <div style="margin-top: auto; padding: 15px; background: rgba(0,0,0,0.2); border-radius: 8px;">
                <p style="font-size: 13px; line-height: 1.4;">DocuBot helps you analyze and understand your documents through AI-powered conversations.</p>
            </div>
        </div>
        
        <div class="main-content">
            <div class="chat-header">
                <div class="chat-title">
                    <h2>Document Analysis</h2>
                    <p>Ask questions about your uploaded documents</p>
                </div>
                <div class="chat-actions">
                    <button style="background: rgba(122, 140, 255, 0.3); color: white; border: none; padding: 8px 15px; border-radius: 6px; cursor: pointer;">Upload New</button>
                </div>
            </div>
            
            <div class="chat-container">
                <div class="message bot-message">
                    <div class="message-inner">
                        <div class="message-header">
                            <h3>DocuBot</h3>
                        </div>
                        <div class="message-content">
                            <p>Hello! I'm DocuBot, your document analysis assistant. I can help you understand and extract information from your uploaded documents.</p>
                            <p>How can I assist you today?</p>
                        </div>
                    </div>
                </div>
                
                <div class="message user-message">
                    <div class="message-inner">
                        <div class="message-header">
                            <h3>You</h3>
                        </div>
                        <div class="message-content">
                            <p>Can you summarize the main points from the uploaded PDF about quarterly sales?</p>
                        </div>
                    </div>
                </div>
                
                <div class="message bot-message">
                    <div class="message-inner">
                        <div class="message-header">
                            <h3>DocuBot</h3>
                        </div>
                        <div class="message-content">
                            <p>Based on the Q3 sales report, the main points are:</p>
                            <ul style="padding-left: 20px; margin: 10px 0;">
                                <li>Total revenue increased by 15% compared to Q2</li>
                                <li>New product line contributed 22% of total sales</li>
                                <li>European market showed strongest growth at 28%</li>
                                <li>Q4 projection estimates 20% growth with holiday season</li>
                            </ul>
                            <p>Would you like me to elaborate on any specific section?</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="input-area">
                <input type="text" placeholder="Ask something about your documents...">
                <button>Send</button>
            </div>
        </div>
        
        <div class="floating-particles" id="particles"></div>
    </div>

    <script>
        // Create floating particles for background animation
        document.addEventListener('DOMContentLoaded', function() {
            const particlesContainer = document.getElementById('particles');
            const particleCount = 20;
            
            for (let i = 0; i < particleCount; i++) {
                const particle = document.createElement('div');
                particle.classList.add('particle');
                
                // Random size between 40 and 150px
                const size = Math.random() * 110 + 40;
                particle.style.width = `${size}px`;
                particle.style.height = `${size}px`;
                
                // Random position
                particle.style.left = `${Math.random() * 100}%`;
                particle.style.top = `${Math.random() * 100}%`;
                
                // Random animation duration between 10 and 25s
                const duration = Math.random() * 15 + 10;
                particle.style.animationDuration = `${duration}s`;
                
                // Random delay
                particle.style.animationDelay = `${Math.random() * 5}s`;
                
                // Random opacity
                particle.style.opacity = Math.random() * 0.4 + 0.1;
                
                particlesContainer.appendChild(particle);
            }
            
            // Simple send message functionality
            const input = document.querySelector('input');
            const button = document.querySelector('button');
            const chatContainer = document.querySelector('.chat-container');
            
            button.addEventListener('click', addMessage);
            input.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') addMessage();
            });
            
            function addMessage() {
                const messageText = input.value.trim();
                if (messageText === '') return;
                
                const messageDiv = document.createElement('div');
                messageDiv.classList.add('message', 'user-message');
                messageDiv.innerHTML = `
                    <div class="message-inner">
                        <div class="message-header">
                            <h3>You</h3>
                        </div>
                        <div class="message-content">
                            <p>${messageText}</p>
                        </div>
                    </div>
                `;
                
                chatContainer.appendChild(messageDiv);
                input.value = '';
                
                // Scroll to bottom
                chatContainer.scrollTop = chatContainer.scrollHeight;
                
                // Simulate bot response after a delay
                setTimeout(() => {
                    const botResponse = document.createElement('div');
                    botResponse.classList.add('message', 'bot-message');
                    botResponse.innerHTML = `
                        <div class="message-inner">
                            <div class="message-header">
                                <h3>DocuBot</h3>
                            </div>
                            <div class="message-content">
                                <p>I understand you asked: "${messageText}". I'm processing your request and will provide a detailed response shortly.</p>
                            </div>
                        </div>
                    `;
                    chatContainer.appendChild(botResponse);
                    chatContainer.scrollTop = chatContainer.scrollHeight;
                }, 1000);
            }
        });
    </script>
</body>
</html>
