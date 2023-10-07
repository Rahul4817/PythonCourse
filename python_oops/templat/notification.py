import time
from plyer import notification
import random

messages=["take some water",
          "How can I assist you?",
          "Hello sir How are you?",
          "Here your all task is completed",
          "once upon a time "

]

def Notification(title,message):

    notification.notify(
        title="Please drink water ",
        message=message,
        app_name="my app",
        timeout=30
    )

while True:
    title = "task"
    message = "drink a water"
    message=random.choice(messages)
    Notification(title,message)
    time.sleep(10)

