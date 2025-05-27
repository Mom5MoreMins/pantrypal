# Home.py
import streamlit as st
import time

def show_home():
    st.title("Welcome to PantryPal 🥗")
    st.write("""
    **PantryPal** helps you:
    - 🍏 **Calorie Calculator**: figure out your daily energy needs  
    - 🥘 **Meal Plan Generator**: get recipes to hit your calorie goal  
    - 🔄 **Ingredient Substitution**: swap out missing ingredients  
    """)

    st.markdown("---")
    placeholder = st.empty()

    swaps = [
        "🍞  ➡️  🥖",
        "🍎  ➡️  🍐",
        "🥕  ➡️  🌽",
        "🍗  ➡️  🥩",
        "🍓  ➡️  🍇",
    ]

    # infinite loop to keep cycling through frames
    while True:
        for frame in swaps:
            placeholder.markdown(f"<h1 style='text-align:center'>{frame}</h1>", unsafe_allow_html=True)
            time.sleep(0.6)
