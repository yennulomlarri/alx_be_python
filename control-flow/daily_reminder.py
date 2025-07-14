task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            print(f"Reminder: {reminder} that requires immediate attention today!")
        else:
            print(f"Reminder: {reminder}.")

    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            print(f"Reminder: {reminder} that requires immediate attention today!")
        else:
            print(f"Note: {reminder}. Try to complete it soon.")

    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            print(f"Reminder: {reminder} that requires immediate attention today!")
        else:
            print(f"Note: {reminder}. Consider completing it when you have free time.")

    case _:
        print("Invalid priority level entered. Please choose high, medium, or low.")