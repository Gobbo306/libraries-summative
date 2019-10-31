#------------------------------------------------
#other < supper_code
#Dylan Friesen
#October 30th, 2019
#------------------------------------------------

#--------------Dictionaries--------------------

supper = {}

#------------------Definitions-----------------

def add_stuff_s(): #used to add stuff to the supper list
    stop = False
    while stop == False:
        stuff = input("What do you want to add to to your shopping list?").lower()
        if stuff == "stop":
            stop = True
        elif stuff != "stop":
            value = input("How many or description?")
            print("adding", value, stuff)
            supper[stuff] = value
        
def remove_stuff_s(): #used to remove stuff in the supper list
    stop = False
    while stop == False:
        stuff = input("What do you want to take off of your shopping list?").lower()
        if stuff == "stop":
            stop = True
        elif stuff != "stop":
            if stuff in supper:
                print("removing", stuff)
                del supper[stuff]
            else:
                print("You don't have that on your list")
                
def view_stuff_s():
    for (stuff, value) in supper.items():
        print("you have", value, stuff, "on your shopping list")
        
#Main        
        
def main_s(): #main code specified for just deciding what it wanted on the supper list
    play = 1
    print("Supper part of list")
    while play == 1:
        print("")
        print("")
        choice = input("Would you like to Add, Remove, View, or Stop?").lower()
        if choice == "add":
            add_stuff_s()
        elif choice == "remove":
            remove_stuff_s()
        elif choice == "view":
            view_stuff_s()
        elif choice == "stop":
            play = 0
            print ("Onto Desserts")
        else:
            ("Sorry, I didn't understand that.")