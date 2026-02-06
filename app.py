import streamlit as st
import random
import time

# Page Configuration
st.set_page_config(page_title="Battleground in Karachi", page_icon="⚔️", layout="wide")

# Custom CSS for Karachi Battle Vibe
st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #001f3f, #000000); color: #00e6e6; }
    .stButton>button { 
        background-color: #008080; color: white; font-weight: bold; 
        border-radius: 10px; border: 2px solid #00ffff; height: 3em;
    }
    .unlocked-status { color: #39ff14; font-size: 20px; font-weight: bold; text-align: center; border: 1px solid #39ff14; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar - iPhone 120 FPS Unlocker
with st.sidebar:
    st.header("⚙️ System Optimization")
    iphone_model = st.selectbox("Select iPhone Model", ["iPhone 13 Pro", "iPhone 14 Pro", "iPhone 15 Pro Max", "iPhone 16 Pro Max"])
    st.write(f"Device Detected: **{iphone_model}**")
    
    unlock_btn = st.button("🔓 Unlock 120 FPS & Ultra Graphics")
    
    if unlock_btn:
        with st.spinner("Modifying System Config..."):
            time.sleep(2)
            st.markdown("<div class='unlocked-status'>120 FPS ULTRA EXTREME UNLOCKED</div>", unsafe_allow_html=True)

st.title("⚔️ Battleground in Karachi (v3.7)")
st.subheader("Sultan Muhammad Hamza Hameed Presents: Karachi Siege")

# Game State
if 'kills' not in st.session_state:
    st.session_state.kills = 0
if 'health' not in st.session_state:
    st.session_state.health = 100

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.write(f"### 📍 Current Location: **Karachi (Clifton/Saddar Area)**")
    st.write(f"### 🩸 Health: {st.session_state.health}% | 🎯 Kills: {st.session_state.kills}")
    
    st.write("---")
    
    # Action Scenario
    scenario = random.choice([
        "Saddar ki tang galiyon mein enemy nazar aaya!",
        "Clifton beach par airdrop gira hai, dushman wahan hai!",
        "Mazaar-e-Quaid ke paas sniper camper baitha hai!"
    ])
    st.info(f"🚀 **Action:** {scenario}")
    
    if st.button("🔥 ATTACK (120 FPS Spray)"):
        action = random.random()
        if action > 0.4:
            st.success("Sultan Hamza ka perfect shot! Enemy Down! 🎯")
            st.session_state.kills += 1
            st.balloons()
        else:
            st.error("Dushman ne cover le liya! Aapko goli lagi!")
            st.session_state.health -= 25

with col2:
    st.write("### 🎒 Inventory")
    st.info("Weapon: AKM + M416 (Max Level)")
    st.info("Graphics: Ultra Extreme (120 FPS)")
    
    if st.session_state.health <= 0:
        st.error("💥 SQUAD ELIMINATED! Karachi ki galiyon mein dushman jeet gaya.")
        if st.button("Respawn in Karachi"):
            st.session_state.health = 100
            st.session_state.kills = 0
            st.rerun()

st.write("---")
st.write("System: **iPhone High Performance Mode Enabled** | Developer: **Sultan Muhammad Hamza Hameed**")