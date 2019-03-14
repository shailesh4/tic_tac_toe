

starting_game = True
inputs = [" "," "," "," "," "," "," "," "," "]
counter = 0


def empty_inputs():
    global inputs
    inputs = [" "," "," "," "," "," "," "," "," "]
    global counter
    counter = 0


def show_board():

    for N in range(1,100):                                        # Prints a Line 100 times to clear the screen
        print()

    print(" " + inputs[6] + " | " + inputs[7] + " | " + inputs[8]) #The Upper Row
    print("-----------")

    print(" " + inputs[3] + " | " + inputs[4] + " | " + inputs[5]) #The Middle Row
    print("-----------")

    print(" " + inputs[0] + " | " + inputs[1] + " | " + inputs[2]) # The Lower Row

def check_board():
    check_for_X = 'X'
    check_for_0 = '0'
    
    for i in range(0,3):                                        #Checks for Horizontal lines
        if (inputs[0+ i*3] == check_for_X and inputs[1+ i*3 ] == check_for_X and inputs[2+ i*3 ] == check_for_X) or (inputs[0+ i*3] == check_for_0 and inputs[1+ i*3 ] == check_for_0 and inputs[2+ i*3 ] == check_for_0) :
            if(inputs[0+ i*3 ] == check_for_X):
                print("X wins this game.")
            else:
                print("0 wins this game.")
            return True


    for i in range(0,3):                                        # Checks for Vertical lines
        if (inputs[0 + i] == check_for_X and inputs[3 +i ] == check_for_X and inputs[6 +i ] == check_for_X) or (inputs[0 + i] == check_for_0 and inputs[3 +i ] == check_for_0 and inputs[6 +i ] == check_for_0) :
            if(inputs[0+ i ] == check_for_X):
                print("X wins this game.")
            else:
                print("0 wins this game.")
            return True


    if (inputs[0] == check_for_X and inputs[4] == check_for_X and inputs[8] == check_for_X) or (inputs[0] == check_for_0 and inputs[4] == check_for_0 and inputs[8] == check_for_0) :
        if inputs[0] == check_for_X:
            print("X wins this game.")
        else:
            print("0 wins this game.")
        return True

    if (inputs[2] == check_for_X and inputs[4] == check_for_X and inputs[6] == check_for_X) or (inputs[2] == check_for_0 and inputs[4] == check_for_0 and inputs[6] == check_for_0) :
        if inputs[2] == check_for_X:
            print("X wins this game.")
        else:
            print("0 wins this game.")
        return True

    return False
            






while True:
    if(starting_game):                                             #Will only start the first time you open a game and explains the game.
        empty_inputs()
        print("The Tic Tae game has 9 slots and are modeled like a num pad with 1 at the bottom. Write a number to put the symbol at that place.")
        play = input("Do you want to play Tic Tac Toe ? (Y/N)  : ")
        starting_game = False
    if play.lower() == 'y':                                         #Checks if the player wants to play the game

        try:
            num_pos = int(input("(press 0 to exit). Write a number between 1 to 9 : "))
            if num_pos in range(1,10):
                if inputs[num_pos-1] == " ":                         #Checks if the place is empty or not
                    if counter%2 == 0:                              #Checks odd or even placement
                        inputs[num_pos-1] = 'X'
                        counter+=1                        
                    else:
                        inputs[num_pos-1] = '0'
                        counter +=1
                    show_board()
                    finished_game = check_board()
                    if finished_game == True:
                        play = input("Would you like to play again? (y/n) : ")
                        if play.lower() == 'y':
                            starting_game = True
                            continue
                        else:
                            print("Thanks for checking this game out!!")
                            exit()


                else:
                    print("The {} Field is already in use.".format(num_pos))
                    continue


            elif num_pos == 0:
                exit()
            else:
                print("The number is out of range. Please Try again. ")
                continue
        except ValueError:
            print("That's not an int. Please enter a valid input.")
            continue


    else:
        print("Thanks for checking this game out!!")
        exit()

