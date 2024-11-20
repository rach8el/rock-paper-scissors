# welcoming player and giving instructions
print("Welcome Rachael and other\n When asked for your choice please enter 'r', 'p', or 's'")

# getting players input 
playerOneInput = input("player one select: r, p, or s; ")
playerTwoInput = input("player two select: r, p, or s; ")

# compare player input to determine result, Either player1 wins, player2 wins or its a tie
if playerOneInput == "s": 
    if playerTwoInput == "s":
        print("tie")
    if playerTwoInput == "r":
        print("p2 wins")
    if playerTwoInput == "p":
        print("p1 wins")

if playerOneInput == "r":
    if playerTwoInput == "r":
        print("tie")
    if playerTwoInput == "s":
        print("p1 wins")
    if playerTwoInput == "p":
        print("p2 wins")

if playerOneInput == "p":
    if playerTwoInput == "p":
        print("tie")
    if playerTwoInput == "r":
        print("p1 wins")
    if playerTwoInput == "s":
        print("p2 wins")