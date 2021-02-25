# This program simulates 10 tosses of a coin.
import random

# Constants
HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(10):
        # Simulate the coin toss.
        if random.randint(1, 2) == 1:
            print('Heads')
        else:
            print('Tails')
            
# Call the main function.
main()
