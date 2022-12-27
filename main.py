import tkinter as tk
import math
import pyautogui as pt
from tkinter.messagebox import *
import ctypes
import time
import requests
from playsound import playsound
ROOT = r"C:\Users\lenovo\PycharmProjects\pythonProject1"
PICTURE = r"\Railgun.png"
BGM = r"\only_my_railgun.mp3"


def set_picture(address):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, address, 0)


def update():
    url = 'https://jicanvas.com/feeds/calendars/user_og6OtqQIBvXUzJrkgFCZl1UgxJysel2xnbd9IaVR.ics'
    address = ROOT + r"\courses.txt"
    ics = requests.get(url)
    txt = ics.text
    courses = open(address, 'w')
    i = 0
    while True:
        if txt[i: i + 8] == 'SUMMARY:':
            j = 1
            while True:
                if txt[i + 8 + j: i + 8 + j + 4] == 'URL:':
                    course = txt[i + 8: i + 7 + j].replace('\n', '')
                    course = course.replace('\r ', '')
                    course = course.replace('  ', ' ')
                    courses.write(course)
                    break
                j += 1
        i += 1
        if i > 100000:
            break
    courses.close()


if __name__ == '__main__':
    path = ROOT + PICTURE
    set_picture(path)
    t = 0
    update()
    while True:
        playsound(ROOT + BGM)
        time.sleep(5)
        t += 65
        if t > 3600:
            update()
            t -= 3600
