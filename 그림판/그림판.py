import turtle as t

t.shape('turtle')
def mDrag(x,y):
    t.ondrag(None) 
    t.goto(x,y)
    t.ondrag(mDrag) 
t.ondrag(mDrag)

def esc():
    t.clear()
def red():
    t.color("red")
def green():
    t.color("green")
def blue():
    t.color("blue")
def black():
    t.color("black")
def pensize():
    t.pensize(3)
def smallsize():
    t.pensize(2)
def white():
    t.color('white')
t.speed(0)
t.pensize(2)
t.onkeypress(esc , "Escape")
t.onkeypress(red , "1")
t.onkeypress(green , "2")
t.onkeypress(blue , "3")
t.onkeypress(black , "0")
t.onkeypress(pensize , "Up")
t.onkeypress(smallsize , "Down")
t.onkeypress(esc , "Escape")
t.onkeypress(white,'4')
t.listen()
t.mainloop()
