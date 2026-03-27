import random

print("You can freely interact with a list using this program. Input 1 for viewing the list, and 2 for editing.")
print("By inputting quit, you will always quit the progam, safely.")

userinput = input("Input here: ")
list1 = []

def start(): #start program
    startmsg()
    check_fuin()

def startmsg(): #start program msg
    print("Starting program")
def quitmsg(): #quit program msg
    print("Exiting program... ")
def invalidinputmsg(): #outputs invalid input message
    print("Invalid input. ")

def check_fuin(): #first function that handles input at start - check_fi
    if userinput == "1":
        view()
    elif userinput == "2":
        check_fxe()
    elif userinput == "quit":
        quitmsg()
    else:
        invalidinputmsg()
def view(): #for viewing, sends to handling editing func if needed - view?
    print(list1)
    view_ec = input("Would you like to edit this list? (y/n): ")
    if view_ec == "y":
        check_fxe()
    elif view_ec == "n":
        quitmsg()
def check_fxe(): #handling editing func, sends over to respective func #check_fxe
    if len(list1) == 0:
        print("List empty. ")
        check_fxe_input = int(input("Using random numbers to fill is recommended. Choosing them yourself is possible as well, input 1 or 2 respectively: "))
        if check_fxe_input == 1:
            fill_rndm()
        elif check_fxe_input == 2:
            fill_uin()
        else:
            invalidinputmsg()
    else:
        edit()

def fill_rndm(): #fills list w random numbers fill_rndm
    for i in range(25):
        x = random.randint(1, 99)
        list1.append(x)
    check_fxe()
def fill_uin(): #uses input to fill list fill_uin
    listlen = int(input("Input length of list: "))
    if listlen < 0:
        invalidinputmsg()
    elif listlen == 0:
        check_fxe()
    else:
        for i in range(listlen):
            list1.append(int(input("Input number at index ")))
        check_fxe()

def edit(): #first editing func, sends over to respective func edit
    print("List: " , list1)
    edit_input = int(input("Add/Remove/Clear/Cancel (1/2/3/4)"))
    if edit_input == 1:
        edit_add()
    elif edit_input == 2:
        edit_remove()
    elif edit_input == 3:
        edit_clear()
    else:
        pass
def edit_add(): #editing func for adding numbers (input) edit_add
    na = int(input("Input number to add: ")) 
    list1.append(na)
    check_fxe()
def edit_remove(): #editing func for removing numbers, (last number) edit_remove
    list1.pop(len(list1) - 1)
    check_fxe()
def edit_clear(): #editing func for clearing edit_clear
    list1.clear()
    check_fxe()

start()
