#Calling program of number 1
def kmp():
    # function
    def transform(authorsName):
        # make an empty list
        initial = []
        joined = ""
        initial.append(authorsName[0])
        # search for -
        for i in range(len(authorsName)):
            if authorsName[i] == '-':
                # store inside a list
                initial.append(authorsName[i + 1])
        # combine the list
        joined = joined.join(initial)
        print(joined)
        answer=input("Do you want to choose again? y/n ")
        if answer == 'y':
            menu()
        elif answer == 'n':
            print("Good Bye!")
        else:
            print("Only y/n!")

    # main program
    authorsName = input("Enter the Authors' names :")
    transform(authorsName)

def modul42():
    def modulo(value):
        list = []
        for i in range(10):
            num = int(input("Input number = "))
            remainder = num % value
            list.append(remainder)
        print(len(set(list)), " unique values.")
        print(list)

    value = 42
    modulo(value)
    answer = input("Do you want to choose again? y/n")
    if answer == 'y':
        menu()
    elif answer == 'n':
        print("Good Bye!")
    else:
        print("Only y/n!")

def alicenbob():
    num = int(input("Enter the number of stones left = "))
    list = ["bob", "alice"]
    print(list[num % 2])
    answer = input("Do you want to choose again? y/n ")
    if answer == 'y':
        menu()
    elif answer == 'n':
        print("Good Bye!")
    else:
        print("Only y/n!")

def cupsnball():
    moves = str(input("Enter the moves : "))
    list = ['b', ' ', ' ']
    for i in range(len(moves)):
        if moves[i] == 'a':
            temporary = list[0]
            list[0] = list[1]
            list[1] = temporary
        elif moves[i] == 'b':
            temporary = list[1]
            list[1] = list[2]
            list[2] = temporary
        elif moves[i] == 'c':
            temporary = list[0]
            list[0] = list[2]
            list[2] = temporary
        else:
            print("Only a/b/c!")
    print(list)
    for j in range(3):
        if list[j] == 'b':
            print("The ball is in position", j + 1)
    answer = input("Do you want to choose again? y/n ")
    if answer == 'y':
        menu()
    elif answer == 'n':
        print("Good Bye!")
    else:
        print("Only y/n!")

def menu():
    print(" 1 . KMP","\n","2 . Modul42","\n","3 . Alice N Bob","\n","4 . Cups N Ball")
    menu = int(input("Enter option : "))
    if menu == 1:
        kmp()
    elif menu == 2:
        modul42()
    elif menu == 3:
        alicenbob()
    elif menu == 4:
        cupsnball()
    else:
        print("Only 1/2/3/4!")

#main program
menu()