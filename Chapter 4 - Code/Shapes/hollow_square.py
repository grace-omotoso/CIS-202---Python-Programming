# A program to print hollow square of specified height
side = int(input("Enter the length of the sides: "))
# An outer loop that controls the lines
for line in range(side):
    # An inner loop that controls the stars
    for star in range(side):
        # print full stars for first and last lines
        if (line == 0 or line == side-1):
            print("* ", end = "")
        # print star only on first and last column
        else:
            if (star == 0 or star == side-1):
                print("* ",end="")
            else:
                print("  ",end="")
    print()
        
