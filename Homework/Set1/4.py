fib1 = 0
fib2 = 1

print(str(fib1) + " "+ str(fib2),end =" ")
for i in range(3,35):
    fib3 = fib1 + fib2
    print(str(fib3), end = " ")
    fib1 = fib2
    fib2 = fib3