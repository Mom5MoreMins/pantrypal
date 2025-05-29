# MealPlan.py
import streamlit as st
import requests

from storage import save_meal_plan, load_meal_plans

def generate_meal_plan(calories: float, exclude: list[str] = None):
    """
    Calls Spoonacular's mealplanner/generate endpoint for one day.
    """
    params = {
        "timeFrame": "day",
        "targetCalories": int(calories),
        "apiKey": st.secrets["SPOONACULAR_KEY"],
    }
    if exclude:
        # Spoonacular expects comma-separated ingredients to skip
        params["exclude"] = ",".join(exclude).lower()
    resp = requests.get(
        "https://api.spoonacular.com/mealplanner/generate",
        params=params,
        timeout=10
    )
    resp.raise_for_status()
    return resp.json()

def show_mealplan(username: str):
    st.header("🥘 Meal Plan")

    # Load BMR from profile
    from storage import load_profile
    bmr, allergies = load_profile(username)

    if bmr is None:
        st.warning("Please calculate and save your BMR/allergies first.")
        return

    st.write(f"Target calories: **{int(bmr)} kcal/day**")
    st.write(f"Excluding: {', '.join(allergies) or 'None'}")
    st.markdown("---")

    if st.button("Generate Meal Plan"):
        with st.spinner("Fetching your custom meal plan…"):
            data = generate_meal_plan(bmr, exclude=allergies)

        # Show each meal
        for meal in data.get("meals", []):
            st.subheader(meal["title"])
            st.write(f"- Ready in {meal['readyInMinutes']} minutes")
            st.write(f"- Servings: {meal['servings']}")
            st.markdown(f"[View Recipe ➡️]({meal['sourceUrl']})")

        nutrients = data.get("nutrients", {})
        st.markdown("---")
        st.subheader("Daily Nutrition Summary")
        st.write(f"- **Calories:** {nutrients.get('calories',0)} kcal")
        st.write(f"- **Protein:** {nutrients.get('protein',0)} g")
        st.write(f"- **Fat:** {nutrients.get('fat',0)} g")
        st.write(f"- **Carbs:** {nutrients.get('carbohydrates',0)} g")

        # Save the plan text if you like (optional)
        save_meal_plan(username, str(data))

    # Show recent saved plans from your DB
    st.markdown("---")
    st.subheader("📜 Your Recent Saved Plans")
    for plan_text, ts in load_meal_plans(username):
        st.markdown(f"**{ts}**")
        st.text(plan_text[:200] + "...")  # preview only
