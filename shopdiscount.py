amount = float(input("enter a number: "))

dis = 0

if amount >= 0 and amount <= 5000:
    dis = 0

elif amount > 5000 and amount <= 15000:
    dis = 10

elif amount > 15000 and amount <= 25000:
    dis = 20

else:
    print("invalid amount")

total = amount - (amount * dis / 100)

print(total)