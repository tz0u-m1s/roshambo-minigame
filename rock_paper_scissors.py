from time import sleep
from random import randint
while True:
    game_start=input("Start Playing Rock Paper Scissors? Y/N ")


    if game_start=="Y" or game_start=="y":
        sp_or_mp=input("SinglePlayer or MultiPlayer ? S/M ")
        if sp_or_mp=="S" or sp_or_mp=="s":
            RPS_player_pick=0
            while RPS_player_pick<1 or RPS_player_pick>3:
                
                    print("Starting Game... ")
                    print("1 is Rock")
                    print("2 is Paper")
                    print("3 is Scissors")

                    try:
                        RPS_player_pick=int(input("Pick a number 1-3: "))
                    except ValueError:
                        print("Invalid! try again!")
                        continue


                    if RPS_player_pick==1:
                        print("You picked: Rock")

                    elif RPS_player_pick==2:
                        print("You picked: Paper")

                    elif RPS_player_pick==3:
                        print("You picked: Scissors")

                    elif RPS_player_pick<1 or RPS_player_pick>3:
                        print("Try again!")
                        continue
                    
                    RPS_AI_pick=randint(1,3)

                    if RPS_AI_pick==1:
                        print("AI picked: Rock")

                    elif RPS_AI_pick==2:
                        print("AI picked: Paper")

                    elif RPS_AI_pick==3:
                        print("AI picked: Scissors")


                    if RPS_player_pick==RPS_AI_pick:
                        print("Tie!")
                    elif RPS_player_pick==1 and RPS_AI_pick==3:
                        print("You Win!")
                    elif RPS_player_pick==1 and RPS_AI_pick==2:
                        print("AI Wins!")
                    elif RPS_player_pick==2 and RPS_AI_pick==1:
                        print("You Win!")
                    elif RPS_player_pick==2 and RPS_AI_pick==3:
                        print("AI Wins!")
                    elif RPS_player_pick==3 and RPS_AI_pick==2:
                        print("You Win!")
                    elif RPS_player_pick==3 and RPS_AI_pick==1:
                        print("AI Wins!")

        elif sp_or_mp=="M" or sp_or_mp=="m":
            RPS_player_pick=0
            RPS_player2_pick=0
            print("Starting 2 Player Game... ")
            print("1 is Rock")
            print("2 is Paper")
            print("3 is Scissors")

            while RPS_player_pick<1 or RPS_player_pick>3:
                try:
                    RPS_player_pick=int(input("Player 1, pick a number 1-3: "))
                except ValueError:
                    print("Invalid! try again!")
                    continue


                if RPS_player_pick==1:
                    print("P1:Rock")
                    sleep(2)

                elif RPS_player_pick==2:
                    print("P1:Paper")
                    sleep(2)

                elif RPS_player_pick==3:
                    print("P1:Scissors")
                    sleep(2)

                elif RPS_player_pick<1 or RPS_player_pick>3:
                    print("Try again!")
                    continue
                while RPS_player2_pick<1 or RPS_player2_pick>3:
                    print('\n'*30)
                    print("1 is Rock")
                    print("2 is Paper")
                    print("3 is Scissors")
                    try:
                        RPS_player2_pick=int(input("Player 2, pick a number 1-3: "))
                    except ValueError:
                        print("Invalid! try again!")
                        continue


                    if RPS_player2_pick==1:
                        print("P2:Rock")
                        sleep(2)

                    elif RPS_player2_pick==2:
                        print("P2:Paper")
                        sleep(2)

                    elif RPS_player2_pick==3:
                        print("P2:Scissors")
                        sleep(2)

                    elif RPS_player2_pick<1 or RPS_player2_pick>3:
                        print("Try again!")
                        continue
                    print("\n"*15)
                    print("The results are in! ")
                    sleep(1)
                    if RPS_player_pick==RPS_player2_pick:
                        print("Its a Tie!")
                    elif RPS_player_pick==1 and RPS_player2_pick==3:
                        print("Rock VS Scissors, Player 1 Wins!")
                    elif RPS_player_pick==1 and RPS_player2_pick==2:
                        print("Rock VS Paper, Player 2 Wins!")
                    elif RPS_player_pick==2 and RPS_player2_pick==1:
                        print("Paper VS Rock, Player 1 Wins!")
                    elif RPS_player_pick==2 and RPS_player2_pick==3:
                        print("Paper VS Scissors, Player 2 Wins!")
                    elif RPS_player_pick==3 and RPS_player2_pick==2:
                        print("Scissors VS Paper, Player 1 Wins!")
                    elif RPS_player_pick==3 and RPS_player2_pick==1:
                        print("Scissors VS Rock, Player 2 Wins!")


            
    else:
        print("ok, closing game")
        exit()
    