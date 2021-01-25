# This program gets an item's original price and
# calculates its sales price, with a 20% discount.

# Get the item's original price
original_price = float(input("Enter the item's original price: "))

# Calcilate the amount of the discount
discount = original_price*0.2

# Calculate the sale prce
sale_price =  original_price - discount

# Display the sale price
print('The sale price is ', sale_price)
