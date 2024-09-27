from turtle import *

forward(100) # move forward, can be abbreviated to fd
right(60) # turn right by 60 degrees, can be abbreviated to rt
backward(100) # move backward, can be abbreviated to bk
left(360-60) # turn left, can be abbreviated to lt
forward(100)
left(120) # this instruction is not strictly neccessary to complete a triangle, but it is good to return to the state you started at

mainloop() # when running from a script always end your program with the call to mainloop or the window will close immidiately