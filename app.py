# app.py
import streamlit as st

# 1) Must be the very first Streamlit call in the script
st.set_page_config(
    page_title="PantryPal 🥗",
    page_icon="🥗",
    layout="wide",
)

# 2) Import your page‐rendering functions
from storage import init_db            # ensures our users table exists
from Login import show_login           # handles sign-up & login
from Account import show_account       # shows account info & logout
from Home import show_home
from CalorieCalculator import show_calculator
from MealPlan import show_mealplan
from IngredientSubstitution import show_substitute

# 3) Initialize database once
init_db()

# 4) Session-state defaults for auth
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = ""

# 5) Build the sidebar
st.sidebar.title("PantryPal 🥗")

# 6) If not logged in, only allow the Login page
if not st.session_state.logged_in:
    page = st.sidebar.radio("Go to", ["🔑 Login"])
    if page == "🔑 Login":
        show_login()

# 7) Once logged in, expose main pages + Account
else:
    page = st.sidebar.radio(
        "Go to",
        [
            "🏠 Home",
            "🍏 Calorie Calculator",
            "🥘 Meal Plan",
            "🔄 Ingredient Substitute",
            "⚙️ Account",
        ],
    )

    if page == "🏠 Home":
        show_home()
    elif page == "🍏 Calorie Calculator":
        show_calculator()
    elif page == "🥘 Meal Plan":
        show_mealplan(st.session_state.user)
    elif page == "🔄 Ingredient Substitute":
        show_substitute()
    else:  # ⚙️ Account
        show_account()