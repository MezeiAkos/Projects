import time
from playsound import playsound


def waiting_time():
    hours_to_wait = int(input("Hours:"))
    minutes_to_wait = int(input("Minutes: "))
    seconds_to_wait = int(input("Seconds: "))
    return (hours_to_wait * 3600) + (minutes_to_wait * 60) + seconds_to_wait


def wait():
    time.sleep(waiting_time())


def alarm():
    wait()
    playsound('alarm01.mp3')


alarm()

# TODO stopwatch
# TODO tkinter UI
# TODO figure out why .waw doesn't work
