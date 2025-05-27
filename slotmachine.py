#Indroduction
#Ask player, spin or quit
# Randomly pull images from list
# Advice: Make sure you store these in a
# Display three images
# Determine outcome if elif else
income = 50
import random
symbol_list = ["♥", "♦", "♠", "♣", "☆", "7"]
print ("Welcome to the casino slot machine!")
while True:
    symbol = input("Would you like to take a spin or quit?:")
    if symbol == "spin":
        income = income - 1
        slotone = random.choice(symbol_list)
        slottwo = random.choice(symbol_list)
        slotthree = random.choice(symbol_list)
        print (slotone + slottwo + slotthree)
        if slotone == "7" and slottwo == "7" and slotthree == "7":
            print("You have won jackpot!")
        elif slotone == slottwo and slottwo == slotthree:
            print("You won!")
        else:
            print("You lost!")
            if income == 0:
                print("Income is zero.")
                break
    elif symbol == "quit":
        break
