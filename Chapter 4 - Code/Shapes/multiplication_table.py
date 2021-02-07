# A program to print the multiplication table
# Get the rows and columns input
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
# Print the header
for c in range(cols):
    print('-------',end='')
print()
for c in range(1, cols+1):
    if c == 1:
        print(f'      {c:2d}',end='    ')
    else:
        print(f'{c:2d}',end='    ')
print()
for c in range(cols):
    print('-------',end='')
print()
# Print the table
for r in range(1,  rows+1):
    print(f'{r:2d}| ',end='')
    for c in range(1, cols+1):
        print(f'{r*c:4d}  ',end= '')
    print()
    
