import time
import os

compLines = [
    "HOWIE: Hi, David!",
    "null",
    "HOWIE: Pretty Good.",
    "HOWIE: Sure, Thanks!",
    "HOWIE: Bye, David!"
]

playerLines = [
    "Hi Howie",
    "Hows It Going",
    "Hey You Wanna Take This Over",
    "null",
    "Bye"
]

playerActions = [
    "wave",
    "high five",
    "step back",
    "null",
    "wave"
]

narrLines = [
    "CONGRATULATIONS! YOU HAVE OPENED THE FIRST GATE!",
    "YOU HAVE 3 LIVES, GOOD LUCK!",
    "COMPUTER: My God, it's full of stars.",
    "YOU'RE GOING TO BE LATE FOR SCHOOL!\n",
    "YOU'RE GOING TO BE LATE FOR SCHOOL, DAVID! HURRY!"
]

yesNoPrompt = [
    "Would you like to enter the gate? (Y/N): ",
    "Follow the green path? (Y/N): "
]

lives = 3
score = 41780

def prompt(x):
    global lives, score

    if (compLines[x] != "null"):
        if (x == 4):
            time.sleep(0.5)

        else:
            time.sleep(0.5)

        print(compLines[x])

    if (playerLines[x] != "null"):
        time.sleep(0.5)
        y = input("WADE: ")
        while(str(lives) == "1"):
            if (y.casefold() == ""):
                print("You can't skip, this is your last life")
                if (compLines[x] != compLines[1]):
                    print(compLines[x])
                    time.sleep(0.2)
                    y = input("WADE: ")
    else:
        y = "silentSkip"

    while(y.casefold() != str(playerLines[x]).casefold()):
        lives = lives - 1
        if (lives == 0):
            time.sleep(0.4)

            print("GAME OVER\n\n\n\n")
            return quit()
        
        if (y == "silentSkip"):
            return

        if (y.casefold() == ""):
            print()
            time.sleep(0.2)
            score = score - 100
            print("\tSkipped, you have:", lives, "lives left.\nYou lost 100 points")
            time.sleep(3)
            return
        else:
            os.system('clear')
            print("\nIncorrect\tLives Remaining " + str(lives))
            print()
            prompt(x)
    else:
        if (playerActions[x] != "null"):
            z = input("WADE (ACTION): ")
            if (z.casefold() == str(playerActions[x])):
                score = score + 200
                print()
                time.sleep(0.1)
                print("\tPlus 200 Points")
                time.sleep(0.1)
                print()
                time.sleep(3)
                return

        score = score + 100
        print()
        time.sleep(0.1)
        print("\n\tPlus 100 Points\n")
        time.sleep(0.1)
        print()
        time.sleep(3)
        return

os.system('clear')

print("Welcome to The (technically but not as much as the OASIS) Virtual Hunt, a program written by Ankur Desai.\n")

print(narrLines[0])
time.sleep(4)
print()

print("Here are the rules:")
print()
print("\t- Dont use and punctuation such as periods ( . ) or commas ( , )")
print("\t- If you get the script wrong, you lose one life and try again")
print("\t- You start the game with exactly 41780 points, if you dont know why that number, you've already lost :(")
print("\t- If you dont know one of the lines, dont type anything and press enter. By doing so you will lose a life and 100 points")
print("\t- If you manage to get through the entire thing without losing any lives you get a 1000 point 'better' bonus")
print("\t- If there is a (ACTION) sign, then you should choose between the following: high five, wave, step back")
print(narrLines[1])

time.sleep(2)
print()
x = input(yesNoPrompt[0])
if (x.capitalize().strip() != "Y"):
    quit()

os.system('clear')
time.sleep(0.2)
print(narrLines[2])
time.sleep(1)
print(narrLines[3])
time.sleep(1)

for i in range(len(playerLines)):
    prompt(i)
    time.sleep(2)
    os.system('clear')

time.sleep(1)
print("Your score is:", score)
time.sleep(1)
if (lives == 3):
    print()
    time.sleep(0.1)
    print("\n\t1000 Point 'better' bonus awarded\n")
    time.sleep(0.1)
    print()
    score = score + 1000
    print()
    time.sleep(0.1)
    print("\n\tYou now have:", score, "points\n")
    time.sleep(0.1)
    print()
    time.sleep(1)

if (lives == 0):
    print("Hint: READ YOUR BOOK!")
else:
    print("CONGRATULATIONS ON WINNING:")
    time.sleep(3)
    print("absolutely nothing")
    time.sleep(2)
    print("lol")