# This program uses a loop to display a
# table showing the numbers 1 through 10
# and their squares.

# Print the table headings.
print('Number\tSquare\tCube')
print('--------------------')

# Print the numbers 1 through 10
# and their squares.
for number in range(1, 11):
    square = number**2
    cube = number**3
    print(f'{number}\t{square}\t{cube}')
