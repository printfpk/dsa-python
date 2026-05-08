arr = [12, 45, 2, 89, 34, 89, 67]

largest = float('-inf')
second = float('-inf')

for num in arr:

    if num > largest:
        second = largest
        largest = num

    elif num > second and num != largest:
        second = num

print("Largest:", largest)
print("Second Largest:", second)