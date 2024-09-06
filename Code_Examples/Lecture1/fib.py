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
