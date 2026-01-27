import json
from datetime import datetime
import os

DATA_FILE = "calorie_data.json"

def load_data():
    """Loads calorie data from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    """Saves calorie data to a JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def get_today_str():
    """Returns today's date as a string (YYYY-MM-DD)."""
    return datetime.now().strftime("%Y-%m-%d")

def add_food_entry(data):
    """Prompts the user for food details and adds it to the data."""
    food_name = input("Enter food name: ")
    try:
        calories = int(input("Enter calories: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for calories.")
        return

    today = get_today_str()
    if today not in data:
        data[today] = []

    data[today].append({"name": food_name, "calories": calories})
    save_data(data)
    print(f"Added {calories} calories for {food_name}.")

def view_summary(data):
    """Displays today's total calorie intake."""
    today = get_today_str()
    if today in data and data[today]:
        total_calories = sum(item['calories'] for item in data[today])
        print(f"\n=== 📅 TODAY'S SUMMARY ({today}) ===")
        for item in data[today]:
            print(f"- {item['name']}: {item['calories']} calories")
        print(f"Total calories: {total_calories}")
        print("====================================")
    else:
        print("No entries for today yet!")

def main():
    """Main function to run the calorie tracker CLI application."""
    data = load_data()
    print("👋 Welcome to the Python Calorie Tracker!")

    while True:
        print("\nChoose an option:")
        print("1. Add a food entry")
        print("2. View today's summary")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_food_entry(data)
        elif choice == "2":
            view_summary(data)
        elif choice == "3":
            print("👋 Stay healthy! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()




    



















