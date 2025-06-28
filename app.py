import streamlit as st
from PIL import Image
import time
import json
from streamlit_lottie import st_lottie

# --- Page Configuration ---
st.set_page_config(page_title="AI Diet Recommender", layout="wide", page_icon="🥗")

# --- Load Lottie Animation ---
def load_lottie(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_diet = load_lottie("assets/diet_animation.json")

# --- Custom CSS ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #f5f7fa, #c3cfe2);
    }
    h1, h2, h3 {
        font-family: 'Trebuchet MS', sans-serif;
        color: #2c3e50;
    }
    .stButton > button {
        background-color: #27ae60;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 0.6em 1.2em;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #2ecc71;
        color: black;
    }
    img:hover {
        transform: scale(1.03);
        transition: 0.3s ease-in-out;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
col1, col2 = st.columns([3, 2])
with col1:
    st.image("assets/banner.jpg", use_column_width=True)
with col2:
    st_lottie(lottie_diet, height=250, key="diet_lottie")

st.markdown("## 🥦 AI-Based Diet Recommender")
st.markdown("#### Personalized meal suggestions powered by artificial intelligence.")

# --- Sidebar Inputs ---
with st.sidebar:
    st.header("💬 Enter Your Info")
    age = st.slider("🎂 Age", 10, 80, 25)
    gender = st.selectbox("👤 Gender", ["Male", "Female", "Other"])
    goal = st.selectbox("🎯 Goal", ["Lose Weight", "Gain Muscle", "Maintain Health"])
    activity = st.selectbox("🔥 Activity Level", ["Sedentary", "Moderately Active", "Active"])
    st.markdown("---")
    if st.button("✨ Recommend Diet"):
        st.session_state.recommend = True

# --- Recommendation Section ---
if st.session_state.get("recommend", False):
    st.success("✅ Generating your AI meal plan...")
    time.sleep(2)

    st.markdown("### 🍽️ Your Personalized AI Meal Plan")
    st.markdown("These meals are curated for you:")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("assets/Salad.jpg", caption="🥗 Fresh Salad", use_column_width=True)
        st.markdown("*Detox with greens, avocado, radish, and feta.*")

    with col2:
        st.image("assets/Soup.jpg", caption="🍲 Tomato Soup & Salad", use_column_width=True)
        st.markdown("*Perfect light dinner with vitamins and fiber.*")

    with col3:
        st.image("assets/Omelette.jpg", caption="🍳 Breakfast Omelette", use_column_width=True)
        st.markdown("*High protein meal with veggies and tomato.*")

    st.balloons()

# --- Footer ---
st.markdown("---")
st.markdown("<center>© 2025 | Built with 💚 by AI Diet Team</center>", unsafe_allow_html=True)
