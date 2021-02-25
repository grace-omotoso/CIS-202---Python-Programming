# A program to demonstrate how functions can return
# Boolean values
def main():
    number = int(input('Enter a number: '))
    if is_even(number):
        print('The number is even. ')
    else:
        print('The number is odd. ')
        
def is_even(number):
    # Determine whether number is even. If it is,
    # set status to true. Otherwise, set status
    # to false.
    if (number % 2) == 0:
        status = True
    else:
        status = False
    # Return the value of the status variable.
    return status
main()
