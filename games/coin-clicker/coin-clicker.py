import pgzrun
import random # Python random module
WIDTH = 800 # Sets the Height and Width of the playing area
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
center = (CENTER_X, CENTER_Y) # The center of the screen
Coins = 0 # Amount of coins you have
button = Actor("button") # These are the buttons that cost certain coins and increase the amount of coins you have based on cost
button.pos = 650, 100
button1 = Actor("button2")
button1.pos = 650, 300
button2 = Actor("button3")
button2.pos = 650, 500
button3 = Actor("button4")
button3.pos = 150, 100
button4 = Actor("button5")
button4.pos = 150, 300
button5 = Actor("button6")
button5.pos = 150, 500

coin = Actor("coin") # The coin to click and get coins
coin.pos = center

cost1 = 100 # Costs of the buttons that increase your coin amount
cost2 = 500
cost3 = 1000
cost4 = 5000
cost5 = 10000
cost6 = 50000

def draw(): # Pygame Zero Draw function that draws everything on the screen
    screen.blit("stage", (0, 0))
    coin.draw() # Draws the coin
    button.draw() # Draws the buttons
    button1.draw()
    button2.draw()
    button3.draw()
    button4.draw()
    button5.draw()
    # Draws your score and costs on the buttons
    screen.draw.text("Coins: " + str(Coins), fontsize=55, color="black", topleft=(6, 6))
    screen.draw.text("$" + str(cost1), fontsize=55, color="black", topright=(670, 90))
    screen.draw.text("$" + str(cost2), fontsize=55, color="black", topright=(670, 290))
    screen.draw.text("$" + str(cost3), fontsize=55, color="black", topright=(670, 490))
    screen.draw.text("$" + str(cost4), fontsize=55, color="black", topright=(170, 90))
    screen.draw.text("$" + str(cost5), fontsize=55, color="black", topright=(195, 290))
    screen.draw.text("$" + str(cost6), fontsize=55, color="black", topright=(195, 490))
    if Coins >= cost1: # Tells you if you have enough money for one of the buttons that increase your coins
        screen.draw.text("Eligible!", fontsize=45, color="blue", topright=(676, 60))
    if Coins >= cost2:
        screen.draw.text("Eligible!", fontsize=45, color="blue", topright=(676, 260))
    if Coins >= cost3:
        screen.draw.text("Eligible!", fontsize=45, color="blue", topright=(676, 460))
    if Coins >= cost4:
        screen.draw.text("Eligible!", fontsize=45, color="blue", topright=(176, 60))
    if Coins >= cost5:
        screen.draw.text("Eligible!", fontsize=45, color="blue", topright=(196, 260))
    if Coins >= cost6:
        screen.draw.text("Eligible!", fontsize=45, color="blue", topright=(196, 460))



    
def add_coins(): # Adds coins, each one is different for each button
    global Coins
    Coins = Coins + 1
    return

def add_more_coins():
    global Coins
    Coins = Coins + 5
    return

def add_lots_coins():
    global Coins
    Coins = Coins + 10
    return
    
def add_huge_coins():
    global Coins
    Coins = Coins + 20
    return

def reset_coin(): # Resets the coin to its default size
    global coin
    coin.image = "coin"
    return

def on_mouse_down(pos): # Pygame Zero handle mouse click function
    global coin_collected, cost1, cost2, cost3, cost4, cost5, cost6
    coin_collected = coin.collidepoint(pos) # Checks if player clicks coin
    if coin_collected:
        global Coins
        Coins = Coins + 1
        coin.image = "coin1" # Makes image smaller (more about it later)
    if button.collidepoint(pos): # Checks if player clicks on buttons
        if Coins >= cost1:
            button.image = "button-down" # Makes buttons smaller when clicked (only if you have enough coins for it)
            Coins = Coins - cost1 # Subtract the cost of the button from the amount of coins you have
            cost1 += random.randint(12, 20) # Increase the cost of that button by a random amount between 12 and 20
            clock.schedule_interval(add_coins, 5) # Adds coins to the amount of coins you have
    if button1.collidepoint(pos):
        if Coins >= cost2:
            button1.image = "button-down"
            Coins = Coins - cost2
            cost2 += random.randint(12, 20) 
            clock.schedule_interval(add_coins, 1)
    if button2.collidepoint(pos):
        if Coins >= cost3:
            button2.image = "button-down"
            Coins = Coins - cost3
            cost3 += random.randint(12, 20)
            clock.schedule_interval(add_more_coins, 2)
    if button3.collidepoint(pos):
        if Coins >= cost4:
            button3.image = "button-down"
            Coins = Coins - cost4
            cost4 += random.randint(12, 20)
            clock.schedule_interval(add_more_coins, 1)
    if button4.collidepoint(pos):
        if Coins >= cost5:
            button4.image = "button-down"
            Coins = Coins - cost5
            cost5 += random.randint(12, 20)
            clock.schedule_interval(add_lots_coins, 1)
    if button5.collidepoint(pos):
        if Coins >= cost6:
            button5.image = "button-down"
            Coins = Coins - cost6
            cost6 += random.randint(12, 20)
            clock.schedule_interval(add_huge_coins, 2)
    return

def on_mouse_up(pos): # Pygame Zero handle mouse click released function
    global coin, button, button2, button3, button4, button5
    if button.image == "button-down": # Resets buttons to original size
        button.image = "button"
    if button1.image == "button-down":
        button1.image = "button1"
    if button2.image == "button-down":
        button2.image = "button2"
    if button3.image == "button-down":
        button3.image = "button3"
    if button4.image == "button-down":
        button4.image = "button4"
    if button5.image == "button-down":
        button5.image = "button5"
    if coin.image == "coin1": # Resets coin to original size
        reset_coin()
    return
pgzrun.go()
