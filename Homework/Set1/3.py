n = int(input("Enter the lenght"))
res = 0
for i in range(2,n,1):
    res+=(1/(i**3))

print(res)
