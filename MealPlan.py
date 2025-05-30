# MealPlan.py
import streamlit as st
import requests
import json

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
        params["exclude"] = ",".join(exclude).lower()

    resp = requests.get(
        "https://api.spoonacular.com/mealplanner/generate",
        params=params,
        timeout=10
    )
    resp.raise_for_status()
    return resp.json()

def get_recipe_info(recipe_id: int):
    """
    Fetches detailed recipe info so we can grab spoonacularSourceUrl.
    """
    resp = requests.get(
        f"https://api.spoonacular.com/recipes/{recipe_id}/information",
        params={"apiKey": st.secrets["SPOONACULAR_KEY"]},
        timeout=10
    )
    resp.raise_for_status()
    return resp.json()

def show_mealplan(username: str):
    st.header("🥘 Meal Plan")

    # Load BMR and allergies from profile
    from storage import load_profile
    bmr, allergies = load_profile(username)

    if bmr is None:
        st.warning("Please calculate and save your BMR/allergies first.")
        return

    st.write(f"**Target calories**: {int(bmr)} kcal/day")
    st.write(f"**Excluding**: {', '.join(allergies) or 'None'}")
    st.markdown("---")

    if st.button("Generate Meal Plan"):
        with st.spinner("Fetching your custom meal plan…"):
            data = generate_meal_plan(bmr, exclude=allergies)

        # Display the generated plan
        for meal in data.get("meals", []):
            st.subheader(meal["title"])
            st.write(f"- Ready in {meal['readyInMinutes']} minutes")
            st.write(f"- Servings: {meal['servings']}")

            # Fetch recipe info to get Spoonacular’s own URL
            info = get_recipe_info(meal["id"])
            link = info.get("spoonacularSourceUrl") or meal.get("sourceUrl")
            st.markdown(f"[View Recipe on Spoonacular ➡️]({link})")

        nutrients = data.get("nutrients", {})
        st.markdown("---")
        st.subheader("Daily Nutrition Summary")
        st.write(f"- **Calories:** {nutrients.get('calories',0)} kcal")
        st.write(f"- **Protein:** {nutrients.get('protein',0)} g")
        st.write(f"- **Fat:** {nutrients.get('fat',0)} g")
        st.write(f"- **Carbs:** {nutrients.get('carbohydrates',0)} g")

        # Persist the full JSON for later review
        save_meal_plan(username, json.dumps(data))

    # Show recent saved plans with full details
    st.markdown("---")
    st.subheader("📜 Your Recent Saved Plans")
    plans = load_meal_plans(username)
    if not plans:
        st.write("No saved plans yet.")
        return

    for plan_text, ts in plans:
        st.markdown(f"### Saved on {ts}")
        try:
            saved = json.loads(plan_text)
        except json.JSONDecodeError:
            st.text("[Error parsing saved plan data]")
            continue

        for meal in saved.get("meals", []):
            st.subheader(meal.get("title", "Untitled"))
            st.write(f"• Ready in {meal.get('readyInMinutes', '?')} minutes")
            st.write(f"• Servings: {meal.get('servings', '?')}")

            # Same trick on saved plans
            info = get_recipe_info(meal["id"])
            link = info.get("spoonacularSourceUrl") or meal.get("sourceUrl")
            st.markdown(f"[View Recipe on Spoonacular ➡️]({link})")

        nutrients = saved.get("nutrients", {})
        st.markdown("**Nutrition Summary**")
        st.write(f"- Calories: {nutrients.get('calories',0)} kcal")
        st.write(f"- Protein: {nutrients.get('protein',0)} g")
        st.write(f"- Fat: {nutrients.get('fat',0)} g")
        st.write(f"- Carbs: {nutrients.get('carbohydrates',0)} g")
        st.markdown("---")
