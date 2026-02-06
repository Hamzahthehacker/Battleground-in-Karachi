import streamlit as st
import random
import time
from streamlit_autorefresh import st_autorefresh

# Page Config
st.set_page_config(page_title="Nokia 3310 Karachi", layout="centered")

# Custom CSS for the "Phone inside Phone" Look
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; }
    /* Nokia Body Frame */
    .nokia-frame {
        background-color: #3b5998;
        border-radius: 40px 40px 100px 100px;
        padding: 30px 20px;
        border: 8px solid #222;
        width: 320px;
        margin: auto;
        box-shadow: 0px 20px 50px rgba(0,0,0,0.5);
    }
    /* The Green Pixel Screen */
    .nokia-screen {
        background-color: #97ba1e;
        border: 10px solid #111;
        height: 250px;
        font-family: 'Courier New', monospace;
        color: #222;
        padding: 5px;
        overflow: hidden;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #444; color: white; border-radius: 50%;
        height: 50px; width: 50px; font-size: 12px; margin: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Auto-refresh loop (Speed control)
st_autorefresh(interval=400, key="nokia_loop")

# Game Logic & State
if 'snake' not in st.session_state:
    st.session_state.snake = [(5, 5), (5, 4)]
    st.session_state.dir = "RIGHT"
    st.session_state.food = (3, 3)
    st.session_state.score = 0
    st.session_state.over = False

# Movement Logic
if not st.session_state.over:
    y, x = st.session_state.snake[0]
    if st.session_state.dir == "UP": y -= 1
    elif st.session_state.dir == "DOWN": y += 1
    elif st.session_state.dir == "LEFT": x -= 1
    elif st.session_state.dir == "RIGHT": x += 1
    
    new_head = (y, x)
    # Collision Check
    if x<0 or x>=15 or y<0 or y>=12 or new_head in st.session_state.snake:
        st.session_state.over = True
    else:
        st.session_state.snake.insert(0, new_head)
        if new_head == st.session_state.food:
            st.session_state.score += 10
            st.session_state.food = (random.randint(0, 11), random.randint(0, 14))
        else:
            st.session_state.snake.pop()

# --- RENDER NOKIA ---
st.markdown('<div class="nokia-frame">', unsafe_allow_html=True)
st.markdown('<div class="nokia-screen">', unsafe_allow_html=True)

# Draw Board
board = [["·" for _ in range(15)] for _ in range(12)]
fy, fx = st.session_state.food
board[fy][fx] = "■"
for sy, sx in st.session_state.snake:
    board[sy][sx] = "▓"

for row in board:
    st.write("".join(row))

st.markdown(f"SCORE: {st.session_state.score}</div>", unsafe_allow_html=True)

# Nokia Keypad (Controls)
st.write("")
c1, c2, c3 = st.columns(3)
with c2: st.button("▲", on_click=lambda: setattr(st.session_state, 'dir', 'UP'))
c1, c2, c3 = st.columns(3)
with c1: st.button("◀", on_click=lambda: setattr(st.session_state, 'dir', 'LEFT'))
with c2: st.write("🎮")
with c3: st.button("▶", on_click=lambda: setattr(st.session_state, 'dir', 'RIGHT'))
c1, c2, c3 = st.columns(3)
with c2: st.button("▼", on_click=lambda: setattr(st.session_state, 'dir', 'DOWN'))

st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.over:
    st.warning("GAME OVER!")
    if st.button("RETRY"):
        st.session_state.snake = [(5, 5), (5, 4)]
        st.session_state.over = False
        st.session_state.score = 0
        st.rerun()

st.caption("Developed by Sultan Muhammad Hamza Hameed")
