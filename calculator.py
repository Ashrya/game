#This is a simple calculator taking 2 number and performing a simple calculation on those number:

#lets first create a function for addition subtraction multiplication and division
#Addition
def add(x, y):
    return x + y

#Subtraction
def sub(x, y):
    return x - y

#Multiplication
def mul(x, y):
    return x * y

#Division
def div(x, y):
    return x / y

#Let's take a number and operation from user
while True:
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if x.is_integer():
            x = int(x)
        if y.is_integer():
            y = int(y)
    except ValueError:
        print("Enter a valid Number")
        continue
    while True:
        print("Choose a operation to perform \n 1) Addition \n 2) Subtraction \n 3) Multiplication \n 4) Division")
        choice = input("Enter your choice: ")
        if choice in ('1', '2', '3', '4'):
            if choice == '1':
                print(x, "+", y, "=", add(x, y))
            elif choice == '2':
                print(x, "+", y, "=", sub(x, y))
            elif choice == '3':
                print(x, "+", y, "=", mul(x, y))
            elif choice == '4':
                print(x, "+", y, "=", div(x, y))
        else:
            print("Invalid choice. Re-enter a choice operation")
            continue
        print("Do you want to perform operation again on same number")
        same_number = input("Enter Y if Yes: ").lower()
        if same_number != 'y':
            break
    #Weather user want to continue the operation or end the program:
    print("Do you want to continue performing operation:")
    user = input("Enter y if Yes: ").lower()
    if user != 'y':
        break

print("\t\tTake care!")