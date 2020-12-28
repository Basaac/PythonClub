# Made by Piz2a

import tkinter as tk
import threading as th
import math
import time
import random


title = 'Moving Screen'
x = 640  # X coordinate
y = 360  # Y coordinate
side = 160
direction = random.uniform(1, 2*math.pi)  # 0 ~ 2pi (Rad)
speed = 400
g = 500  # Gravitical Acceleration
period = 1/40  # Loop Period



def rof(d, rad=1):  # Resolution of Force (힘 분해): return (x, y)
    x, y = 0, 0
    if rad:
        d *= 180 / math.pi
    for i in range(1, 4+1):
        j = i * 90
        if d == 0:
            d = 360
        if j-90 < d <= j:
            c = (j - d) * math.pi / 180
            a, b = math.cos(c), math.sin(c)
            if i % 2 == 1:
                x, y = a, b
                if i == 3:
                    x, y = -x, -y
            else:
                x, y = b, a
                if i == 2:
                    y = -y
                elif i == 4:
                    x = -x
    return x, y


def cof(x, y):  # Composition of Force (힘의 합력): return (direction)
    e = ValueError('(0, 0) has no direction')
    d = math.pi / 2
    if x == 0 and y == 0:
        raise e
    elif x == 0:
        if y > 0:
            return 0
        elif y < 0:
            return d * 2
    elif y == 0:
        if x > 0:
            return d
        elif x < 0:
            return d * 3

    a, b = x, y
    if x < 0 and y < 0:
        d *= 3
        a, b = -x, -y
    elif y < 0:
        d *= 2
        a, b = -y, x
    elif x < 0:
        d *= 4
        a, b = y, -x
    if a != 0 and b != 0:
        d -= math.atan(b / a)
    return d


class MovingScreen(tk.Frame):

    sx = 0
    sy = 0
    t = None
    isRunning = False
    
    def __init__(self, master, x, y, side, direction, speed, g, period):
        print('Creating Screen Successful')
        super().__init__(master)
        self.x = x
        self.y = y
        self.side = side
        self.direction = direction
        self.speed = speed
        self.g = g
        self.period = period

        self.screenw = self.master.winfo_screenwidth()
        self.screenh = self.master.winfo_screenheight()

        self.run()

    def run(self):
        self.master.geometry('{}x{}'.format(self.side, self.side))
        self.master.geometry('+{}+{}'.format(int(self.x), int(self.y)))
        self.master.bind('<Escape>', self.quit)
        self.master.bind('<Button>', self.quit)
        self.master.protocol('WM_DELETE_WINDOW', self.quit)
        self.isRunning = True
        self.t = th.Thread(target=self.move)
        self.t.start()

    def move(self):
        self.sx, self.sy = [self.speed * i for i in rof(self.direction)]
        while self.isRunning:
            self.x += self.sx * self.period
            self.y += self.sy * self.period
            # print('x: {}, y: {}'.format(self.x, self.y))
            # print('y: {}, sy: {}'.format(self.y, self.sy))
            self.master.geometry('+{}+{}'.format(int(self.x), int(self.y)))
            self.sy += self.g * self.period
            self.direction = cof(self.sx, self.sy)
            if not (0 <= self.x <= self.screenw - self.side):
                if self.x < 0:
                    self.x = 0
                elif self.x > self.screenw - self.side:
                    self.x = self.screenw - self.side
                self.sx *= -1
            if not (0 <= self.y <= self.screenh - self.side):
                if self.y < 0:
                    self.y = 0
                elif self.y > self.screenh - self.side:
                    self.y = self.screenh - self.side
                self.sy *= -1
            time.sleep(self.period)

    def quit(self, e=None):
        print('Stopping...')
        self.isRunning = False
        time.sleep(0.1)
        self.destroy()
        self.master.destroy()


def main():
    print('Creating Screen...')
    root = tk.Tk()
    root.title(title)
    root.resizable(False, False)
    frame = MovingScreen(root, x, y, side, direction, speed, g, period)
    try:
        frame.mainloop()
    except KeyboardInterrupt:
        frame.quit()


if __name__ == '__main__':
    main()
