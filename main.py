from playsound import playsound
from datetime import datetime, timedelta
import multiprocessing
import schedule

path_to_song = 'sounds/blackpink-shut-down-mp3.mp3'


def playsound_once(time, path):
    print(f'Your alarm, set on {time} is playing')
    p = multiprocessing.Process(target=playsound, args=(path,))
    p.start()
    input("press ENTER to stop playback")
    p.terminate()
    return schedule.CancelJob


def playSound(time, path):
    print(f'Your alarm, set on {time} is playing')
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

def checkTimeforValid(time):
    try:
        a = time.split(":")
        if len(a) == 2 and len(a[1]) == 2 and len(a[0]) == 2:
            return 3
    except Exception:
        return 2
    return 2


def checkConftoValid(conf):
    if conf == 'y':
        return 4
    elif conf =='n':
        return 5
    return 6


def setSchedule(time,t):
    if t == 4:
        t1 = schedule.every().day.at(time).do(playSound(time, path_to_song))
        schedule.cancel_job(t1)
    else:
        t2 = schedule.every().day.at(time).do(playsound_once(time, path_to_song))
        schedule.cancel_job(t2)


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
        setSchedule(time,inp3)
        printDefaultmsg(inp3,time)



