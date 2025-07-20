import schedule
import time

def schedule_task(time_str, func, *args, **kwargs):
    schedule.every().day.at(time_str).do(func, *args, **kwargs)

def run_pending():
    while True:
        schedule.run_pending()
        time.sleep(1)