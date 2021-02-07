# This program displays gross pay.
# Get the number of hours worked.
hours = int(input('Enter the hours worked this week: '))
while (hours > 168 or hours < 0):
    print("Hours must be greater than 168 and not less than 0")
    
    hours = int(input('Enter the hours worked this week: '))
    
# Get the hourly pay rate.
pay_rate = float(input('Enter the hourly pay rate: '))

# Calculate the gross pay.
gross_pay = hours * pay_rate

# Display the gross pay.
print(f'Gross pay: ${gross_pay:,.2f}')
