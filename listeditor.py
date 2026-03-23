import random

print("You can freely interact with a list using this program. Input 1 for viewing the list, and 2 for editing.")
print("By inputting quit, you will always quit the progam, safely.")

userinput = input("Input here: ")

list1 = []

def invalidinputmsg():
    print("Invalid input. ")

def quitmsg():
    print("Exiting program... ")

def start():
    print("Starting... ")
    checkfunc()


def checkfunc():
    if userinput == "1":
        func1()
    elif userinput == "2":
        func2()
    elif userinput == "quit":
        quitmsg()
    else:
        invalidinputmsg()

def func1():
    print(list1)
    func1_ec = input("Would you like to edit this list? (y/n): ")
    if func1_ec == "y":
        func2()
    elif func1_ec == "n":
        quitmsg()

def func2():
    if len(list1) == 0:
        print("List empty. ")
        func2_input = int(input("Using random numbers to fill is recommended. Choosing them yourself is possible as well, input 1 or 2 respectively: "))
        if func2_input == 1:
            fillfunc1()
        elif func2_input == 2:
            fillfunc2()
        else:
            invalidinputmsg()
    else:
        editfunc()

def fillfunc1():
    for i in range(25):
        x = random.randint(1, 99)
        list1.append(x)
    print(list1)
    editqfunc()


def fillfunc2():
    listlen = int(input("Input length of list: "))
    if listlen < 0:
        invalidinputmsg()
    elif listlen == 0:
        func2()
    else:
        for i in range(listlen):
            list1.append(int(input("Input number at index ")))
        func2()

def editfunc():
    print("List: " , list1)
    editfunc_input = int(input("Add/Remove/Clear/Cancel (1/2/3/4)"))
    if editfunc_input == 1:
        editfunc_add()
    elif editfunc_input == 2:
        editfunc_remove()
    elif editfunc_input == 3:
        editfunc_clear()
    else:
        pass

def editfunc_add():
    na = int(input("Input number to add: ")) 
    list1.append(na)
    func2()

def editfunc_remove():
    list1.pop(len(list1) - 1)
    func2()


def editfunc_clear():
    list1.clear()
    func2()

def editqfunc():
    editq = input("Edit/Quit (e/q): ")
    if editq == "q" or editq == "quit":
        quitmsg()
    elif editq == "e":
        func2()
    else:
        invalidinputmsg()






start()
