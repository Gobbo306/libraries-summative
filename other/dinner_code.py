#------------------------------------------------
#other < dinner_code
#Dylan Friesen
#October 30th, 2019
#------------------------------------------------

#--------------Dictionaries--------------------

dinner = {}

#---------------Definitions---------------------

def add_stuff_d(): #used to add stuff to the dinner list
    stop = False
    while stop == False:
        stuff = input("What do you want to add to to your shopping list?").lower()
        if stuff == "stop":
            stop = True
        elif stuff != "stop":
            value = input("How many or description?")
            print("adding", value, stuff)
            dinner[stuff] = value
        
def remove_stuff_d(): #used to remove stuff from the dinner list
    stop = False
    while stop == False:
        stuff = input("What do you want to take off of your shopping list?").lower()
        if stuff == "stop":
            stop = True
        elif stuff != "stop":
            if stuff in dinner:
                print("removing", stuff)
                del dinner[stuff]
            else:
                print("You don't have that on your list")
                
def view_stuff_d():
    for (stuff, value) in dinner.items():
        print("you have", value, stuff, "on your shopping list")
        
#Main
        
def main_d(): #main code for selecting what you want for dinner list
    play = 1
    print("Dinner part of list")
    while play == 1:
        print("")
        print("")
        choice = input("Would you like to Add, Remove, View, or Stop?").lower()
        if choice == "add":
            add_stuff_d()
        elif choice == "remove":
            remove_stuff_d()
        elif choice == "view":
            view_stuff_d()
        elif choice == "stop":
            play = 0
            print ("Onto Supper")
        else:
            ("Sorry, I didn't understand that.")