#This is an number guessing game where you have to guess a number choosen by computer. 
#First lets import all required librery
import random
import math
#Now lets provide a computer a range of number from where it can choose any number
while True:
    try:
        lower = int(input("Enter lower range:"))
    except ValueError:
        print("\t\tEnter integer for lower range")
        continue
    while True:
        try:
            upper = int(input("Enter upper range:"))
            break
        except ValueError:
            print("\t\tEntered", lower, "for lower\n\t\tEnter integer for upper range")
            continue
    if lower < upper:
        break
    else:
        print("\t\tLower range",lower,">=",upper,"upper range\n\t\tRe-Enter the value")
        continue

#Here computer choose a random number from provided range
x = random.randint(lower,upper)
#Lets provide a user a lifeline 
lifeline = round(math.log(upper-lower+1,2))
print(f"You have {lifeline} lifeline: ")

#Initializing the number of count
count = 0
#Running loop until lifeline of user is available
while count < lifeline:
    count += 1
    #lets take an input guess from user
    user = int(input("Enter the number: "))
    if user == x:
        print("\n\n\t\tCongratulation You Guessed the right number in ", count, "try")
        #after guessing a correct number, loop should be closed
        break
    elif user > x:
        print("\t\tThe guessed number",user, "is high\n\t\tTry low")
    elif user < x:
        print("\t\tThe guessed number",user, "is low\n\t\tTry high")
#After user count meets lifeline, End program providing correct guessed number
if count >= lifeline:
    print("The correct number is", x ,"\nBetter luck next time!")