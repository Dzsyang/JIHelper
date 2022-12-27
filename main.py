import tkinter as tk
from tkinter.messagebox import *
import pyautogui as pt
import ctypes
import requests
from playsound import playsound

ROOT = r"C:\Users\lenovo\PycharmProjects\pythonProject1"
PICTURE = r"\Railgun.png"
BGM = r"\only_my_railgun.mp3"


class CanvasHelper(object):
    def __init__(self):
        self.winsize = pt.size()
        self.set_wallper()
        self.Window()

    def set_wallper(self):
        def set_picture(address):
            ctypes.windll.user32.SystemParametersInfoW(20, 0, address, 0)

        set_picture(ROOT + PICTURE)
        """
        t = 0
        update()
        while True:
            playsound(ROOT + BGM)
            time.sleep(5)
            t += 65
            if t > 3600:
                update()
                t -= 3600
        """

    def Window(self):
        self.window = tk.Tk()
        self.window.geometry("1000x1300+10+150".format(self.winsize[0] - 1000))
        self.window.title("Clock")
        self.window.resizable(width=False, height=False)
        self.window.wm_attributes("-alpha", 1.0)  # 透明度(0.0~1.0)
        self.window.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.window.wm_attributes("-topmost", False)  # 永远处于顶层
        self.window.wm_attributes("-transparentcolor", "orange")
        self.window.overrideredirect(True)
        self.canvas = tk.Canvas(self.window, bg="orange", width=1000, height=1300, highlightthickness=0)
        self.canvas.pack(expand=1, fill=tk.BOTH)
        self.cx = 500
        self.cy = 600

        def write_title():
            self.ass = self.canvas.create_text(self.cx - 480, self.cy - 600, anchor="nw", text="Canvas Assignment",
                                               fill="white", font=("Edwardian Script ITC", 40))

        def write_ass():
            f = open(ROOT + r"\courses.txt")
            try:
                content = f.read()
            finally:
                f.close()
            self.ass = self.canvas.create_text(self.cx - 480, self.cy - 500, anchor="nw", text=content, fill="white",
                                               font=("Times New Roman", 14))

        write_title()
        write_ass()

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
            self.canvas.delete(self.ass)
            write_ass()
            showinfo(title='Hint', message='Update Successfully!')

        def popup_menu(event):  # 弹出菜单代码
            popup.post(event.x_root, event.y_root)

        """
        canmove = tk.IntVar(self.window, value=False)
        X = tk.IntVar(self.window, value=False)
        Y = tk.IntVar(self.window, value=False)
        
        def onLeftBtnD(event):
            X.set(event.x)
            Y.set(event.y)
            canmove.set(True)

        self.window.bind("<Button-1>", onLeftBtnD)

        def onLeftBtnUp(event):
            canmove.set(False)

        self.window.bind("<ButtonRelease-1>", onLeftBtnUp)
        
        def onLeftBtnM(event):
            if not canmove.get():
                return
            newX = self.window.winfo_x() + (event.x - X.get())
            newY = self.window.winfo_y() + (event.y - Y.get())
            g = f"500x500+{newX}+{newY}"
            self.window.geometry(g)

        self.window.bind("<B1-Motion>", onLeftBtnM)
        """

        popup = tk.Menu(self.window, tearoff=0)
        popup.add_command(label='Update', command=update)
        popup.add_command(label='退出', command=self.window.destroy)

        self.window.bind("<Button-3>", popup_menu)

        self.window.mainloop()


if __name__ == '__main__':
    x = CanvasHelper()
