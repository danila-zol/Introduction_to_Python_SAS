from functools import reduce


f = lambda x : x*x
print(f"f is a value {f} of type {type(f)}")

arr = [5, 3, 9, 10]
m = list(map(lambda x: x*x, arr))
red = reduce(lambda x, y: x+y, arr)
fl = list(filter(lambda x: True if x <= 5 else False, arr))

print(f"Result of map x^2: {m}")
print(f"Result of reduce x+y: {red}")
print(f"Result of filter x <= 5: {fl}")