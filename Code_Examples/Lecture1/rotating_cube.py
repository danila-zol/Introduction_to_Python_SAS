from turtle import *
from math import cos, sin, radians
from time import sleep

SIDE_LENGTH = 100
cube = [
        [0, 0, 0],
        [SIDE_LENGTH, 0, 0],
        [SIDE_LENGTH, SIDE_LENGTH, 0],
        [0, SIDE_LENGTH, 0],
        [0, 0, SIDE_LENGTH],
        [SIDE_LENGTH, 0, SIDE_LENGTH],
        [SIDE_LENGTH, SIDE_LENGTH, SIDE_LENGTH],
        [0, SIDE_LENGTH, SIDE_LENGTH],
]


def rotate_x(vector, rotation_angle):
    result = [0, 0, 0]
    result[0] = vector[0]
    result[1] = vector[1] * cos(rotation_angle) + vector[2] * -sin(rotation_angle)
    result[2] = vector[1] * sin(rotation_angle) + vector[2] * cos(rotation_angle)
    return result


def rotate_y(vector, rotation_angle):
    result = [0, 0, 0]
    result[0] = vector[0] * cos(rotation_angle) + vector[2] * sin(rotation_angle)
    result[1] = vector[1]
    result[2] = vector[0] * -sin(rotation_angle) + vector[2] * cos(rotation_angle)
    return result


def rotate_z(vector, rotation_angle):
    result = [0, 0, 0]
    result[0] = vector[0] * cos(rotation_angle) + vector[1] * sin(rotation_angle)
    result[1] = vector[0] * -sin(rotation_angle) + vector[1] * cos(rotation_angle)
    result[2] = vector[2]
    return result


def render_surface(surface) -> None:
    up()
    goto((surface[0][0], surface[0][1]))
    down()

    for point in reversed(surface):
        goto(point[0], point[1])
    

def render_cube(cube) -> None:
    render_surface(cube[4:])
    render_surface(cube[:4])
    render_surface([cube[4], cube[0], cube[3], cube[7]])
    render_surface([cube[5], cube[1], cube[2], cube[6]])


speed("fastest")

x_increment = radians(numinput("Settings", "Input rotation about X"))
y_increment = radians(numinput("Settings", "Enter rotation about Y"))

x_angle = 0
y_angle = 0

while True:
    for n in range(len(cube)):
        cube[n] = rotate_x(cube[n], x_angle)
        cube[n] = rotate_y(cube[n], y_angle)
    
    x_angle += x_increment
    y_angle += y_increment

    render_cube(cube)
    sleep(1)
    clearscreen()