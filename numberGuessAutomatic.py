#Here a user choose a number than the computer will try to guess the correct number.
import random
import math
import time

#Lets the user choose the number and declare the lower limit and upper limit
while True:
    #user input
    try:
        user = int(input("Enter the number:"))
    except ValueError:
        print("Enter Integer value:")
        continue
    while True:
        #setting lower limit
        try:
            lower = int(input("\nEnter the lower limit:"))
        except ValueError:
            print("Enter Integer value:")
            continue
        #setting upper limit
        try:
            upper = int(input("\nEnter the upper limit:"))
        except ValueError:
            print("Enter Integer value:")
            continue
        if lower < upper:
            break
        else:
            print(f"\t\tLower is greater than upper: {lower} > {upper}")
    if user in range(lower,upper):
        print(f"Number is between {lower} and {upper}")
        break
    else:
        print("Number is not in range, Re-enter the value: ")
#Now let computer guess the number:
lifeline = round(math.log(upper  - lower+1, 2))
print(f"Computer has {lifeline} chance to guess")
count = 1
repeated_num = list()
while count <= lifeline:
    count += 1
    number_pool = list(range(lower, upper))
    unique_list = [i for i in number_pool if i not in repeated_num]
    c_guess = random.choice(unique_list)
    print(f"\n\nComputer Guess = {c_guess}")
    #Computer guess the number now user has to say whether its right, low or high:
    if c_guess == user:
        print(f"Computer Guessed the number in try!!\nThe number is {user}")
        break
    elif c_guess < user:
        print("Computer Guessed the low number:")
        lower = c_guess
    elif c_guess > user:
        print("Computer guessed the high number:")
        upper = c_guess
    repeated_num.append(c_guess)
    time.sleep(3)
if count > lifeline:
    print("Computer failed to guess the correct number!!")
