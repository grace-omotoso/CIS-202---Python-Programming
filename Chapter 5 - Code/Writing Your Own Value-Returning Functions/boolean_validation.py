# A program that shows how functions can be used
# to validate input
# Suppose we want to prompt a user to enter a product
# model number assuming valid values are 100, 200, and 300
def main():
    # Validate the model number.
    model = int(input('Enter a valid model number: '))
    while is_invalid(model):
        print('The valid model numbers are 100, 200 and 300.')
        model = int(input('Enter a valid model number: '))
        
def is_invalid(mod_num):
    if mod_num != 100 and mod_num != 200 and mod_num != 300:
        status = True
    else:
        status = False
    return status

main()
