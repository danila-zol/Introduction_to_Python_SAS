from math import pow

def exponentiate(power):
    def inner(base):
        return pow(base, power)
    return inner

square = exponentiate(2)
cube = exponentiate(3)

print(square(2))
print(cube(2))

