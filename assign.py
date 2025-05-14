#!/usr/bin/env python3

def get_user_input(prompt):
    """Prompt user and return a float. Raises ValueError on invalid input."""
    value_str = input(prompt).strip()
    if not value_str:
        raise ValueError("Input cannot be empty.")
    value = float(value_str)  # may raise ValueError
    if value < 0:
        raise ValueError("Input must be non-negative.")
    return value

def calculate_bmi(weight_kg, height_cm):
    """Calculate BMI from weight (kg) and height (cm)."""
    height_m = height_cm / 100
    if height_m == 0:
        raise ZeroDivisionError("Height cannot be zero.")
    return weight_kg / (height_m ** 2)

def suggest_plan(bmi):
    """Return a tuple (workout_minutes, diet_plan)."""
    if bmi < 18.5:
        return (30, "High-protein diet with healthy fats")
    elif bmi < 25:
        return (45, "Balanced diet: carbs, proteins, fats")
    elif bmi < 30:
        return (60, "Low-carb diet with moderate protein")
    else:
        return (75, "Calorie-deficit diet, focus on veggies")

def main():
    print("=== Workout Time Planner ===")
    try:
        w = get_user_input("Enter your weight (kg): ")
        h = get_user_input("Enter your height (cm): ")
        bmi = calculate_bmi(w, h)
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return
    except ZeroDivisionError as zde:
        print(f"Math error: {zde}")
        return

    workout_min, diet = suggest_plan(bmi)
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Suggested daily workout: {workout_min} minutes")
    print(f"Basic diet plan: {diet}")

if __name__ == "__main__":
    main()
