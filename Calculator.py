#Simple calculator lez gooooo

#colors yeheyyyyy
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

import math #for sqrt
while True: #program will loop until user exits 

    line = "---------------------------------------------------"
    print(line)
    print(BLUE + "                    <Calculator>" + RESET)
    print()
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print ("[5] Modulus")
    print("[6] Square root")
    print("[7] Exit")
    print()

    print("Select an action that you would like to perform:")
    UserInput = input ()
    print(line)

    if (UserInput == "1"):
        print("Please enter the numbers separated by a comma")
        num1, num2 = map(int, input().split(','))
        print()
        print (GREEN + "Answer:" , num1 + num2, RESET)

    elif(UserInput == "2"):
        print("Please enter the numbers separated by a comma")
        num1, num2 = map(int, input().split(','))
        print()
        print (GREEN + "Answer:" , num1 - num2, RESET)

    elif(UserInput == "3"):
        print("Please enter the numbers separated by a comma")
        num1, num2 = map(int, input().split(','))
        print()
        print (GREEN + "Answer:" , num1 * num2, RESET)

    elif(UserInput == "4"):
        print("Please enter the numbers separated by a comma")
        num1, num2 = map(int, input().split(','))
        if (num2 != 0):
            print()
            print (GREEN + "Answer:" , num1 / num2, RESET)
            print (GREEN + "Round down:" , math.floor(num1 / num2), RESET)
            print (GREEN + "Round up:" , math.ceil(num1 / num2), RESET)

        else:
            print()
            print (RED + "You can't divide by 0 bozo" + RESET)
            print(PURPLE + "Try again :)))" + RESET)

    
    elif(UserInput == "5"):
        print("Please enter the numbers separated by a comma")
        num1, num2 = map(int, input().split(','))
        print()
        print (GREEN + "Answer:" , num1 % num2, RESET)

    elif(UserInput == "6"):
        print("Please enter the number")
        num = (float(input()))
        result = math.sqrt(num)
        print()
        print( GREEN + "Answer:" , result , RESET)
        print (GREEN + "Round down:" , math.floor(result), RESET)
        print (GREEN + "Round up:" , math.ceil(result), RESET)

    elif(UserInput == "7"):
        print()
        print(PURPLE + "Exiting..." + RESET)
        break

    else:
        print()
        print (RED + "Bro....please choose a number from 1-6" + RESET)