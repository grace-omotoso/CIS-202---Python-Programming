# A program to demonstrate how a boolean variable
# can be used as a flag

QUOTA = 50000 # Create a named constant for sales quota
# Get the sales value from user
sales = float(input("Enter the sales made: "))
if sales >= QUOTA:
    sales_quota_met = True
else:
    sales_quota_met = False

# Check the flag value and determine if quota was met
if sales_quota_met:
    print('You have met your sales quota!')
else:
    print('You have not met your sales quota!')


