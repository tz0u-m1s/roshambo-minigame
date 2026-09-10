from random import randint
while True:
    game_start=input("Start Playing Rock Paper Scissors? Y/N ")


    if game_start=="Y" or game_start=="y":
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
                    print("Player Wins!")
                elif RPS_player_pick==1 and RPS_AI_pick==2:
                    print("AI Wins!")
                elif RPS_player_pick==2 and RPS_AI_pick==1:
                    print("Player Wins!")
                elif RPS_player_pick==2 and RPS_AI_pick==3:
                    print("AI Wins!")
                elif RPS_player_pick==3 and RPS_AI_pick==2:
                    print("Player Wins!")
                elif RPS_player_pick==3 and RPS_AI_pick==1:
                    print("AI Wins!")
            
    else:
        print("ok, closing game")
        exit()
    