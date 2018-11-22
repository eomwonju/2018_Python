import turtle

wn = turtle.Screen()
t1 = turtle.Turtle()

r = int(input())
t1.right(90)
t1.penup()
t1.forward(r)
t1.pendown()
t1.left(90)
t1.circle(r)
t1.goto(r,0)
t1.goto(0,r)
t1.goto(-r,0)
t1.goto(0,-r)

wn.mainloop()