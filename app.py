import streamlit as st
from PIL import Image

# --- Page Setup ---
st.set_page_config(page_title="AI Diet Recommender", layout="wide", page_icon="🥗")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #1f1f1f, #2d2d2d);
        color: white;
    }
    h1, h2, h3 {
        font-family: 'Trebuchet MS', sans-serif;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #27ae60;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 8px 20px;
    }
    .stButton>button:hover {
        background-color: #2ecc71;
        color: black;
    }
    img:hover {
        transform: scale(1.02);
        transition: 0.3s ease-in-out;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar User Input ---
with st.sidebar:
    st.header("💬 Enter Your Info")
    age = st.slider("🎂 Age", 10, 80, 25)
    name = st.text_input("🧑 Your Name")
    gender = st.selectbox("👤 Gender", ["Male", "Female", "Other"])
    goal = st.selectbox("🎯 Goal", ["Lose Weight", "Gain Muscle", "Maintain Health"])
    activity = st.selectbox("🔥 Activity Level", ["Sedentary", "Moderately Active", "Active"])
    st.markdown("---")
    if st.button("✨ Recommend Diet"):
        st.session_state.recommend = True
        st.session_state.name = name

# --- Full-Width Banner ---
st.image("assets/banner.jpg", use_container_width=True)

# --- Personalized Welcome Message ---
if "name" in st.session_state and st.session_state.name.strip():
    st.markdown(f"### 👋 Welcome, **{st.session_state.name}**!")
else:
    st.markdown("### 👋 Welcome!")

# --- Diet Recommendation Section ---
if st.session_state.get("recommend", False):
    st.success("✅ Generating your personalized meal plan...")

    st.markdown("### 🍽️ Your Recommended Meals:")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("assets/Salad.jpg", caption="🥗 Fresh Avocado Salad", use_container_width=True)
        st.markdown("Rich in fiber, antioxidants, and healthy fats.")

    with col2:
        st.image("assets/Soup.jpg", caption="🍲 Tomato Veggie Soup", use_container_width=True)
        st.markdown("Perfect light meal packed with nutrients.")

    with col3:
        st.image("assets/Omelette.jpg", caption="🍳 Spinach Cheese Omelette", use_container_width=True)
        st.markdown("High protein breakfast to fuel your day.")

# --- Footer ---
st.markdown("---")
st.markdown("<center>© 2025 | Built with 💚 by AI Diet Team</center>", unsafe_allow_html=True)
