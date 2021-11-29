import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.speed(20)

def draw_axis(s):
    t.setpos(0,0)
    t.shape("circle")
    t.color("blue")
    t.pensize(8)

    for i in range(4):
        t.fd(s)
        t.pu()
        t.goto(0,0)
        t.pd()
        t.lt(90)
    t.ht
draw_axis(300)

t.pu()
t.goto(-100, 90)
t.pd()
t.ht()
t.seth(45)
t.pensize(10)
for n in range(2):
    t.begin_fill()
    t.color("red")
    t.circle(80,90)
    t.circle(150, 90)
    t.end_fill()

t.penup()
t.goto(-100, 30)
t.pendown()
t.write("ellipse")



t.penup()
t.goto(-100, -250)
t.pendown()
t.begin_fill()
t.color("green")
t.circle(90, 190, 50)
t.end_fill()
t.penup()
t.goto(-250, -200)
t.pendown()
t.write("Half ellipse")

t.pu()
t.goto(300, 90)
t.pendown()

t.pd()
t.ht()
t.seth(45)
t.pensize(10)
for n in range(1):
    t.begin_fill()
    t.color("red")
    t.circle(90,110)
    t.circle(110, 110)
    t.end_fill() 

turtle.mainloop()