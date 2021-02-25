# A program to find the area of a cirlce
import math

def main():
    radius = float(input("Enter the radius of the circle: "))
    print(f'The area of a circle with radius {radius} is {area(radius):.2f}')

def area(radius):
    return math.pi*radius**2

main()
