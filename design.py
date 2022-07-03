from tkinter import *

# ==========================================================================
# GUI Design

window = Tk()
window.title("Blackjack")
window.resizable(0,0)

textColor = "#6b665a"
backgroundColor = "#cec8b0"

window.config(width = 741, height = 560, background = backgroundColor)

#title
title = StringVar()
title.set(value = "BLACKJACK")

blankText = StringVar()
blankText.set(value = "")

dealer = StringVar()
dealer.set(value = "DEALER")

player = StringVar()
player.set(value = "YOU")

enterbet = StringVar()
enterbet.set(value = "ENTER BET AMOUNT:")

moneyText = StringVar()
moneyText.set(value = "MONEY: ")

#changing text
playersum = StringVar()
playersum.set(value = "0")

dealersum = StringVar()
dealersum.set(value = "?")

totalmoney = StringVar()
totalmoney.set(value = 500)

betframecolor = "#b0ab96"

#line that separates the dealer and player side
separation = Frame(window, width = 740, height = 2, bg = textColor)
separation.place(x = 0, y = 285)
betFrame = Frame(window, width = 300, height = 200, bg = textColor)
betFrame.place(x = 225, y = 320)

startTextFrame = Frame(window, width = 400, height = 70, bg = textColor)
startTextFrame.place(x = 180, y = 120)

gameOverFrame = Frame(width = 741, height = 560, background = textColor)

#text
titletext = Label(window, textvariable = title, fg = textColor, bg = backgroundColor, font = ("Eina 01", 24))
titletext.place(x = 283, y = 10)

dealer_text = Label(window, textvariable = dealer, fg = textColor, bg = backgroundColor, font = ("Eina 01", 16))
dealer_text.place(x = 5, y = 255)

player_text = Label(window, textvariable = player, fg = textColor, bg = backgroundColor, font = ("Eina 01", 16))
player_text.place(x = 5, y = 290)

money_text = Label(window, textvariable = moneyText, fg = textColor, bg = backgroundColor, font = ("Eina 01", 12))
money_text.place(x = 5, y = 530)

gameover_text = Label(window, text = "GAME OVER", fg = backgroundColor, bg = textColor, font = ("Eina 01", 30))

#changing text
dealer_total = Label(window, textvariable = dealersum, fg = textColor, bg = backgroundColor, wraplength = 741, font = ("Eina 01", 35))
dealer_total.place(x = 25, y = 110)

player_total = Label(window, textvariable = playersum, fg = textColor, bg = backgroundColor, wraplength = 741, font = ("Eina 01", 35))
player_total.place(x = 25, y = 400)

startText = Label(window, text = "PLACE YOUR BET TO START!", fg = backgroundColor, bg = textColor, font = ("Eina 01", 18))
startText.place(x = 210, y = 140) #will appear after an outcome

dialogueText = Label(window, text = " ", fg = textColor, bg = backgroundColor, font = ("Eina 01", 16))
 #will appear after an outcome

totalmoney_text = Label(window, textvariable = totalmoney, fg = textColor, bg = backgroundColor, font = ("Eina 01", 12))
totalmoney_text.place(x = 80, y = 530)

placedBet = Entry(window, width = 20)
placedBet.place(x = 310, y = 405)

#buttons/user input
enterbetamount = Label(window, textvariable = enterbet, fg = backgroundColor, bg = textColor, font = ("Eina 01", 15))
enterbetamount.place(x = 270, y = 350)