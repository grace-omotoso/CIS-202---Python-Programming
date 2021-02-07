# This program calculates retail prices.
MARK_UP = 2.5  # The markup percentage
another = 'y'  # Variable to control the loop.

# Process one or more items.
while another == 'y' or another == 'Y':
    # Get the item's wholesale cost.
    wholesale = float(input("Enter the item's wholesale cost: "))
    while wholesale < 0:
        print("ERROR: Item cost cannot be less than 0")
        wholesale = float(input("Enter the item's wholesale cost again: "))

    # Calculate the retail price.
    retail = wholesale * MARK_UP

    # Display the retail price.
    print(f'Retail price: ${retail:,.2f}')

    # Do this again?
    another = input('Do you have another item? ' +
                    '(Enter y for yes): ')
