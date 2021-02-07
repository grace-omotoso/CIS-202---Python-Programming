# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Named constants to represent the grade thresholds
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Get a test score from the user.
score = int(input('Enter your test score: '))
while(score < 0 or score > 100):
    print("ERROR: Score cannot be negative or greater than 100")
    score = int(input('Enter your test score again: '))
    
# Determine the grade.
if score >= A_SCORE:
    print('Your grade is A')
elif score >= B_SCORE:
    print('Your grade is B')
elif score >= C_SCORE:
    print('Your grade is C')
elif score >= D_SCORE:
    print('Your grade is D')
else:
    print('Your grade is F')
                
        
