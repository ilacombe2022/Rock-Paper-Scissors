import random

def choose():
    choice = input("Shall we get started? [yes/no]: ").lower().strip()
    if choice == "yes":
        return choice
    elif choice == "no":
        print("We understand, thanks anyways.")
        exit()
    else:
        print("That's not the answer we're looking for.")
        choose()

def difficulty():
    print("Choose your difficulty:")
    print("Best of 1")
    print("Best of 3")
    print("Best of 5")

    diff = int(input("\n[1/3/5]: "))
    if diff == 1:
        bestOfOne(1)
    elif diff == 3:
        bestOfThree(2)
    elif diff == 5:
        bestOfFive(3)
    else:
        print("We do not provide that difficulty.\n")
        return difficulty()

def winner(u,c):
    print("\nYou beat Al!")
    print("Final Score: %d - %d" % (u, c))
    print("Number of Rounds: %d" % (round - 1))

def loser(u, c):
    print("You lost to Al.")
    print("Final Score: %d - %d" % (u, c))
    print("Number of Rounds: %d" % (round - 1))

def bestOfOne(num):
    print("Rule: \tOne round of Rock-Paper-Scissors.")
    print("\t\tFirst person to score 1 point win!")

    startGame()
    introCPU()
    playGame(num)

def bestOfThree(num):
    print("Rule: \tThree rounds of Rock-Paper-Scissors.")
    print("\t\tFirst person to score 2 points win!")

    startGame()
    introCPU()
    playGame(num)

def bestOfFive(num):
    print("Rule: \tFive rounds of Rock-Paper-Scissors.")
    print("\t\tFirst person to score 3 points win!")

    startGame()
    introCPU()
    playGame(num)

def playGame(match):
    userPoint = 0
    computerPoint = 0
    round = 1

    while userPoint < match and computerPoint < match:
        user = input("\nRound #%d, what will you choose? [rock/paper/scissors]: " % round)
        computer = random.randrange(1, 4, 1)
        if user == "rock" or user == "paper" or user == "scissors":
            if user == "rock" and computer == 1:
                print("You chose rock and Al chose rock! Tie!")
                print("Score: %d - %d" % (userPoint, computerPoint))
                round = round + 1
            elif user == "rock" and computer == 2:
                print("You chose rock and Al chose paper! Al gets a point!")
                computerPoint = computerPoint + 1
                print("Score: %d - %d" % (userPoint, computerPoint))
                round = round + 1
            elif user == "rock" and computer == 3:
                print("You chose rock and Al chose scissors! You get a point!")
                userPoint = userPoint + 1
                print("Score: %d - %d" % (userPoint, computerPoint))
                round = round + 1
            elif user == "paper" and computer == 1:
                print("You chose paper and Al chose rock! You gets a point!")
                userPoint = userPoint + 1
                print("Score: %d - %d" % (userPoint, computerPoint))
                round = round + 1
            elif user == "paper" and computer == 2:
                print("You chose paper and Al chose paper! Tie!")
                print("Score: %d - %d" % (userPoint, computerPoint))
                round = round + 1
            elif user == "paper" and computer == 3:
                print("You chose paper and Al chose scissors! Al gets a point!")
                computerPoint = computerPoint + 1
                print("Score: %d - %d" % (userPoint, computerPoint))
                round = round + 1
            elif user == "scissors" and computer == 1:
                print("You chose scissors and Al chose rock! Al gets a point!")
                computerPoint = computerPoint + 1
                print("Score: %d - %d" % (userPoint, computerPoint))
                round = round + 1
            elif user == "scissors" and computer == 2:
                print("You chose scissors and Al chose paper! You get a point!")
                userPoint = userPoint + 1
                print("Score: %d - %d" % (userPoint, computerPoint))
                round = round + 1
            elif user == "scissors" and computer == 3:
                print("You chose scissors and Al chose scissors! Tie!")
                print("Score: %d - %d" % (userPoint, computerPoint))
                round = round + 1
        else:
            print("Not an option, time to start over.\n")
            playGame(match)

    if userPoint == match:
        print("\nYou beat Al!")
        print("Final Score: %d - %d" % (userPoint, computerPoint))
        print("Number of Rounds: %d" % (round - 1))
        playAgain()
    elif computerPoint == match:
        print("You lost to Al.")
        print("Final Score: %d - %d" % (userPoint, computerPoint))
        print("Number of Rounds: %d" % (round - 1))
        playAgain()


def playAgain():
    again = input("\nWould you like to play again?[yes/no]: ").lower().strip()

    if again == "yes":
        difficulty()
    elif again == "no":
        print("Thanks for playing!")
        exit()
    else:
        print("We are trying to ask if you would like to play again?")
        playAgain()

def startGame():
    start = input("\nAre you ready to play against the CPU? [yes/no]: ").lower().strip()

    if start == "yes":
        return start
    elif start == "no":
        print("Oh! You've changed your mind? That's fine.")
        exit()
    else:
        print("That choice isn't available.\n")
        startGame()

def introCPU():
    print("Say hello to Al! He will be you opponent!")
    print("NOTE: Make sure you spell each word correctly, otherwise, rounds and scores will be reset!")
    print("HAVE FUN!")

if __name__ == '__main__':
    print("Let's play Rock-Paper-Scissors!")
    print("Created by Isaac Lacombe\n")

    choose()
    difficulty()