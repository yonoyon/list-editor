# import stuff
import random
import sys

# define list
list1 = []

# generic messages
def startmsg(): 
    print("Starting program... ")
    print("You can freely interact with a list using this program. Input help for a list of possible commands. ")
def invalidinputmsg():
    print("Invalid Input. Try help?")
def errormsg():
    print("An error has occured, possible invalid input. ")
# other messages
def helph():
    print("Commands for the main menu: view, edit, fill, cancel, help,  quit. Input using numbers is possible, from 1 onwards. ")
    print("Commands for the editor: add, remove, fill, clear, cancel, help, return, quit. ")
def printlist():
    print("Your List: ", list1)

# main menu functions
def view():
    printlist()
def edit():
    printlist()
    while True:
        editor_user_input= input("Input editor command: ").strip().lower()
        if editor_user_input in editor_command:
            editor_command[editor_user_input]()
        else:
            invalidinputmsg()

# functions used by main menu and editor
def fill():
    list1.clear()
    for i in range(25):
        x = random.randint(1, 99)
        list1.append(x)
    printlist()
def cancel():
    pass
def quitq():
    printlist()
    print("Exiting program. ")
    sys.exit()

# editor functions
def editor_add():
    try:
        n = int(input("Input number to add: "))
        list1.append(n)
    except:
        errormsg()
    printlist()
def editor_remove():
    try:
        list1.pop(len(list1) - 1)
    except:
        errormsg()
    printlist()
def editor_clear():
    list1.clear()
def editor_returnr():
    whilefunc()

# handles input for main menu and sends over to editor
function = edit
def commandcheck():
    user_input = input("Input command: ").strip().lower()
    if user_input in command and command[user_input] == function:
        command[user_input]()
    elif user_input in command:
        command[user_input]()
    else:
        invalidinputmsg()
   
# loops it all
def whilefunc():
    while True:
        commandcheck()

# dictionaries
command = {
    "view" : view,
    "v" : view,
    "1" : view,
    "edit" : edit,
    "e" : edit,
    "2" : edit,
    "fill" : fill,
    "f" : fill,
    "3" : fill,
    "cancel" : cancel,
    "c" : cancel,
    "4" : cancel,
    "help" : helph,
    "h" : helph,
    "5" : helph,
    "quit" : quitq,
    "q" : quitq,
    "6" : quitq,
}
editor_command = {
    "add" : editor_add,
    "a" : editor_add,
    "1" : editor_add,
    "remove" : editor_remove,
    "r" : editor_remove,
    "2" : editor_remove,
    "fill" : fill,
    "f" : fill,
    "3" : fill,
    "clear" : editor_clear,
    "cl" : editor_clear,
    "4" : editor_clear,
    "cancel" : cancel,
    "c" : cancel,
    "5" : cancel,
    "help" : helph,
    "h" : helph,
    "6" : helph,
    "return" : editor_returnr,
    "r" : editor_returnr,
    "7" : editor_returnr,
    "quit": quitq,
    "q" : quitq,
    "8" : quitq,
}

# start program
startmsg()
whilefunc()
