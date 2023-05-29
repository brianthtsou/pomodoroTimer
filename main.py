import time
import datetime
# from timer_py import Timer

def pomodoro():
    total_time = 25 #* 60
    rest_time = 5
    print((f"Time remaining: {total_time}"))
    s = input("Enter any character to start: ")
    while total_time > 0:
        total_time -= 1
        time.sleep(1)
    print("Time is up! Time for a break!")
    s = input("Enter any character to start: ")
    print((f"Time remaining: {rest_time}"))
    while rest_time > 0:
        rest_time -= 1
        time.sleep(1)

pomodoro()