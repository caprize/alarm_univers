from os.path import exists, abspath

from playsound import playsound
from datetime import datetime, timedelta
import multiprocessing
import schedule

path_to_song = 'sounds/blackpink-shut-down-mp3.mp3'


def playsound_once(time, path):
    p = multiprocessing.Process(target=playsound, args=(path,))
    p.start()
    input("press ENTER to stop playback")
    p.terminate()
    return schedule.CancelJob


def playSound(time, path):
    p = multiprocessing.Process(target=playsound, args=(path,))
    p.start()
    input("press ENTER to stop playback")
    p.terminate()


def printDefaultmsg(t,time = "12:00"):
    if t == 1:
        print("Please enter the time in format(hh:mm):")
    if t == 2:
        print("Not valid time")
        print("Please enter the time in format(hh:mm):")
    if t == 3:
        print("Do you want to repeat it every day y/n")
    if t == 4 or t == 5:
        print(f'Your alarm is set for:{time}')
    if t == 6:
        print("Please enter in format y/n:")
    if t == 7:
        print("Do you want to set your own music y/n")
    if t == 8:
        print("Set!!")
    if t == 9:
        print("Could not open your file, enter again")
    if t == 10:
        print("Enter your music path")

def checkTimeforValid(time):
    try:
        a = time.split(":")
        b = int(a[0])
        c = int(a[1])
        if len(a) == 2 and len(a[1]) == 2 and len(a[0]) == 2 and b<24 and c<60:
            return 3
    except Exception:
        return 2
    return 2


def checkConftoValid(conf):
    conf = conf.lower()
    if conf == 'y':
        return 4
    elif conf =='n':
        return 5
    return 6


def setSchedule(time,t):
    if t == 4:
        try:
            t1 = schedule.every().day.at(time).do(playSound(time, path_to_song))
            schedule.cancel_job(t1)
        except Exception:
            return 1
    else:
        try:
            t1 = schedule.every().day.at(time).do(playsound_once(time, path_to_song))
            schedule.cancel_job(t1)
        except Exception:
            return 1

def checkForvalidpath(path):
    if not exists(abspath(path)):
        return 9
    return 8

if __name__ == '__main__':

    while True:
        inp1 = input("Press enter if you want to set alarm")
        printDefaultmsg(1)
        time = str(input())
        inp2 = checkTimeforValid(time)
        while inp2 !=3:
            printDefaultmsg(inp2)
            time = str(input())
            inp2 = checkTimeforValid(time)
        printDefaultmsg(inp2)
        inp3 = checkConftoValid(input())
        while inp3 == 6:
            printDefaultmsg(6)
            inp3 = checkConftoValid(input())
        setSchedule(time,inp3)
        printDefaultmsg(inp3,time)
        printDefaultmsg(7)
        inp4 = checkConftoValid(input())
        while inp4 == 6:
            printDefaultmsg(6)
            inp4 = checkConftoValid(input())
        printDefaultmsg(10)
        inp5 = checkForvalidpath(input())
        while inp5 == 9:
            printDefaultmsg(inp5)
            inp5 = checkForvalidpath(input())
        printDefaultmsg(inp5)





