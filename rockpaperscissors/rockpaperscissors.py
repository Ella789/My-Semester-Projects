#ella
#1/8/25
#Rock Paper Scissors
print("Welcome to Rock, Paper, Scissors")
wins = 0
losses = 0
ties = 0
#Player's Choice
while True:
    print("""Please select one of the three options:
        Rock
        Paper
        Scissors """)
    player =(input("selection:"))
    #Computer's Choice"
    import random
    computer = random.randint(1,3)
    if computer == 1:
        computer = "rock"
        print("computer chose rock")
    elif computer == 2:
        computer = "paper"
        print("computer chose paper")
    elif computer == 3:
        computer = "scissors"
        print("computer chose scissors")
    #Determine the outcome
    if player == "rock" and computer == "paper":
        print("computer won!")
        losses = losses + 1
    elif player == "rock" and computer == "scissors":
        print("you won!")
        wins = wins + 1
    elif player == "rock" and computer == "rock":
        print("tie game!")
        ties = ties + 1
    elif player == "paper" and computer == "paper":
        print("tie game!")
        ties = ties + 1
    elif player == "paper" and computer == "scissors":
        print("computer won!")
        losses = losses + 1
    elif player == "paper" and computer == "rock":
        print("you won!")
        wins = wins + 1
    elif player == "scissors" and computer == "paper":
        print("you won!")
        wins = wins + 1
    elif player == "scissors" and computer == "scissors":
        print("tie game!")
        ties = ties + 1
    elif player == "scissors" and computer == "rock":
        print("computer won!")
        losses = losses + 1
    print(wins)
    print(losses)
    print(ties)
    #Ask the player if they want to continue:
    again = input("Would you like to play again")
    if again == "yes":
        print("Restarting...")
    elif playagain == "no":
        break
    # = get the value of
    # == is equal to
