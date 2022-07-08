import time
from playsound import playsound

def waitingTime():
    hoursToWait = int(input("Hours:"))
    minutesToWait = int(input("Minutes: "))
    secondsToWait = int(input("Seconds: "))
    return (hoursToWait * 3600) + (minutesToWait * 60) + secondsToWait


def wait():
    time.sleep(waitingTime())

def alarm():
    wait()
    playsound('alarm01.mp3')

alarm()

# TODO stopwatch
# TODO tkinter UI
# TODO set an audio alarm
