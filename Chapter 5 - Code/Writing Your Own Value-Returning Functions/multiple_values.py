def main():
    first_name, last_name = get_name()
    print("First Name:",first_name)
    print("Last Name:",last_name)
    last, first = reverse_names(first_name, last_name)
    print("My name in reverse order is ",last, first)

def get_name():
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    return first, last

def reverse_names(first, last):
    return last, first

main()
