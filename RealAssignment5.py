'''
Created on Apr 11, 2019

@author: Berkohfam
'''
from tkinter import *

import random
root = Tk()

dealerfirst_card = random.randint(1,10)
dealersecond_card = random.randint(1,10)
dealerthird_card = random.randint(1,10)

playerfirst_card = random.randint(1,10)
playersecond_card = random.randint(1,10)

                            
dealers = (dealerfirst_card + dealersecond_card + dealerthird_card )



players = (playerfirst_card + playersecond_card )
You = Label(root, text = "You have these cards:"+ " " + str(playerfirst_card) + " " + str(playersecond_card) + " "+ "Your cards make a combined total of:" + " " + str(players))
You.pack()


Action = Label(root, text= "Would you like to Hit or Stay?")
TextBox = Entry(root)
Action.pack()
TextBox.pack()

    
    
def send ():    
    userinput = TextBox.get()
    if userinput == "hit":
        playerthird_card = 3
        current = playerfirst_card + playersecond_card + playerthird_card
        player_result = Label(root, text= "You now have:" + " " + str(current) + " " + "With these cards:" + " " + str(playerfirst_card) + " " + str(playersecond_card) + " "+ str(playerthird_card))
        player_result.pack()
        dealer_result = Label(root, text= "Dealer has:" + " " + str(dealerfirst_card) + " " + str(dealersecond_card) + " " + str(dealerthird_card) + " " + "The dealer has a combined total of:"+ " "+ str(dealers))
        dealer_result.pack()
        if current < 21 and dealers < 21 :
            if dealers == current:
                Tie = Label(root, text = "It's a tie!")
                Tie.pack()
                    
            if current < dealers:
                DealerWins = Label(root, text = "Dealer Wins :(")
                DealerWins.pack()
            if current > dealers:
                playerwins = Label(root, text = "You Win!")
                playerwins.pack()
        else:
            if current > 21:
                DealerWins3 = Label(root, text = "You Busted! Dealer Wins :(")
                DealerWins3.pack()
            elif dealers> 21:
                playerwins3 = Label(root, text = "Dealer Busted! You Win!")
                playerwins3.pack()

            
    else:
        dealer_result = Label(root, text= "Dealer has:" + " " + str(dealerfirst_card) + " " + str(dealersecond_card) + " " + str(dealerthird_card) + " " + "The dealer has a combined total of"+ " "+ str(dealers))
        dealer_result.pack()
        if players < 21 and dealers < 21 :
            if dealers == players:
                Tie = Label(root, text = "It's a tie!")
                Tie.pack()
                    
            if players < dealers:
                DealerWins = Label(root, text = "Dealer Wins :(")
                DealerWins.pack()
            if players > dealers:
                playerwins = Label(root, text = "You Win!")
                playerwins.pack()
        else:
            if players > 21:
                DealerWins3 = Label(root, text = "You Busted! Dealer Wins :(")
                DealerWins3.pack()
            elif dealers> 21:
                playerwins3 = Label(root, text = "Dealer Busted! You Win!")
                playerwins3.pack()

sendb = Button (root, text = "Check", command = send)
sendb.pack()
   
root.mainloop()
