import time
import os
import random

#1 Tables
Stanza = [[], [], []]
StanzaIn = [[], [], []]

#2 Lists
Stanza[0] = [
    "We're no strangers to love",
    "A full commitment's what I'm thinking of",
    "I just wanna tell you how I'm feeling",
]

StanzaIn[0] = [
    "You know the rules and so do I",
    "You wouldn't get this from any other guy",
    "Gotta make you understand",
]

Stanza[1] = [
    "We've known each other for so long",
    "Inside, we both know what's been going on (going on)",
    "And if you ask me how I'm feeling",
]

StanzaIn[1] = [
    "Your hearts been aching but you're too shy to say it",
    "We know the game and we're gonna play it",
    "Don't tell me you're too blind to see",
]

Stanza[2] = [
    "We've known each other for so long",
    "Inside, we both know what's been going on (going on)",
    "I just wanna tell you how I'm feeling",
]

StanzaIn[2] = [
    "Your hearts been aching but you're too shy to say it",
    "We know the game and we're gonna play it",
    "Gotta make you understand",
]

chorus = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
]

#2 Variables
lives: int = 5
score: int = 0

#4 endGame function
# Process for ending the game
def endGame():
    os.system("clear")
    time.sleep(0.5)
    if lives > 0:
        print("You Won!")
    else:
        print("You Lost!")

    #5 sleep function
    time.sleep(0.5)
    #6 print function
    print()
    print("You finished the game with:")
    time.sleep(0.75)
    print("Score: " + str(score) + "\t\t\tLives: " + str(lives))
    time.sleep(2)
    print()
    print()
    #7 abort function
    os.abort()

#8 chooseOptions function
# Makes sure that nothing gets chosen twice
def chooseOptions(chosenNum: int, chosenOption: str, options: list[str], x: int) -> str:
    if x == (chosenNum - 1):
        return chosenOption
    else:
        #9 random int
        returnStr = StanzaIn[random.randint(0, 2)][random.randint(0, 2)]
        #10 for loop
        #11 string length
        for y in range(options.__len__()):
            #12 if statement
            if returnStr == options[y]:
                returnStr = chooseOptions(chosenNum, chosenOption, options, x)
        return returnStr

#13 prompt function
def prompt(stanzaNum: int, stanzaLine: int):
    global lives, score

    if stanzaLine < 3:
        option = ["", "", "", ""]
        chosenOption: str = StanzaIn[stanzaNum][stanzaLine]
        chosenNum = random.randint(1, 4)
        for x in range(4):
            option[x] = chooseOptions(chosenNum, chosenOption, option, x)

        #14 clear console
        os.system("clear")
        print(Stanza[stanzaNum][stanzaLine])
        print()
        time.sleep(1)
        print("Option 1: ", option[0])
        time.sleep(0.7)
        print("Option 2: ", option[1])
        time.sleep(0.7)
        print("Option 3: ", option[2])
        time.sleep(0.7)
        print("Option 4: ", option[3])
        print()
        time.sleep(0.4)
        #15 input
        humInput = int(input("Option: "))

        if humInput == chosenNum:
            #16 increment
            score += 100
            return
        else:
            #17 decrement
            lives -= 1
            score -= 100
            if lives > 0:
                #18 recursive function
                prompt(stanzaNum, stanzaLine)
            else:
                endGame()
    else:
        os.system("clear")
        for i in chorus:
            print(i)
            time.sleep(1.3)
        time.sleep(2)


os.system("clear")
print("Welcome to Song Quiz")
time.sleep(2)
print("In this game you will be given a line of a song")
time.sleep(2)
print("Your job is to respond with the correct option number")
time.sleep(3)
print("The song will be:\n\tNever Gonna Give You Up\n\tby Rick Astley")
time.sleep(2)
print("Good Luck!")
time.sleep(2)

#19 for loop
for x in range(3):
    os.system("clear")
    time.sleep(0.1)
    #20 for loop
    for y in range(4):
        prompt(x, y)

endGame()
\