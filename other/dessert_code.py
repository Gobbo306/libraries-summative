#------------------------------------------------
#other < dessert_code
#Dylan Friesen
#October 30th, 2019
#------------------------------------------------

#--------------Dictionaries--------------------

dessert_list = ["ice cream", "pie", "cheese cake"]

#-------------Definitions----------------------

def dessert(): #code for messing around 
    dessert = input("You already have ice cream, pie and cheese cake on your list, is there anything you would like to add?")
    if dessert == "yes":
        new_dessert = input("What would you like to add?")
        dessert_list.append(new_dessert)
    elif dessert == "no":
        dessert_remove = input("what would you like to remove?").lower()
        if dessert_remove == "ice cream":
            dessert_list.remove("ice cream")
        elif dessert_remove == "pie":
            dessert_list.remove("pie")
        elif dessert_remove == "cheese cake":
            dessert_list.remove("cheese cake")
        else:
            print("You cant remove that, deal with it")
        print(dessert_list)