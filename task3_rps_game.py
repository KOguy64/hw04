from random import randint
draws = 0
wins = 0
losses = 0

i_map = {0:"rock",1:"paper",2:"scissors"}

while True:
    c = input("rock, paper, scissors or q to quit: ")
    comp = i_map[randint(0,2)]
    if c == "q":
        break
    elif c not in ["rock", "paper", "scissors"]:
        print("Invalid choice")
        continue

    print(f"Computer: {comp}")
    if c == comp:
        print("It's a draw!")
        draws += 1
    elif (c == "rock" and comp == "scissors") or (c == "paper" and comp == "rock") or (c == "scissors" and comp == "paper"):
        print("You win!")
        wins += 1
    elif (comp == "rock" and c == "scissors") or (comp == "paper" and c == "rock") or (comp == "scissors" and c == "paper"):
        print("Computer wins!")
        losses += 1

print(f"You won {wins}, the computer won {losses}, draws {draws}")