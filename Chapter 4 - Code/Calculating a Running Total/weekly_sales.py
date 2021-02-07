# A program that calculate the total sales for a week
total = 0
for day in range(6):
    sales = float(input("Enter the sales for day "+ str(day+1)+": "))
    total = total+sales
print(f'The total sales is ${total:,.2f}')
