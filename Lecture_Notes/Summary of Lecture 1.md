## Background
### How a computer works?
You probably already know at least something about computers, but let's rehearse. A computer is a device that can perform general purpose computations (duh). It has some way of receiving input (keyboard and mouse or remote SSH commands for servers), some amount of memory that the running programs are loaded to called RAM[1](#notes), permanent storage (HDD[2](#notes), SSD[3](#notes)), some output device (monitor, teletype, packets send over the internet), and perhaps most importantly a Central Processing Unit (CPU for short) that can executing execute commands written in machine code.

But how do we program a computer? Back in the day you had to learn something called an assembly language: a minimal abstraction over ones and zeroes of the machine code that a programmer can at least partially comprehend. However, nowadays the operating system such as Windows or Linux handles most of the work of managing the hardware and you can write your program in a _high level_ language such as Python without worrying about low-level hardware.

### Types of Programming Languages
Each programming language fundamentally solves the same problem: "How do we write code that a computer can execute, but also that a human can understand?"

Currently there are three major approaches to transforming code written in a programming language ergonomic to humans to machine code that a computer can execute:
- Ahead-Of-Time (AOT) compilation (or just compilation). 
	- Typical examples: C, Rust, Java
- Just-In-Time (JIT) compilation
	- Typical examples: JavaScript (V8), Julia
- Interpreting
	- Typical examples: Python, Ruby, Perl

Python is an interpreted language. That means it evaluates the expressions as you type them in a prompt interactively or line by line in a script if used non-interactively. Python also is _memory managed_ language which means the interpreter that executes your code will automatically allocate and deallocate memory for variables and you don't have to think about it.

## Anatomy of a program
### Variables
Variables allow us to attach a name to data stored by our program or provided to it. Giving variables descriptive names is an important aspect of readability. To assign a value to a variable you use the equals sign "=", note however that in programming it has a different meaning than in math. In programming equals sign means assignment, not equality, so a statement like `i = i + 5` makes perfect sense in a Python program, but would simplify to non-sensical 0 = 5 if read as math notation. 

Variables can point to data of different types, the most fundamental ones we will be using for now are:
- Strings. This type stores text. Denoted with quotes. 
- Integers. This type stores whole numbers.
- Floating point numbers or just floats. This type stores numbers with a fraction part. 
- List. This type stores a list of other variables. Denoted with square brackets.

Examples of each type:
```python
course_name = "Introduction to Python" # String

course_attendance = 26 # Integer

average_grade = 8.4 # Float

student_names = ["Alexey", "Olesya", "Andrey", "Nelly"] # List
```

### Operators
In Python you can use all of the familiar mathematical operators to form expressions. They follow conventional precedence rules which you can overcome by putting an expression inside parenthesis analogously to regular math notation. Additionally there is a shorthand notation for performing operation on a value and then assigning it back to itself because this operation arises often in programming.

Examples:
```python
i = 1 + 4 # i is 5
i = 4 - 2 # i is 2

i = 2 * 2 # i is 4
i = 1 / 2 # i is 0.5

i = (1 + 3) / 3 # i is 1

# Only makes sense in programming
i = i + 5

# Shorthand
i += 2 # Identical to i = i + 2
i -= 2 # Identical to i = i - 2
i *= 2 # Identical to i = i * 2
i /= 2 # Identical to i = i / 2
```

### Functions
Functions are blocks of code that you can reuse over and over. They follow notation similar to math, however unlike in math functions in a program can modify values passed to it or other values in your program, this is called side-effects. Because functions with side-effects rely on external _state_ they do not neccesairly produce the same output given the same set of inputs like mathematical functions, but functions without side-effects that do are called _pure functions_. If you can make your function a pure function this is always preferable because pure functions are easier to debug and in general less error prone. 

You can define your own functions or import functions and variables from libraries written by other programmers.

One last thing to remeber is that a good function does one thing well and one thing only. If your function grows in size to the point it is hard to reason about that means you should split it into multiple smaller functions. The process of changing the source code to enhance its structure without changing its functionality is called _refactoring_. 

Example of calling library functions. Here we import a function that rises a number to power `pow`, caluclates cosine `cos`, convert degrees to radians `radians`, and a variable `pi` which approximates the value of π:
```python
print("Hello, World!")

from math import pow, cos, radians, pi

i = pow(2, 2) # i is 4
i = cos(pi) # i is 1
i = cos(radians(180))# same as cos(pi)
```

The syntax for defining your own functions is as follows:
```python
def get_rectangle_area(w, l):
	a = w * l
	return a

w = 10
l = 20
a = get_rectangle_area(w, l)

print("Area of the rectangle is " + str(a))

```

This example illustrates that each function forms its own _scope_ that is variables defined within a function do not interfere with variables defined elsewhere in our program. That is why we can have variables `w`, `l`, `a` both inside the definition of a function and near its invocation without any problem.

You can also see that indentation plays important role in a Python program. Unlike some other languages that define these scopes with curly brackets or keywords, Python uses indentation level to denote a scope. Thankfully VS Code will take care of keeping the right indentation level most of the time and in case of a mistake Python will produce a discriptive error.

### For Loop
For loop allows you to repeat a certain action for each element in a list. We can also use `range(n)` function to provide us with a list of values from 0 to n to run the loop n times.

Demonstration:
```python
students = ["Alexey", "Olesya", "Andrey", "Nelly"]

for student in students:
	print(student) # will print each name

def grow(n, increment, steps = 1):
	for i in range(steps):
		n += increment
	
	return n

i = grow(5, 2, 10)

```

With just this limited knowledge we can already approximate the golden ratio!
```python
def fib(n):
    prev_term = 0
    next_term = 1

    for i in range(n):
        tmp = prev_term
        prev_term = next_term
        next_term += tmp

    return next_term

f11 = fib(11)
f12 = fib(12)

print("The Golden Ratio is " + str(f12 / f11))
```

## Good Thing 2 Rember
- If you run into problems with your program first try to imagine yourself a computer and go through each line step by step to understand what is going on.
- A program consists of expressions that just return a value and statements that can modify other values and have side effects. This a useful distinction to undestand Python's syntax. We can conclude that you can assign a value of any expression to a variable with assignment operator `=` and any expression can be an argument to a function call.
## Turtle
Turtle is a simple programmable object introduced by Seymour Papert for teaching programming to kids. A turtle has two properties: heading and position, and can be controlled programmatically to move in space. As it moves it leaves a line behind allowing you to draw shapes. It is easy to draw simple shapes and shapes with radial symmetry.  With enough skill you can make turtle draw more complicated images or geometry.

Turtle syntax demonstration:
```python
from turtle import *

forward(100) # move forward, can be abbreviated to fd
right(60) # turn right by 60 degrees, can be abbreviated to rt
backward(100) # move backward, can be abbreviated to bk
left(360-60) # turn left, can be abbreviated to lt
forward(100)
left(120) # this instruction is not strictly neccessary to complete a triangle, but it is good to return to the state you started at

```
You can also issue commands:
`up()` to stop turtle from drawing, think about this command as lifting up your pen.
`down()` to continue drawing, think about this command as putting it down.
`reset()` to reset your canvas, and this one as throwing away the artwork.
`clear()` to clear the screen.

**Important Note:** When running Turtle from a script you need to call the function `mainloop()` at the end after all of the turtle commands. Otherwise the window with your turtle will just close immediately after it's done drawing and you will not be able to appreciate the result.

And some other ones. Consult the documentation at https://docs.python.org/3/library/turtle.html if you want to get further information about this module. It is not crucial right now, but in general for an aspiring programmer it is important to gain the skill of reading and learning from technical documentation.

You can easily create visually complex patterns using a for loop:
```python
from turtle import *

for n in range(20):
    for n in range(360):
        fd(2)
        rt(1)
    rt(18)
```

To create an infinite loop use `while True`
```python
from turtle import *
from math import pi

radius = 10

while True:
    fd(radius * 2 * pi / 360)
    rt(1)
    radius += 0.1
```

You can call the function from within the function, this is called recursion. This technique is sometimes used in practice and for our drawing purposes can be used similar to an infinite loop since we don't know how to set conditions to exit the function yet (will be covered in the next lecture):
```python
from turtle import *

def step(distance):
    fd(distance)
    rt(90)
    step(distance + 5)

step(10)
```


## Homework
1. Write in the Discord (`homework` channel) about one interesting discovery about Turtle that you have made and that feels meaningful to you. Note that you can use documentation at https://docs.python.org/3/library/turtle.html to study this operator further.
2. Write a program using Turtle that draws something. Can be simple geometry or a more complicated shapes. You can use examples in a repository I created for this course as reference: https://github.com/danila-zol/Introduction_to_Python_SAS/tree/main/Code_Examples/Lecture1 .


### Notes

1. Rapid-access memory.
2. Hard drive disk.
3. Solid state drive.
