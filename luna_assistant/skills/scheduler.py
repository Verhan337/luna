import schedule
import time

def schedule_task(time_str, func, *args, **kwargs):
    schedule.every().day.at(time_str).do(func, *args, **kwargs)

def run_pending():
    while True:
        schedule.run_pending()
        time.sleep(1)

def handle(intent, entities):
    if intent == "set_reminder":
        time_str = entities.get("time")
        message = entities.get("message")
        if time_str and message:
            def remind():
                print(f"Reminder: {message}")
            schedule_task(time_str, remind)
            return f"Reminder set for {time_str}: {message}"
        return "Time or message missing for reminder."
    return "Unknown scheduler command."