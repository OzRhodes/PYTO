'''
A simple analog clock
uses turtle

logic should work but believe
PYTO turtle implementation may be flawed
 
'''


from turtle import *
import turtle
import time

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

def draw_clock(t):
    t.clear()
    t.up()
    t.goto(0, -100)
    t.color("black")
    t.pendown()
    t.circle(100)
        
    for num in range(12):
        t.up()
        t.goto(0,0)
        t.setheading(num*30)
        t.fd(90)
        t.down()
        t.fd(5)
    t.goto(0,0)
    return

def draw_hands(hour, minutes, seconds, t):

    hands = [("red", 50), ("blue", 80), ("black", 70)]
    
    # draw hour:
    angle = hour*30-90 + (30*minutes/60)
    t.penup()
    t.goto(0, 0)
    t.color(hands[0][0])
    t.setheading(angle)
    t.pendown()
    t.fd(hands[0][1])
    
    # draw minutes:
    angle = minutes*6-90
    t.penup()
    t.goto(0, 0)
    t.color(hands[1][0])
    t.setheading(angle)
    t.pendown()
    t.fd(hands[1][1])
    
    # draw seconds:
    angle = seconds*6-90
    t.penup()
    t.goto(0,0)
    t.color(hands[2][0])
    t.setheading(angle)
    t.pendown()
    t.fd(hands[2][1])    
    
    return


draw_clock(t)
while True:
    hour = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))
    draw_hands(hour, minutes, seconds, t)
    ws.update()
    time.sleep(1)








