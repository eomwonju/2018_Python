import turtle
import math

win = turtle.Screen()
t1 = turtle.Turtle()

r=100
t1.circle(r)
t1.forward(r)
t1.left(45)
t1.circle(r*math.sqrt(2), steps=4)
t1.circle(r*math.sqrt(2))

win.onkey(exit,'q')
win.listen()
win.mainloop()