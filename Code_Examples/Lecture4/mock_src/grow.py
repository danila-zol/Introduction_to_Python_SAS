def grow(n, increment, steps = 1):
	for i in range(steps):
		n += increment
	
	return n

i = grow(5, 2, 10)
print(i)
