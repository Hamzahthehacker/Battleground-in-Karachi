import streamlit as st
import random
import time
from streamlit_autorefresh import st_autorefresh

# 1. Page Config - Responsive settings
st.set_page_config(page_title="Nokia 3310 Karachi", layout="centered", initial_sidebar_state="collapsed")

# 2. Advanced CSS for Fixed Screen & Nokia Body
st.markdown("""
    <style>
    /* Hide Streamlit default elements */
    #MainMenu, footer, header {visibility: hidden;}
    .main { background-color: #111; overflow: hidden; height: 100vh; }
    
    /* Phone Frame - Optimized for iPhone 6s Aspect Ratio */
    .nokia-body {
        background-color: #3b5998;
        border-radius: 30px;
        border: 5px solid #222;
        width: 300px;
        height: 520px;
        margin: auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-top: 20px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.8);
    }
    
    /* Green Game Screen */
    .screen-area {
        background-color: #97ba1e;
        width: 260px;
        height: 180px;
        border: 8px solid #111;
        font-family: 'Courier New', monospace;
        color: #222;
        padding: 5px;
        font-weight: bold;
        font-size: 16px;
        line-height: 1;
        overflow: hidden;
    }
    
    /* Keypad Area */
    .keypad {
        margin-top: 20px;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    
    /* Invisible but clickable buttons for joystick */
    .stButton>button {
        background-color: #444 !important;
        color: white !important;
        border-radius: 50% !important;
        width: 45px !important;
        height: 45px !important;
        padding: 0px !important;
        font-size: 18px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Game Loop (Faster for Action)
st_autorefresh(interval=350, key="nokia_engine")

# 4. State Management
if 'snake' not in st.session_state:
    st.session_state.snake = [(5, 5), (5, 4)]
    st.session_state.dir = "RIGHT"
    st.session_state.food = (3, 3)
    st.session_state.score = 0
    st.session_state.over = False

# 5. Logic
if not st.session_state.over:
    y, x = st.session_state.snake[0]
    if st.session_state.dir == "UP": y -= 1
    elif st.session_state.dir == "DOWN": y += 1
    elif st.session_state.dir == "LEFT": x -= 1
    elif st.session_state.dir == "RIGHT": x += 1
    
    new_head = (y, x)
    if x<0 or x>=16 or y<0 or y>=10 or new_head in st.session_state.snake:
        st.session_state.over = True
    else:
        st.session_state.snake.insert(0, new_head)
        if new_head == st.session_state.food:
            st.session_state.score += 10
            st.session_state.food = (random.randint(0, 9), random.randint(0, 15))
        else:
            st.session_state.snake.pop()

# --- 6. RENDER NOKIA ---
st.markdown('<div class="nokia-body">', unsafe_allow_html=True)

# Speaker & Logo
st.markdown("<div style='color:#ccc; font-size:10px;'>NOKIA</div>", unsafe_allow_html=True)

# The Screen
st.markdown('<div class="screen-area">', unsafe_allow_html=True)
board = [["·" for _ in range(16)] for _ in range(10)]
fy, fx = st.session_state.food
board[fy][fx] = "■"
for sy, sx in st.session_state.snake:
    board[sy][sx] = "▓"

display_str = "\n".join(["".join(row) for row in board])
st.text(display_str)
st.write(f"SCORE: {st.session_state.score}")
st.markdown('</div>', unsafe_allow_html=True)

# Virtual Keypad
st.write("")
_, c2, _ = st.columns([1,1,1])
with c2: st.button("▲", on_click=lambda: setattr(st.session_state, 'dir', 'UP'))

c1, c2, c3 = st.columns([1,1,1])
with c1: st.button("◀", on_click=lambda: setattr(st.session_state, 'dir', 'LEFT'))
with c2: st.write("🎮")
with c3: st.button("▶", on_click=lambda: setattr(st.session_state, 'dir', 'RIGHT'))

_, c2, _ = st.columns([1,1,1])
with c2: st.button("▼", on_click=lambda: setattr(st.session_state, 'dir', 'DOWN'))

st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.over:
    st.error("GAME OVER!")
    if st.button("RETRY"):
        st.session_state.snake = [(5, 5), (5, 4)]
        st.session_state.over = False
        st.session_state.score = 0
        st.rerun()

st.caption("Sultan Muhammad Hamza Hameed Edition")
