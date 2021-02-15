# This program demonstrates a function that accepts
# two arguments.

def main():
    # print('The sum of 12 and 45 is')
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the secomd number: "))
    show_sum(num1, num2)

# The show_sum function accepts two arguments
# and displays their sum.
def show_sum(num1, num2):
    result = num1 + num2
    print(f'The sum of {num1} and {num2} is {result}')
    # print(result)

# Call the main function.
main()
