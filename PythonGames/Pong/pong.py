import turtle
import os

wn = turtle.Screen()
wn.title("Pong by SP")
wn.bgcolor("#8000ff")
wn.setup(width=800,height = 600)
wn.tracer(0)

score_a = 0
score_b = 0

#Paddle A
pa = turtle.Turtle()
pa.speed(0)
pa.shape("square")
pa.color("white")
pa.shapesize(stretch_wid = 5,stretch_len=1)
pa.penup()
pa.goto(-350,0)

#Paddle B
pb = turtle.Turtle()
pb.speed(0)
pb.shape("square")
pb.color("white")
pb.shapesize(stretch_wid = 5,stretch_len=1)
pb.penup()
pb.goto(350,0)

#Ball
b = turtle.Turtle()
b.speed(0)
b.shape("circle")
b.color("white")
b.penup()
b.goto(0,0)
b.dx = 0.25
b.dy = -0.25

#Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PLAYER A: 0 PLAYER B: 0", align="center", font =("Arial",24,"normal"))

def pa_up():
    y = pa.ycor()
    y += 20
    pa.sety(y)
    
def pa_down():
    y = pa.ycor()
    y -= 20
    pa.sety(y)

def pb_up():
    y = pb.ycor()
    y += 20
    pb.sety(y)
    
def pb_down():
    y = pb.ycor()
    y -= 20
    pb.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(pa_up,"w")
wn.onkeypress(pa_down,"s")
wn.onkeypress(pb_up,"Up")
wn.onkeypress(pb_down,"Down")


while(True):
    wn.update()

    #Move Ball
    b.setx(b.xcor() + b.dx)
    b.sety(b.ycor() + b.dy)

    #Border
    if b.ycor() > 290:
        b.sety(290)
        b.dy *= -1
        os.system("aplay bounc.wav&")
    if b.ycor() < -290:
        b.sety(-290)
        b.dy *= -1
        os.system("aplay bounc.wav&")
    if b.xcor() > 390:
        b.goto(0,0)
        b.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PLAYER A: {} PLAYER B: {}".format(score_a,score_b),align="center", font =("Arial",24,"normal"))
    if b.xcor() < -390:
        b.goto(0,0)
        b.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("PLAYER A: {} PLAYER B: {}".format(score_a,score_b),align="center", font =("Arial",24,"normal"))

    #Paddle and Ball collisions
    if (b.xcor() > 340 and b.xcor() < 350) and (b.ycor() < pb.ycor() + 40 and b.ycor() > pb.ycor() - 40):
        b.setx(340)
        b.dx *= -1
        os.system("aplay bounc.wav&")
    if (b.xcor() < -340 and b.xcor() > -350) and (b.ycor() < pa.ycor() + 40 and b.ycor() > pa.ycor() - 40):
        b.setx(-340)
        b.dx *= -1   
        os.system("aplay bounc.wav&")
