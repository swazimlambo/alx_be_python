task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
reminder = f"'{task}' is a {priority} priority task that requires immediate attention today!"
note = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."

match priority: 
    case "high":
        if time_bound == "yes":
            print("Reminder: ", reminder)
        else:
            print("Note: ", note)
    case "medium":
        if time_bound == "yes":
            print("Reminder: ", reminder)
        else:
            print("Note: ", note)
    case "low":
        if time_bound == "yes":
            print("Reminder: ", reminder)
        else:
            print("Note: ", note)

        