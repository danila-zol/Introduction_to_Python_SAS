from turtle import *

base_length = 10

for n in range(35):
    for n in range(3):
        fd(base_length)
        rt(120)
    base_length += 10
    rt(20)

mainloop()