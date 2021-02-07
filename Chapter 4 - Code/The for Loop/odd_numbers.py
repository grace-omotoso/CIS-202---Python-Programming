# A program to print odd numbers between two numbers (both inclusive)
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
if lower % 2 == 0:
    lower = lower + 1
for num in range(lower, upper+1, 2):
    print(num)
