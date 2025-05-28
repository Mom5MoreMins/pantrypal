# app.py
import streamlit as st

# 1) Must be the very first Streamlit call
st.set_page_config(
    page_title="PantryPal 🥗",
    page_icon="🥗",
    layout="wide",
)

# 2) Import everything
from storage import init_db                   # makes sure our tables exist
from Login import show_login                  # signup/login page
from Account import show_account              # account & logout page
from Home import show_home                    # your home page
from CalorieCalculator import show_calculator # 🍏 calorie + allergy profile
from MealPlan import show_mealplan            # 🥘 meal plan
from IngredientSubstitution import show_substitute  # 🔄 ingredient subs

# 3) Initialize the database
init_db()

# 4) Set up auth flags in session_state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = ""

# 5) Build the sidebar
st.sidebar.title("PantryPal 🥗")

# 6) If not logged in, only show the Login page
if not st.session_state.logged_in:
    choice = st.sidebar.radio("Go to", ["🔑 Login"])
    if choice == "🔑 Login":
        show_login()

# 7) Once logged in, show all the pages
else:
    choice = st.sidebar.radio(
        "Go to",
        [
            "🏠 Home",
            "🍏 Calorie Calculator",
            "🥘 Meal Plan",
            "🔄 Ingredient Substitute",
            "⚙️ Account",
        ],
    )

    if choice == "🏠 Home":
        show_home()
    elif choice == "🍏 Calorie Calculator":
        show_calculator()
    elif choice == "🥘 Meal Plan":
        show_mealplan(st.session_state.user)
    elif choice == "🔄 Ingredient Substitute":
        show_substitute()
    else:  # ⚙️ Account
        show_account()
