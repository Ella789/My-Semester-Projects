#Ella Leung
#Oct 15, 2024
#Init
#Functions
#Choose your superhero
def manorwoman():
    gender = input("Man or woman?:")
    if gender == "woman":
        color = input ("black or green?:")
        if color == "black" :
            a = input("cat or widow?:")
            if a == "cat":
                print("you are cat woman!")
            elif a == "widow":
                print("you are black widow!")
                if color == "green":
                    a = input("anger or galaxy?:")
                    if a == "anger":
                        print("you are she-hulk!")
                    elif a == "galaxy":
                        print("you are Gamora!")
    elif gender == "man":
        color = input ("red or black?:")
        if color == "red":
            a = input("web or metal?:")
            if a == "web":
                print("you are spiderman!")
            elif a == "metal":
                print("you are ironman!")
        elif color == "black":
            a = input("bat or claws?:")
            if a == "bat":
                print("you are batman!")
            elif a == "claws":
                print("you are blackpanter!")



#Main
manorwoman()
