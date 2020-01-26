cp = int(input("input the cp:" ))
sp = int(input("input the sp:"))
if cp<sp:
    print("Profit")
    profit = sp-cp
    print(profit)
elif cp>sp:
    print("Loss")
    Loss = cp-sp
    print(Loss)
else:
    print("same")

