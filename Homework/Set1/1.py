cp = int(input("input the cost price :" ))
sp = int(input("input the selling price:"))
if cp<sp:
    print("Profit")
    profit = sp-cp
    print(profit)
elif cp>sp:
    print("Loss")
    Loss = cp-sp
    print(Loss)
else:
    print("Same")

