# A program to take in scores until a sentinel is found
score = int(input("Enter a number or 0 if there is no number: "))
total = 0
while score != -1:
    total += score
    score = int(input("Enter a number or 0 if there is no number: "))
print("The total score is ",total)
    
