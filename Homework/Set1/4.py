f1 = 0
f2 = 1

print(str(f1) + " "+ str(f2),end =" ")
for i in range(3,35):
    f3 = f1 + f2
    print(str(f3), end = " ")
    f1 = f2
    f2 = f3
