n = int(input("Enter number of rows: "))

# Upper Part
for i in range(1, n + 1):

    # Left stars
    for j in range(i):
        print("*", end="")

    # Spaces
    for j in range(2 * (n - i)):
        print(" ", end="")

    # Right stars
    for j in range(i):
        print("*", end="")

    print()

# Lower Part
for i in range(n, 0, -1):

    # Left stars
    for j in range(i):
        print("*", end="")

    # Spaces
    for j in range(2 * (n - i)):
        print(" ", end="")

    # Right stars
    for j in range(i):
        print("*", end="")

    print()