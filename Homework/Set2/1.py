import random as rn

li = []

def prime(num):
    for i in range(2,(num//2)):
        if num % i == 0:
            return False
    return True

arr = []
for i in range(1,16):
    g = rn.randint(1,75)
    li.append(g)
    if prime(g):
        arr.append(g)


print(li)

print("The prime numbers are")
print(arr)  

li.sort(reverse= True )
print("the Descending order is")
print(li)

