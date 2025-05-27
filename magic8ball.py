#Ella
#Init
#ask user question
#randomly select and display response
#create loop to ask again
import random
#Functions
magic_list = ["yes", "no", "Most likely", "certainly", "Cannot predict now", "Ask again later", "Don’t count on it", "My sources say no", "Outlook not so good", "Signs point to yes" , "Without a doubt" , "maybe", "not sure", "probaly not", "of course", "ill get back on that", "50/50"]
#Main
while True:
    print("Welcome player to magic 8 ball!")
    ball = input("Please ask a yes or no question")
    if ball.endswith("?"):
        print(random.choice(magic_list))
    else:
        print("Please enter a QUESTION.")
    again = input("Would you like to play again")
    if again == "yes":
        print("Restarting...")
    elif again == "no":
        break
