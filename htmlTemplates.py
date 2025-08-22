# htmlTemplates.py

css = """
<style>
:root{
  /* Balanced (not too deep/light) RGB palette */
  --bg1: rgb(255, 120, 120);   /* soft red */
  --bg2: rgb(120, 190, 255);   /* sky blue */
  --bg3: rgb(120, 255, 190);   /* mint green */

  --sb1: rgb(255, 210, 140);   /* warm apricot */
  --sb2: rgb(140, 210, 255);   /* light azure */
  --sb3: rgb(220, 150, 255);   /* lilac */

  --text: #0b1020;
  --text-contrast: #0b1020;
  --text-on-dark: #f3f6ff;

  --card-bg: rgba(255,255,255,0.12);
  --card-border: rgba(255,255,255,0.28);
  --shadow: 0 6px 30px rgba(0,0,0,0.15);

  --radius: 16px;
}

@media (prefers-color-scheme: dark){
  :root{
    --text: #e8ecf7;
    --text-contrast: #ffffff;
    --card-bg: rgba(0,0,0,0.20);
    --card-border: rgba(255,255,255,0.22);
  }
}

/* Full-bleed animated RGB background */
html, body{height:100%;}
body{
  margin:0;
  color: var(--text);
  background: linear-gradient(120deg, var(--bg1), var(--bg2), var(--bg3));
  background-size: 300% 300%;
  animation: bgShift 18s ease-in-out infinite;
  font-family: system-ui, -apple-system, Segoe UI, Roboto, Inter, "Noto Sans", Arial, sans-serif;
}
@keyframes bgShift{
  0%{background-position: 0% 50%}
  50%{background-position: 100% 50%}
  100%{background-position: 0% 50%}
}

/* Glassy containers for readability */
.container, main, .glass{
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}

/* Sidebar with a separate RGB flow */
.sidebar{
  position: fixed; inset: 0 auto 0 0;
  width: 280px;
  padding: 20px 18px;
  color: var(--text);
  background: linear-gradient(180deg, var(--sb1), var(--sb2), var(--sb3));
  background-size: 300% 300%;
  animation: sbShift 24s ease-in-out infinite;
  box-shadow: 2px 0 20px rgba(0,0,0,0.12);
  overflow-y: auto;
}
@keyframes sbShift{
  0%{background-position: 50% 0%}
  50%{background-position: 50% 100%}
  100%{background-position: 50% 0%}
}
.sidebar .title{
  font-weight: 800; letter-spacing: .4px;
  color: var(--text-contrast);
  text-shadow: 0 1px 1px rgba(0,0,0,.18);
  margin: 4px 0 14px 2px;
}
.sidebar .nav a{
  display:block; padding:10px 12px; margin:6px 0;
  border-radius: 12px;
  background: rgba(255,255,255,0.55);
  color: #0b1020; text-decoration:none; font-weight:600;
  border: 1px solid rgba(0,0,0,0.08);
}

/* Main content */
.content{
  margin-left: 300px;
  padding: 24px;
}
h1,h2,h3{
  color: var(--text-contrast);
  text-shadow: 0 1px 2px rgba(0,0,0,.15);
  margin: 0 0 10px 0;
}

/* Chat area */
.chat{ display:grid; gap:14px; }
.msg{
  max-width: 960px;
  padding: 14px 16px;
  border-radius: 14px;
  line-height: 1.6;
  word-wrap: break-word;
}
.msg.user{
  background: rgba(255,255,255,0.85);
  color:#0b1020;
  border: 1px solid rgba(0,0,0,0.08);
}
.msg.bot{
  background: rgba(14,24,44,0.78);
  color: var(--text-on-dark);
  border: 1px solid rgba(255,255,255,0.18);
}

/* Inputs / buttons */
button, .btn{
  padding: 10px 14px; border-radius: 12px; border: 0;
  background: rgba(255,255,255,0.9); color:#0b1020;
  box-shadow: 0 4px 14px rgba(0,0,0,.12);
  cursor:pointer; transition: transform .08s ease, filter .2s ease;
}
button:hover{ transform: translateY(-1px); filter: brightness(1.03); }
input, textarea{
  width: 100%;
  padding: 12px 14px;
  border-radius: 12px;
  border: 1px solid rgba(0,0,0,.15);
  background: rgba(255,255,255,.95);
  color: #0b1020;
}

/* Selections & accessibility */
::selection{ background: rgba(0,0,0,.25); color:#fff; }
@media (prefers-reduced-motion: reduce){
  body, .sidebar{ animation: none !important; }
}
</style>
"""

# A simple wrapper layout if you want to render a sidebar + content quickly.
# Use layout_open before your page body and layout_close after.
layout_open = """
<div class="sidebar">
  <div class="title">DocuBot</div>
  <div class="nav">
    <a href="#">Home</a>
    <a href="#">Documents</a>
    <a href="#">Settings</a>
  </div>
</div>
<div class="content">
"""

layout_close = """
</div> <!-- /.content -->
"""

# Chat bubble templates. Replace {{MSG}} at runtime.
bot_template = """
<div class="chat">
  <div class="msg bot">
    {{MSG}}
  </div>
</div>
"""

user_template = """
<div class="chat">
  <div class="msg user">
    {{MSG}}
  </div>
</div>
"""
