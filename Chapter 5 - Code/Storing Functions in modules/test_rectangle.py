import rectangle2
def main():
    # A program to test the rectangle module
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    print('The area is', rectangle2.area(width, length))
    print('The perimeter is', rectangle2.perimeter(width, length))

main()
