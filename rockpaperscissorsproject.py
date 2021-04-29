import random

aiWinCount = 0
userWinCount = 0

while True:
    userAction = input("Enter your choice: rock, paper, scissors or done.\n")
    print("Player chooses:", userAction)

    options = ["rock", "paper","scissors"]
    if userAction == "done":
        print("Thanks for playing!")
        break
    else:
        aiAction = random.choice(options)
        print("Computer chooses:", aiAction)

    if aiAction == userAction:
        print("Draw!")
    elif aiAction == "rock" and userAction == "paper":
        print("Player Wins this Round!")
        userWinCount += 1
    elif aiAction == "rock" and userAction == "scissors":
        print("Computer Wins this Round!")
        aiWinCount += 1
    elif aiAction == "paper" and userAction == "rock":
        print("Computer Wins this Round!")
        aiWinCount += 1
    elif aiAction == "paper" and userAction == "scissors":
        print("Player Wins this Round!")
        userWinCount += 1
    elif aiAction == "scissors" and userAction == "rock":
        print("Player Wins this Round!")
        userWinCount += 1
    elif aiAction == "scissors" and userAction == "paper":
        print("Computer Wins this Round!")
        aiWinCount += 1

    print("Rounds Won: Player", userWinCount)
    print("Rounds Won: Computer", aiWinCount)
              
if aiWinCount > userWinCount:
    print("Computer Wins!\n")
else:
    print("Player Wins!\n")

    


