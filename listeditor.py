import random

def start(): #start program
    check_fuin()

def startmsg(): #outputs start program msg
    print("Starting program... ")
def quitmsg(): #outputs quit program msg
    print("Exiting program... ")
def invalidinputmsg(): #outputs invalid input message
    print("Invalid input. ")

def check_fuin(): #first function that handles input at start
    if uin == "view" or uin == "v" or uin == "1":
        view()
    elif uin == "edit" or uin == "e" or uin == "2":
        check_fxe()
    elif uin == "quit" or uin == "q" or uin == "3":
        quitmsg()
    else:
        invalidinputmsg()

def view(): #for viewing, sends to fill/edit func if needed
    print(list1)
    view_uin = input("Would you like to edit this list? (yes/no): ")
    if view_uin == "yes" or view_uin == "y" or view_uin == "1":
        check_fxe()
    elif view_uin == "no" or view_uin == "n" or view_uin == "2" or view_uin == "quit" or view_uin == "q":
        quitmsg()
def check_fxe(): #handles filling/editing func, sends over to respective func
    if len(list1) == 0:
        print("List empty. ")
        check_fxe_uin = input("Using random numbers to fill is recommended. Choosing them yourself is possible as well, input random or choose respectively: ")
        if check_fxe_uin == "random" or check_fxe_uin == "rndm" or check_fxe_uin == "r" or check_fxe_uin == "1":
            fill_rndm()
        elif check_fxe_uin == "choose" or check_fxe_uin == "c" or check_fxe_uin == "2":
            fill_uin()
        elif check_fxe_uin == "quit" or check_fxe_uin == "q":
            quitmsg()
        else:
            invalidinputmsg()
    else:
        edit()

def fill_rndm(): #fills list w random numbers
    for i in range(25):
        x = random.randint(1, 99)
        list1.append(x)
    check_fxe()
def fill_uin(): #uses input to fill list
    listlen = int(input("Input length of list: "))
    if listlen < 0:
        print("Length of list must be positive. ")
        fill_uin()
    elif listlen == 0:
        check_fxe()
    else:
        for i in range(listlen):
            list1.append(int(input("Input number at index ")))
        check_fxe()

def edit(): #first editing func, sends over to respective editing func
    print("List: " , list1)
    edit_uin = input("Choose whether to add, remove, or clear: ")
    if edit_uin == "add" or edit_uin == "a" or edit_uin == "1":
        edit_add()
    elif edit_uin == "remove" or edit_uin == "r" or edit_uin == "2":
        edit_remove()
    elif edit_uin == "clear" or edit_uin == "c" or edit_uin == "3":
        edit_clear()
    elif edit_uin == "quit" or edit_uin == "q":
        quitmsg()
    else:
        invalidinputmsg()
def edit_add(): #editing func for adding numbers (input)
    n = int(input("Input number to add: ")) 
    list1.append(n)
    check_fxe()
def edit_remove(): #editing func for removing numbers (last number)
    list1.pop(len(list1) - 1)
    check_fxe()
def edit_clear(): #editing func for clearing
    list1.clear()
    check_fxe()

startmsg()

print("You can freely interact with a list using this program. Input view to view the list or edit to edit. ")
print("All input fields are intuitive. Simply input the command name, or its number. ")
print("Input quit at any time to exit program. ")

uin = input("Input here: ")
list1 = []

start()

