import streamlit as st

def show_mealplan():
    st.header("Meal Plan 🥘")
    bmr = st.session_state.get("bmr")
    if not bmr:
        st.warning("Calculate your BMR first on the Calorie Calculator page.")
        return

    # placeholder: call Gemini API or your logic here
    st.write(f"Generating a meal plan for ~{bmr} kcal/day…")
    # e.g., st.write(gemini.generate_meal_plan(calories=bmr))
