# daily_reminder.py
# Reminder for a single priority task based on time sensitivity

# مطالبة المستخدم بإدخال المهمة
task = input("Enter your task: ")

# مطالبة المستخدم بإدخال أولوية المهمة
priority = input("Priority (high/medium/low): ").lower()

# مطالبة المستخدم إذا كانت المهمة محددة بوقت
time_bound = input("Is it time-bound? (yes/no): ").lower()

# استخدام match-case لمعالجة المهمة حسب الأولوية
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unspecified priority"

# تعديل الرسالة إذا كانت المهمة محددة بوقت
if time_bound == "yes" and priority in ["high", "medium"]:
    message += " that requires immediate attention today!"
elif time_bound == "no" and priority == "low":
    message += ". Consider completing it when you have free time."

# طباعة التذكير النهائي
print(message)
