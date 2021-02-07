# A program that prints an inverted triangle of a specified height
height = int(input("Enter the height of the triangle: "))
# An outer loop that controls the lines
for line in range(height, 0, -1):
    # An inner that controls the stars on each line
    for star in range(line):
        print("* ",end='')
    print()
