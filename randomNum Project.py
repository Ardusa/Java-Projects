import random

print("Welcome to Blackjack, the game of Hit and Bust")
print("ACTIVATE ALL CAPS")
name = input("\nNow what will your username be? ")
begin = input(name + ", I love it, are you ready to start? (Y/N): ")

round = 1
money = 1000

if (begin == 'Y'):
    print("Great! Lets get started!")
else:
    while (begin != 'Y'):
        begin = input("Well, how about now? ")

readRules = input("Would you like to review the rules of Blackjack (Y/N): ")
if (readRules == 'Y'):
    print("\n\nBlackjack for dummies:")
    print("Welcome to Blackjack, the game of Hit and Bust")
    print("In this game you will be attempting to collect 21 points")
    print("But be careful, when you hit, you dont want to bust!")
    print("All numbered cards are face value, Ace is 11 points, J/Q/K are 11/12/13")
    print("This is a 1-on-1 duel with the dealer, his name is Cobra.")
    print("However much you put down as a bet, dealer will match")
else:
    print("Let the game BEGIN!")

while (round == 1):

    # Variables
    betVal = 0
    betState = " "
    balance = " your current balance is $" + str(money)
    nextCard = 0
    x = 3
    game = " "
    hitStay = " "

    player = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    playerPts = 0
    dealer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    dealerPts = 0

    print("\n\n" + name + ", you have $" + str(money))

    while (betState != "I"):
        betVal = int(input("How much money do you want to put down: $"))
        if (betVal > money):
            print("\nYou dont have that much money." + balance)
        elif (betVal <= 0):
            print("\nYou cant bet an amount less than $1." + balance)
        elif (betVal == money):
            confirm = input(
                "\nWoah, " + name + " thats all your money. Please confirm that your betting your full account (Y/N): ")
            if (confirm == 'Y'):
                print("\nAlright, Good Luck!")
                betState = 'I'
                money = money - betVal
            else:
                print("")
        else:
            print("\nAlright, Good Luck " + name + "!")
            money = money - betVal
            betState = "I"

# First 4 cards assignment
    for k in range(4):
        card = random.randint(1, 13)
        stringCard = str(card)

        if stringCard == '1':
            stringCard = 'A'
        if stringCard == '11':
            stringCard = 'J'
        if stringCard == '12':
            stringCard = 'Q'
        if stringCard == '13':
            stringCard = 'K'

        if k == 0:
            print("\n\n\n\n\n" + name + "'s first card: " + stringCard)
            player[0] = card
            playerPts = playerPts + player[0]
        elif k == 1:
            print("\nThe dealer pulled a hidden card")
            dealer[0] = card
            dealerPts = dealerPts + dealer[0]
        elif k == 2:
            print("\n" + name + "'s second card: " + stringCard)
            player[1] = card
            playerPts = playerPts + player[1]
        elif k == 3:
            print("\nThe dealer pulled: " + stringCard)
            dealer[1] = card
            dealerPts = dealerPts + dealer[1]
        else:
            nextCard = eval(stringCard)

    while (hitStay != "STAY"):
        hitStay = input("\n" + name + " would you like to 'HIT' or 'STAY': ")
        if hitStay == "HIT":
            nextCard = random.randint(1, 13)
            print(name + " you pulled: " + str(nextCard))
            player[x] = nextCard
            playerPts = playerPts + player[x]
            x = x + 1
        elif hitStay == "STAY":
            print("")
        else:
            print("Invalid Function")

        if playerPts > 21:
            print("\n   Looks like you busted!")
            print("  |----------------------|")
            print("  |       YOU LOST       |")
            print("  |----------------------|")
            hitStay = "STAY"
            game = "LOSS"
    if playerPts <= 21:
        print(name + " your turn is over.")

    if game != "LOSS" and game != "WIN":
        x = 3
        hitStay = " "

        print("\nNow the dealer flips his cards")
        print("The dealer has: " + str(dealer[0]) + " & " +
              str(dealer[1]) + ". Totalling to " + str(dealerPts))

        while (hitStay != "STAY"):
            if dealerPts <= 16:
                hitStay = "HIT"
                print("The dealer must hit, as he has 16 or less points.")
                nextCard = random.randint(1, 13)
                dealer[x] = nextCard
                dealerPts = dealerPts + dealer[x]
                print("The Cobra pulled: " + str(nextCard))
                print("He now has " + str(dealerPts) + " points.")
                x = x + 1
            elif dealerPts >= 17:
                hitStay = "STAY"
                print("The dealer must stay, as he has 17 or more points.")
                print("The round is over, whoever is closest to 21 wins.")
            else:
                print("Invalid Input")

            if dealerPts > 21:
                hitStay = "STAY"
                game = "WIN"
            elif dealerPts < playerPts:
                game = "WIN"
            elif playerPts < dealerPts:
                game = "LOSS"
            else:
                game = "TIE"

        if game == "LOSS":
            print("\n\nYou have lost your bet,")
            print("  |----------------------|")
            print("  |       YOU LOST       |")
            print("  |----------------------|")
        elif game == "WIN":
            print("\n\n         CONGRATULATIONS!")
            print("  |----------------------|")
            print("  |        YOU WON       |")
            print("  |----------------------|")
            money = money + (2 * betVal)
        else:
            print("You tied! None of you gained or lost money.")
            print("  |----------------------|")
            print("  |       YOU TIED       |")
            print("  |----------------------|")
            money = money + betVal

        print("Current account balance: $" + str(money))

        if money != 0:
            round = 0
            while (round == 0):
                cont = input(
                    "Would you like to 'CASH OUT' or would you like to 'CONTINUE': ")
                if cont == "CASH OUT":
                    print("\n\nI hope you had fun! Come back soon!")
                    round = -1
                elif cont == "CONTINUE":
                    print("Ok, lets run it back!")
                    round = 1
                else:
                    print("Invalid Entry")
                    round = 0
        else:
            print("Broke ahh go away, dont come(pause) again another day!")
            round = 0
    else:
        print("Current account balance: $" + str(money))
        while (round > 0):
            if money != 0:
                cont = input(
                    "Would you like to 'CASH OUT' or would you like to 'CONTINUE': ")
                if cont == "CASH OUT":
                    print("\n\nI hope you had fun! Come back soon!")
                    round = 0
                elif cont == "CONTINUE":
                    print("Ok, lets run it back!")
                    round = round + 1
                else:
                    print("Invalid Entry")
                    round = -1
            else:
                print("Broke FOOL go away, dont come again another day!")
                round = 0
