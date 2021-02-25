def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sum, diff, prod = do_calculations(num1, num2)
    print(f'The sum of {num1} and {num2} is {sum}')
    print(f'The difference between {num1} and {num2} is {diff}')
    print(f'The product of {num1} and {num2} is {prod}')
               
def do_calculations(num1, num2):
    sum = num1 + num2
    diff = num1 - num2
    prod = num1*num2

    return sum, diff, prod

main()
