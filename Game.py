from time import sleep
import random
import sys


print("\n==============================================\n")
print(f"Welcome to Dice Cricket! The rules are as follow: \n\n*Players Must Try and Attempt to Score as High as Possible \n*Each Roll is Added to a Players Total \n*Do Not Roll a 5 or the Game is Over ")
print("\n==============================================\n")

def playagain():
    try:
        play = input("\nWould you like to play again?: Y/N \n")
        if play.lower() == 'n':
            print("\n==================\n")
            print("Quitting Game...")
            print("\n==================")
            sleep(.5)
            return(False)
        elif play.lower() == 'y':
            print("\n==================")
            print("\nRestarting Game...\n")
            print("==================")
            sleep(1)
            dicecricket()
        else:
            print("Enter Y or N \n")
    except:
            print("Error")
    

def dicecricket():

    player_1_total = 0
    player_2_total = 0
    wait_press = 1
    i = 1
    while True:
        try:
            print(f"\nPlayer {i} is Currently Playing\n")

            if i == 1:
                keypress = input(f"Player {i} Ready? Y/N: \n")

                if keypress.lower() == 'y':
                    number = random.randrange(1,6)
                    print("\nRolling the Dice...")
                    sleep(1)
                    print(f"Dice Roll: {number}")
                    sleep(1)
                           
                    if number == 5:
                        print("\nGame Over!\n")

                        if player_1_total > player_2_total:
                            print("\nPlayer 1 Wins!\n")
                            print(f"==========================\nPlayer 1 Total Score: {player_1_total} \nPlayer 2 Total: {player_2_total} \n==========================")
                            break
                        elif player_1_total < player_2_total:
                            print("\nPlayer 2 Wins!\n")
                            print(f"==========================\nPlayer 1 Total Score: {player_1_total} \nPlayer 2 Total: {player_2_total} \n==========================")
                            break
                        elif player_1_total == 0 and player_2_total == 0:
                            print("First Random Number Drawn was 5!")
                            break
                        elif player_1_total == player_2_total:
                            print("\nPlayer 1 and 2 Draw!\n")
                            print(f"==========================\nPlayer 1 Total Score: {player_1_total} \nPlayer 2 Total: {player_2_total} \n==========================")
                            break
                               
                    else:
                        player_1_total = player_1_total + number
                        i = 2
                           
                elif keypress.lower() == 'n':

                    if wait_press < 5:
                        print("Waiting...")
                        wait_press = wait_press + 1
                        sleep(2)
                    elif wait_press >=5:
                        print("\nI've Waited Long Enough! Come Back When Your Ready!\n")
                        return
                    else:
                        print("Error")
                else:
                    print("Enter a yes or no")
                                   
            elif i == 2:
                keypress = input(f"Player {i} Ready? Y/N: \n")
                   
                if keypress.lower() == 'y':
                    number = random.randrange(1,6)
                    print("\nRolling the Dice...")
                    sleep(1)
                    print(f"Dice Roll: {number}")
                    sleep(1)
                           
                    if number == 5:
                        print("\nGame Over!\n")

                        if player_1_total > player_2_total:
                            print("\nPlayer 1 Wins!\n")
                            print(f"==========================\nPlayer 1 Total Score: {player_1_total} \nPlayer 2 Total: {player_2_total} \n==========================")
                            break
                        elif player_1_total < player_2_total:
                            print("\nPlayer 2 Wins!\n")
                            print(f"==========================\nPlayer 1 Total Score: {player_1_total} \nPlayer 2 Total: {player_2_total} \n==========================")
                            break
                        elif player_1_total == 0 and player_2_total == 0:
                            print("First Random Number Drawn was 5!")
                            break
                        elif player_1_total == player_2_total:
                            print("\nPlayer 1 and 2 Draw!\n")
                            print(f"==========================\nPlayer 1 Total Score: {player_1_total} \nPlayer 2 Total: {player_2_total} \n==========================")
                            break
                                
                        
                                   
                    else:
                        player_2_total = player_2_total + number
                        i = 1
                elif keypress.lower() == 'n':
                    
                    if wait_press < 5:
                        print("Waiting...")
                        wait_press = wait_press + 1
                        sleep(2)
                    elif wait_press >=5:
                        print("\nI've Waited Long Enough! Come Back When Your Ready!\n")
                        return
                    else:
                        print("Error")
                else:
                    print("Enter a yes or no")
                   
            else:
                print("Error")

        except:
            print("Error")
    playagain()
                
dicecricket()





    
