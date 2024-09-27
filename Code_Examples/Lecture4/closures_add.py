def grow(n, start_value = 1, increment = 5):
	for i in range(n):
		start_value += increment
	
	return start_value

def get_growth_func(start_value, increment):
    def grow_step(n):
        sv = start_value
        for i in range(n):
            sv += increment
        
        return sv
    
    return grow_step

def print_sequence(f, len):
    for n in range(len):
        print(str(f(n)), end=", ")
    print("... ")

f = get_growth_func(5, 10)
print_sequence(f, 10)
