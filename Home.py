# app.py
import streamlit as st
from Home import show_home
from CalorieCalculator import show_calculator
from MealPlan import show_mealplan
from IngredientSub import show_substitute

st.set_page_config(page_title="PantryPal", page_icon="🥗")

# build your own menu
page = st.sidebar.selectbox(
    "Navigate",
    [
        "🏠 Home",
        "🍏 Calorie Calculator",
        "🥘 Meal Plan",
        "🔄 Ingredient Substitute",
    ],
)

if page == "🏠 Home":
    show_home()
elif page == "🍏 Calorie Calculator":
    show_calculator()
elif page == "🥘 Meal Plan":
    show_mealplan()
elif page == "🔄 Ingredient Substitute":
    show_substitute()