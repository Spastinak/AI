

binAmount = [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0]

playing = True

playerOne = True

messageCode = 0



        
while(playing):

    message= ""
    if playerOne and messageCode == 0:
        message = "\nPlayer one's turn.\n"
    elif not(playerOne) and messageCode == 0:
        message = "\nPlayer two's turn.\n"
    elif messageCode == -2:
        message = "Invalid input. Try again"
    elif messageCode == -1:
        message = "Choose a non empty bin idiot."
    print(message)

    if not(playerOne):
        print("        f    e    d    c    b    a")
    else:
        print(" ")
    messageCode = 0

    i = 0
    # convert the binAmount to strings
    for element in binAmount: 
        binAmount[i] = int(binAmount[i]) # remove extra spaces
        if int(binAmount[i]) < 10:
            binAmount[i] = " " + str(binAmount[i]) # if binAmount is a single diget 
        else :
            binAmount[i] = str(binAmount[i]) # double diget
        i += 1
    # end of the for loop


    print("+----+----+----+----+----+----+----+----+")
    print("|    | "+ binAmount[12] +" | "+ binAmount[11] +" | "+ binAmount[10] +" | "+ binAmount[9] +" | "+ binAmount[8] +" | "+ binAmount[7] +" |    |")
    print("| "+ binAmount[13] +" |----+----+----+----+----+----| "+ binAmount[6] +" |")
    print("|    | "+ binAmount[0] +" | "+ binAmount[1] +" | "+ binAmount[2] +" | "+ binAmount[3] +" | "+ binAmount[4] +" | "+ binAmount[5] +" |    |")
    print("+----+----+----+----+----+----+----+----+")

    if playerOne:
        print("        f    e    d    c    b    a")
    else:
        print(" ")

    userInput = input("Enter a letter to choose a bin or enter 'QUIT' to quit the game: ")

    # why is there no switch case in python? 
    if userInput == "QUIT":
        playing = False
    elif playerOne and userInput == "a":
        chosenBin = 5
    elif playerOne and userInput == "b":
        chosenBin = 4
    elif playerOne and userInput == "c":
        chosenBin = 3
    elif playerOne and userInput == "d":
        chosenBin = 2
    elif playerOne and userInput == "e":
        chosenBin = 1
    elif playerOne and userInput == "f":
        chosenBin = 0
    elif not(playerOne) and userInput == "a":
        chosenBin = 7
    elif not(playerOne) and userInput == "b":
        chosenBin = 8
    elif not(playerOne) and userInput == "c":
        chosenBin = 9
    elif not(playerOne) and userInput == "d":
        chosenBin = 10
    elif not(playerOne) and userInput == "e":
        chosenBin = 11
    elif not(playerOne) and userInput == "f":
        chosenBin = 12
    else:
        chosenBin = -2
        messageCode = -2 # invalid input
   

    if int(chosenBin) >= 0:
        giveawayPile = binAmount[chosenBin]
        binAmount[chosenBin] = 0
        if int(giveawayPile) > 0:
            playerOne = not(playerOne)
        else:
            messageCode = -1 # empty bin was chosen


# end of while loop