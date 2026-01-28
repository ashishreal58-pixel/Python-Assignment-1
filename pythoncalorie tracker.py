# ---------------------------------------------
# Daily Calorie Tracker
# Written by Ashish Raj
# A simple program to track meals and calories
# ---------------------------------------------

# Task 1: Welcome Message
print("Welcome to Daily Calorie Tracker!")
print("Track what you eat, count your calories, and see if you’re staying within your daily goal!")

# Task 2: Input & Data Collection
meals = []
calories = []
num_meals = int(input("How many times you had taken meals for today starting from morning to night  ? "))
for i in range(num_meals):
    print(f"\n Enter details for meal that you had taken {i + 1}:")
    meal_name = str(input("Meal name: "))
    calorie_amount = float(input("Calories (in kcal): "))
    meals.append(meal_name)
    calories.append(calorie_amount)
# Task 3: Calorie Calculation
total_calories = sum(calories)
average_calories = total_calories / len(calories)
daily_limit = float(input("\nEnter your daily calorie limit: "))
 # Task 4: Exceed Limit Warning System
if total_calories > daily_limit:
    status_message = " You have exceeded your daily calorie limit Today : "
else:
    status_message = " You are within your daily calorie limit today  :"

# Task 5: Summary Output
# -------------------------------
print("\n----------- DAILY SUMMARY REPORT -----------\n")
print("Meal Name            Calories")
print("--------------------------------------------")

for i in range(len(meals)):
    print(f"{meals[i]}              {calories[i]}")

print("--------------------------------------------")
print(f"Total:               {total_calories}")
print(f"Average:             {average_calories}")
print(f"Status:              {status_message}")
print("--------------------------------------------")








    




















