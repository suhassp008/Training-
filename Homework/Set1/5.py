n = int(input("enter the number"))
li = []
for i in range(1,n,2):
    li.append(i)
    print(i,end=",")
print(" ")
print("Sum of series :" +str(sum(li)))