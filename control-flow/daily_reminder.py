Task = input("Enter your task: ")
Time_Bound = input("Is it time-bound? (yes/no) ")
Priority = input("Priority (high/medium/low): ")


reminder = ""
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a High priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a Medium priority task." 
    case "low":
        reminder = f"Reminder: '{task}' is a Low priority task."
    case _:
        reminder = f"Reminder: '{task}' has an unspecified priority."

if time_bound.lower() == "yes":
    reminder += " That requires immediate attention today!."

print(reminder)