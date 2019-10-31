#------------------------------------------------
#other < breakfast_code
#Dylan Friesen
#October 30th, 2019
#------------------------------------------------

#---------------Dictionaries-------------------

breakfast = {}

#------------------Definitions-----------------

def add_stuff_b(): #used to add stuff to the breakfast list
    stop = False
    while stop == False:
        stuff = input("What do you want to add to to your shopping list?").lower()
        if stuff == "stop":
            stop = True
        elif stuff != "stop":
            value = input("How many or description?")
            print("adding", value, stuff)
            breakfast[stuff] = value
        
def remove_stuff_b(): #remove stuff from breakfast list
    stop = False
    while stop == False:
        stuff = input("What do you want to take off of your shopping list?").lower()
        if stuff == "stop":
            stop = True
        elif stuff != "stop":
            if stuff in breakfast:
                print("removing", stuff)
                del breakfast[stuff]
            else:
                print("You don't have that on your list")
                
def view_stuff_b():
    for (stuff, value) in breakfast.items():
        print("you have", value, stuff, "on your shopping list")
        
#Main

def main_b(): #main code for choosing what you wan to put in your breakfast list
    play = 1
    print("Breakfast part of list")
    while play == 1:
        print("")
        print("")
        choice = input("Would you like to Add, Remove, View, or Stop?").lower()
        if choice == "add":
            add_stuff_b()
        elif choice == "remove":
            remove_stuff_b()
        elif choice == "view":
            view_stuff_b()
        elif choice == "stop":
            play = 0
            print ("Onto Dinner")
        else:
            ("Sorry, I didn't understand that.")