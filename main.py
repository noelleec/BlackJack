import random
from tkinter import *
from card import Card
from deck import Deck
from hand import Hand
from design import *

money = 500

def start():

    global money
    global bet

    try:
        bet = float(placedBet.get())

    except ValueError:
        startText.config(text = "INVALID BET PLACED")
        placedBet.delete(0, END)
        startText.place(x = 258)

    bet = float(placedBet.get())

    if bet > money:
        startText.config(text = "MAXIMUM BET = $" + str(money))
        placedBet.delete(0, END)
        startText.place(x = 255)
    elif bet < 1:
        startText.config(text = "MINIMUM BET = $1")
        placedBet.delete(0, END)
        startText.place(x = 270)
    else:
        placedBet.place_forget()
        placeBetButton.place_forget()
        enterbetamount.place_forget()
        betFrame.place_forget()
        startText.place_forget()
        startTextFrame.place_forget()

        placedBet.delete(0, END)

        money = money - bet
        totalmoney.set(value = money)

        dealstart()

def dealstart():

    global deck
    global playerHand
    global dealerHand

    deck = Deck()

    playerHand = Hand(deck.deal(), deck.deal())
    playerHand.printCards(playersum)

    dealerHand = Hand(deck.deal(), deck.deal())
    dealerHand.printDealerHand()

    hit.config(state = 'normal')
    stand_button.config(state = 'normal')

def hitCard():

    global deck
    global playerHand
    global money

    playerHand.hit(deck.deal())
    playerHand.printCards(playersum)

    if (playerHasLost()):

        stand()

def playerHasLost():

    global playerHand

    playerTotals = playerHand.getTotal()

    for total in playerTotals:
        if total <= 21:
            return False
    return True

def dealerHasLost():

    global dealerHand

    dealerTotals = dealerHand.getTotal()

    for total in dealerTotals:
        if total <= 21:
            return False
    return True

def playAgain():

    global bet 

    startText.config(text = "PLACE YOUR BET TO START!")

    bet = " "

    playagain_button.place_forget()

    dialogueText.config(text = " ")

    playersum.set(value = "0")
    dealersum.set(value = "?")

    dealerHand.reset()
    playerHand.reset()

    placedBet.place(x = 310, y = 405)
    placeBetButton.place(x = 320, y = 450)
    enterbetamount.place(x = 270, y = 350)
    betFrame.place(x = 225, y = 320)
    startText.place(x = 210, y = 140)
    startTextFrame.place(x = 180, y = 120)

def hideMenu():

    hit.place_forget()
    stand_button.place_forget()
    titletext.place_forget()
    dealer_total.place_forget()
    player_total.place_forget()
    separation.place_forget()
    totalmoney_text.place_forget()
    player_text.place_forget()
    dealer_text.place_forget()
    playagain_button.place_forget()
    dialogueText.place_forget()
    money_text.place_forget()

def stand():

    global deck
    global playerHand
    global dealerHand
    global money
    global bet

    hit.config(state = 'disabled')
    stand_button.config(state = 'disabled')

    foundCard = False

    while not dealerHasLost() and not foundCard:
        for total in dealerHand.getTotal():
            if total >= 16 and total <= 21:
                foundCard = True
        if not foundCard:
            dealerHand.hit(deck.deal())

    dealerHand.printCards(dealersum)

    dealerValue = -1
    for total in dealerHand.getTotal():
        if total <= 21:
            dealerValue = total

    playerValue = -1
    for total in playerHand.getTotal():
        if total <= 21:
            playerValue = total

    if dealerValue == playerValue:
        # draw
        dialogueText.config(text = "YOU TIED WITH THE DEALER!")
        dialogueText.place(x = 235, y = 255)
        money = money + bet
        totalmoney.set(value = money)

        if money == 0:
            gameover_text.place(x = 250, y = 255)
            gameOverFrame.place(x = 0, y = 0)

            hideMenu()

        else:
            playagain_button.place(x = 625, y = 290)
            playagain_button.config(state = 'normal')

    elif playerValue > dealerValue:
        # you win
        dialogueText.config(text = "YOU WON!")
        dialogueText.place(x = 320, y = 255)
        money = money + (1.5 * bet)
        totalmoney.set(value = money)
        playagain_button.place(x = 625, y = 290)
        playagain_button.config(state = 'normal')
    
    else:
        # you lose
        dialogueText.config(text = "YOU LOST!")
        dialogueText.place(x = 315, y = 250)

        totalmoney.set(value = money)

        if money == 0:
            gameover_text.place(x = 250, y = 255)
            gameOverFrame.place(x = 0, y = 0)

            hideMenu()

        else:
            playagain_button.place(x = 625, y = 290)
            playagain_button.config(state = 'normal')

    hit.config(state = 'disabled')
    stand_button.config(state = 'disabled')

#button GUI
hit = Button(window, text = "HIT", fg = textColor, bg = backgroundColor, font = ("Eina 01", 10), state = DISABLED, command = lambda: hitCard())
hit.place(x = 645, y = 525)

stand_button = Button(window, text = "STAND", fg = textColor, bg = backgroundColor, font = ("Eina 01", 10), state = DISABLED, command = lambda: stand())
stand_button.place(x = 680, y = 525)

playagain_button = Button(window, text = "PLAY AGAIN!", fg = textColor, bg = backgroundColor, font = ("Eina 01", 12), state = DISABLED, command = lambda: playAgain())

placeBetButton = Button(window, text = "PLACE BET", fg = backgroundColor, bg = textColor, font = ("Eina 01", 13), command = lambda: start())
placeBetButton.place(x = 320, y = 450)

window.mainloop()