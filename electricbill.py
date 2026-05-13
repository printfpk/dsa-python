unit = int(input("enter a unit: "))

amount = 0

if unit > 400:
    amount = (unit - 400) * 13
    unit = 400

if unit > 200 and unit <= 400:
    amount = amount + (unit - 200) * 8
    unit = 200

if unit > 100 and unit <= 200:
    amount = amount + (unit - 100) * 6
    unit = 100

if unit > 0 and unit <= 100:
    amount = amount + unit * 4.2

print(amount)