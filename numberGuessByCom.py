#Here a user choose a number than the computer will try to guess the correct number.
import random
import math

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
count = 0
low = lower
up = upper
while count < lifeline:
    count += 1
    c_guess = random.randint(low, up)
    print(f"Computer Guess = {c_guess}")
    #Computer guess the number now user has to say whether its right, low or high:
    while c_guess != user:
        print("""\n\n\tIf guess is low: Reply (L)\n
              If guess is high: Reply (H)""")
        u_reply = input("Enter your reply:").lower()
        if u_reply in ("l","h"):
            break
        else:
            print("Reply out of box:\n\t\tReply again")
    if c_guess == user:
        print(f"Computer Guessed the number in {count} try!!\nThe number is {user}")
        break
    elif u_reply == "l":
        print("Computer Guessed the low number:")
        low = c_guess
    elif u_reply == "h":
        print("Computer guessed the high number:")
        up = c_guess
if count >= lifeline and lifeline > 1:
    print("Computer failed to guess the correct number!!")
