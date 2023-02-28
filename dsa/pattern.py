 for row in range(1, 5):
    for col in range(1, 6-row):
        print(" ", end="")
    for col in range(1, 2*row):
        print("*", end="")
    print()

for row in range(3, 0, -1):
    for col in range(1, 6-row):
        print(" ", end="")
    for col in range(1, 2*row):
        print("*", end="")
    print()
