#Rom-com movie list
#Init
movieList = []
print("Welcome to my Theme List Organization")
while True:
    try:
        print("Please select one of the following options")
        print("1. View \n2.Add \n3. Remove \n4.Quit")
        #Collect User Choice
        option = input("Select a number between 1-4:")
        option = int(option)
        #Process Information
        if option ==1:
            print("Here is your these list:")
            print(movieList)
        elif option == 2:
            addItem = input("What would you like to add?:")
            movieList.append(addItem)
            print("Successfully added" + addItem)

        elif option == 3:
            remItem = input("What would you like to remove?:")
            movieList.remove(remItem)
            print("Successfully removed" + remItem)
        else:
            print("Thank you for using Theme List organizer!")
            print("Please rate us 5 stars on the App Store")

            break
    except:
        print("ERROR: Please enter a NUMBER")
