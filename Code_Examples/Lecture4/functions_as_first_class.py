def fib(n):
    prev_term = 0
    next_term = 1

    for i in range(n):
        tmp = prev_term
        prev_term = next_term
        next_term += tmp

    return next_term

def grow(n, start_value = 1, increment = 5):
	for i in range(n):
		start_value += increment
	
	return start_value

def print_sequence(f, len):
    for n in range(len):
        print(str(f(n)), end=", ")
    print("... ")

f = fib
print(f"f is a value {f} of type {type(f)}")

print_sequence(f, 10)
print_sequence(grow, 10)
