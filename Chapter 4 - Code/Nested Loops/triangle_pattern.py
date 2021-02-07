# This program displays a triangle pattern.
base_size = int(input("Enter the base size of triangle: "))

for r in range(base_size):
    for c in range(r + 1):
        print('*', end='')
    print()
