# Object-Oriented Programming Basics

## What OOP Is

As the complexity of our programs we are confronted more and more with the need to create *abstraction* to manage that complexity. One of the patterns most prevalent in programming today that is used to achieve this goal is **Object-Oriented Programmin** or OOP for short.

## Real World Example
When programming in OOP style instead of focusing on how the computer will interpret your code, you structure your program to reflect the way humans think about entities and the logical relationships between them.

Suppose we are writing a racing video game. In it we need to have a variety of vehicles from small motorcycles to giant trucks. We can write unique data structures to model each of them and unique functions to act on each of those structures. However, you will soon realize that despite their differences all of the vehicles share a great deal of behaivior, for example they probably all have a `speed` variable, a `move` function and so on. Instead of implementing the same functionality over and over we can define all these vehicles to be of the same *class* to share this common functionality. `Car`, `Motorcycle`, `Truck`, and other classes will **inherit** from the common `Vehicle` class fascilitating code reuse. On the other hand all of the behaviour unique to `Truck`, `Motorcycle`, or `Car` can be defined inside those child classes.

Functions defined to act on a class are called **methods**. Variables defined inside a class are called **fieldds**. Every class in Python has a special `__init__` method that gets called when the class is instantiated. In it you can set various default values or run initialization code required for your class to work. To refer to the object itself within a method you use `self` keyword. Child classes can also override any methods defined in the parent class in Python. To call the parent method from the child you use `super` keyword. This feature is very useful for example when you want to first perform initialization for all of the variables your class inherited from the parent and then run additional initialization code for the data specific to the child.

The syntax goes like this:

```python
class Vehicle:

    max_speed = 100 # Field with a default value

    # Special initialization function
    def __init__(velocity = 0, heading = [0, 0, 0], position = [0, 0, 0]):
        self.velocity = velocity # Setting up default fields
        self.heading = heading
        self.position = position

    # Methods
    def turn(heading):
        self.heading += heading

    def move(position):
        self.position += position

# Class inheriting from Vehicle
class Car(Vehicle):
    def __init__(velocity = 0, heading = [0, 0, 0], position = [0, 0, 0]):
        super(velocity, heading, position) # calling __init__ of the parent class
        self.max_speed = 150

    def open_trunk():
        printf("Opened trunk")

    def close_trunk():
        print("Closed trunk")

class Truck(Vehicle):
    parcels = []

    def load_parcels(parcels):
        self.parcels.append(parcels)

    def unload_parcel(parcels):
        return self.parcels.pop()
```

Class itself only defines a class. It is like a blueprint for the data that we will fill in runtime. We need to **instantiate** the class to make an actual variable following the class declaration. A resulting variable is called **an instance of the class**. The word **object** is commonly used to refer both to the class definition and to the class instances.

The syntax for instantiation is similar to calling a function:

```python
car = Car()
truck = Truck()
```

The usual convention in Python is to name variables or functions in all lowercase and in camel case (starting with an uppercase letter).

Objects fascilitate code reuse and incapsulation of state. Instead of working with a lot of variables we can model our program as an interaction between a handful of objects that each manage their own state and only provide a clean interface to consumers with methods.

All values in Python are objects under the hood and operators are actually defined as special methods on those objects. That is why you can override default operators such as addition, multiplication, and and so on in your classes. So called operator overloading is very useful to make operations with your classes more intuitive.

Those special methods take the form of `__operation__(operand)`, the method for addition is `__add__(n)`. Full list can be found in Python documentation: https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types

For example we can define a type vector and implement proper scalar addition on it. In a default Python list the plus `+` operator means concatentaion, not mathematical addition and concatenation between list and integer is not defined, so it will not serve us well to represent vectors, unlike the class we declare here:
