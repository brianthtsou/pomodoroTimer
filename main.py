import time
import datetime
# from timer_py import Timer

def pomodoro():
    total_time = 25 #* 60
    print((f"Time remaining: {total_time}"))
    while total_time > 0:
        total_time -= 1
        time.sleep(1)
    print("Time is up!")


pomodoro()