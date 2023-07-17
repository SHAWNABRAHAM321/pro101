import random 
response="y"
while response == "y":
    a1 = random.randint(1,6)
    if a1 ==1:
        print(" --------- ")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print(" --------- ")
    elif a1 ==2:
        print(" --------- ")
        print("| 0       |")
        print("|         |")
        print("|       0 |")
        print(" --------- ")
    elif a1 ==3:
        print(" --------- ")
        print("|    0    |")
        print("|    O    |")
        print("|    0    |")
        print(" --------- ")
    elif a1 ==4:
        print(" --------- ")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print(" --------- ")
    elif a1 ==5:
        print(" --------- ")
        print("| 0     0 |")
        print("|    O    |")
        print("| 0     0 |")
        print(" --------- ")
    elif a1 ==6:
        print(" --------- ")
        print("| 0     0 |")
        print("| 0     0 |")
        print("| 0     0 |")
        print(" --------- ")
    response = input("would you like to roll the dice(y/n)")
    
