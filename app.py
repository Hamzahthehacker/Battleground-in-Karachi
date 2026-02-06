import streamlit as st
import random
import time
from streamlit_autorefresh import st_autorefresh

# Page Config
st.set_page_config(page_title="Nokia Snake: Hamza Edition", page_icon="🐍")

# Custom CSS for Nokia 3310 Vibes
st.markdown("""
    <style>
    .main { background-color: #8fb31d; color: #000; font-family: 'Courier New', Courier, monospace; }
    .game-board { 
        border: 10px solid #222; 
        background-color: #97ba1e; 
        line-height: 1; 
        font-size: 20px;
        padding: 10px;
        display: inline-block;
    }
    .stButton>button { background-color: #222; color: #97ba1e; border: none; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# Game Constants
WIDTH, HEIGHT = 20, 10

# Initialize Game State
if 'snake' not in st.session_state:
    st.session_state.snake = [(5, 5), (5, 4), (5, 3)]
    st.session_state.direction = "RIGHT"
    st.session_state.food = (random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1))
    st.session_state.score = 0
    st.session_state.game_over = False

# Auto-refresh for movement (Simulating FPS)
st_autorefresh(interval=500, key="gameloop")

st.title("🐍 Nokia Snake: Karachi 3.7")
st.write(f"**Player:** Sultan Muhammad Hamza Hameed | **Score:** {st.session_state.score}")

# Controls
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("UP"): st.session_state.direction = "UP"
with col1:
    if st.button("LEFT"): st.session_state.direction = "LEFT"
with col3:
    if st.button("RIGHT"): st.session_state.direction = "RIGHT"
with col2:
    if st.button("DOWN"): st.session_state.direction = "DOWN"

# Game Logic
if not st.session_state.game_over:
    head_y, head_x = st.session_state.snake[0]
    
    if st.session_state.direction == "UP": head_y -= 1
    elif st.session_state.direction == "DOWN": head_y += 1
    elif st.session_state.direction == "LEFT": head_x -= 1
    elif st.session_state.direction == "RIGHT": head_x += 1
    
    new_head = (head_y, head_x)
    
    # Check Collisions
    if (new_head in st.session_state.snake or 
        head_x < 0 or head_x >= WIDTH or 
        head_y < 0 or head_y >= HEIGHT):
        st.session_state.game_over = True
    else:
        st.session_state.snake.insert(0, new_head)
        if new_head == st.session_state.food:
            st.session_state.score += 10
            st.session_state.food = (random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1))
        else:
            st.session_state.snake.pop()

# Render Board
board = [["░" for _ in range(WIDTH)] for _ in range(HEIGHT)]
fy, fx = st.session_state.food
board[fy][fx] = "🍎"

for i, (y, x) in enumerate(st.session_state.snake):
    board[y][x] = "█" if i == 0 else "▓"

game_str = "\n".join(["".join(row) for row in board])
st.markdown(f"<div class='game-board'><pre>{game_str}</pre></div>", unsafe_allow_html=True)

if st.session_state.game_over:
    st.error("💥 CRASHED! GAME OVER")
    if st.button("Restart Game"):
        st.session_state.snake = [(5, 5), (5, 4), (5, 3)]
        st.session_state.score = 0
        st.session_state.game_over = False
        st.rerun()
