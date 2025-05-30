# MealPlan.py
import streamlit as st
import requests
import json
from storage import save_meal_plan, load_meal_plans, load_profile


def generate_meal_plan(username: str, calories: float):
    """
    Calls Spoonacular's mealplanner/generate endpoint for one day.
    Automatically excludes the user's known allergies from the database.
    """
    _, allergies = load_profile(username)

    params = {
        "timeFrame": "day",
        "targetCalories": int(calories),
        "apiKey": st.secrets["SPOONACULAR_KEY"],
    }
    if allergies:
        params["exclude"] = ",".join(a.lower() for a in allergies)

    resp = requests.get(
        "https://api.spoonacular.com/mealplanner/generate",
        params=params,
        timeout=10
    )
    resp.raise_for_status()
    return resp.json()


def show_mealplan(username: str):
    st.header("🥘 Meal Plan")

    # Load BMR to ensure profile exists
    bmr, _ = load_profile(username)
    if bmr is None:
        st.warning("Please calculate and save your BMR and allergies first.")
        return

    st.write(f"**Target calories**: {int(bmr)} kcal/day")
    st.markdown("---")

    if st.button("Generate Meal Plan"):
        with st.spinner("Fetching your custom meal plan…"):
            try:
                plan = generate_meal_plan(username, bmr)
            except requests.exceptions.HTTPError as err:
                code = err.response.status_code
                if code in (402, 429):
                    st.error("⚠️ API limit reached—showing your last saved plan.")
                    plan = None
                else:
                    st.error(f"API error ({code}): {err}")
                    return
            except requests.exceptions.ReadTimeout:
                st.error("⚠️ Request timed out—showing your last saved plan.")
                plan = None

        # Display new plan
        if plan:
            for meal in plan.get("meals", []):
                title = meal.get("title", "Untitled")
                st.subheader(title)
                st.write(f"• Ready in {meal.get('readyInMinutes', '?')} minutes")
                st.write(f"• Servings: {meal.get('servings', '?')}")

                slug = title.lower().replace(" ", "-")
                url = f"https://spoonacular.com/recipes/{slug}-{meal.get('id')}"
                st.markdown(f"[View Recipe on Spoonacular ➡️]({url})")

            nutrients = plan.get("nutrients", {})
            st.markdown("---")
            st.subheader("Daily Nutrition Summary")
            st.write(f"- Calories: {nutrients.get('calories',0):.0f} kcal")
            st.write(f"- Protein: {nutrients.get('protein',0):.1f} g")
            st.write(f"- Fat: {nutrients.get('fat',0):.1f} g")
            st.write(f"- Carbs: {nutrients.get('carbohydrates',0):.1f} g")

            save_meal_plan(username, json.dumps(plan))

        # Fallback to last saved plan
        else:
            st.markdown("---")
            st.subheader("📜 Last Saved Plan")
            recent = load_meal_plans(username, limit=1)
            if not recent:
                st.write("No prior plans to display.")
                return
            plan_text, ts = recent[0]
            saved = json.loads(plan_text)
            for meal in saved.get("meals", []):
                title = meal.get("title", "Untitled")
                st.subheader(title)
                st.write(f"• Ready in {meal.get('readyInMinutes', '?')} minutes")
                st.write(f"• Servings: {meal.get('servings', '?')}")
                slug = title.lower().replace(" ", "-")
                url = f"https://spoonacular.com/recipes/{slug}-{meal.get('id')}"
                st.markdown(f"[View Recipe on Spoonacular ➡️]({url})")
            nutrients = saved.get("nutrients", {})
            st.markdown("**Nutrition Summary**")
            st.write(f"- Calories: {nutrients.get('calories',0):.0f} kcal")
            st.write(f"- Protein: {nutrients.get('protein',0):.1f} g")
            st.write(f"- Fat: {nutrients.get('fat',0):.1f} g")
            st.write(f"- Carbs: {nutrients.get('carbohydrates',0):.1f} g")

    # Display recent history
    st.markdown("---")
    st.subheader("📜 Your Recent Saved Plans")
    history = load_meal_plans(username)
    if not history:
        st.write("No saved plans yet.")
        return
    for _, ts in history:
        st.write(f"- {ts}")
