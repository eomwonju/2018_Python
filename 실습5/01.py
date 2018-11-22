import turtle

win = turtle.Screen()
t1 = turtle.Turtle()

t1.circle(100, steps=3)
t1.circle(100, steps=4)
t1.circle(100)

win.onkey(exit,'q')
win.listen()
win.mainloop()