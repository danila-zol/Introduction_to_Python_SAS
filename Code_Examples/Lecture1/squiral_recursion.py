from turtle import *

def step(distance):
    fd(distance)
    rt(90)
    step(distance + 5)

step(10)
