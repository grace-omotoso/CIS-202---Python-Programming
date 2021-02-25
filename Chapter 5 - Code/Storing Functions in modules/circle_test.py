# A program to test circle module
import circle
def main():
    radius = float(input("Enter the radius of the circle: "))
    area = circle.area(radius)
    circum = circle.circumference(radius)
    print(f'The areas of a circle with radius {radius} is {area:.2f}.')
    print(f'The circumference of a circle with radius {radius} is {circum:.2f}.')

main()
