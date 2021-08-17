# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 10:48:18 2020

@author: Ayush Padhy
"""

from turtle import *
from random import randint
speed(10)
penup()
goto(-140, 140)
for step in range(15):
    write(step, align = "center")
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
t1 = Turtle()
t1.color("red")
t1.shape("turtle")

t1.penup()
t1.goto(-160, 100)
t1.pendown()

for turn in range(10):
    t1.right(36)
    
t2 = Turtle()
t2.color("blue")
t2.shape("turtle")

t2.penup()
t2.goto(-160, 70)
t2.pendown()

for turn in range(10):
    t2.right(36)

t3 = Turtle()
t3.color("orange")
t3.shape("turtle")

t3.penup()
t3.goto(-160, 40)
t3.pendown()

for turn in range(10):
    t3.right(36)

t4 = Turtle()
t4.color("green")
t4.shape("turtle")

t4.penup()
t4.goto(-160, 10)
t4.pendown()

for turn in range(10):
    t4.right(36)

for turn in range(100):
    t1.forward(randint(1, 5))
    t2.forward(randint(1, 5))
    t3.forward(randint(1, 5))
    t4.forward(randint(1, 5))


