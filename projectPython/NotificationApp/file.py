import time
import random
from plyer import notification


messages = [
    "Please take some water.",
    "Please take rest.",
    "Don't forget to take a break!",
    "Hello Sir,How am I assist you",
    "Here your task."
]

def desktop_notifier(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Notification App",
        timeout=10 # for message disappear
    )
num_notifications = 5
notifications_displayed = 0


# notification_count = 5
# for _ in range(notification_count): #End task with for loop


while notifications_displayed < num_notifications:# End task with comparison
    title = "Your Task"

    message = random.choice(messages)

    desktop_notifier(title, message)

    notifications_displayed+=1

    # Waiting  for some time
    time.sleep(30)

print("All task is Completed")


