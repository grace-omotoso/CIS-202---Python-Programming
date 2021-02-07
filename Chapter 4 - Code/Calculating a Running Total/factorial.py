# A program to compute the factorial of a number
# Get the number
number = int(input("Enter a number: "))
factorial =  1
for num in range(number, 0, -1):
    factorial*=num #factorial = factorial * num
print(f'{number}! is {factorial}')
