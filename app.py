import streamlit as st
from Home import show_home
from CalorieCalculator import show_calculator
from MealPlan import show_mealplan
from IngredientSubstitution import show_substitute

st.set_page_config(
    page_title="PantryPal 🥗",
    page_icon="🥗",
    layout="wide",
)

st.sidebar.title("PantryPal")
page = st.sidebar.radio(
    "Go to",
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