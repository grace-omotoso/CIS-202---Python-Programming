# A program to display a pyramid of a given height
height = int(input("Enter the height of the pyramid: "))
# An outer loop that controls the lines
starcount = 1
for line in range(height-1, -1, -1):
    # An inner loop that controls the spaces
    for space in range(line):
        print(" ",end="")
    # An inner that controls the stars
    for star in range(starcount):
        print("*",end="")
    starcount+=2
    # Go to the next line
    print()

        
