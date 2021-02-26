import random
import time

print("Welcome to hangman Game\n")

x = input("Enter your name : ")
print("Hello ",x)
time.sleep(2)
print("Welcome to Hangman Game")
time.sleep(3)
def main():
    global count,display,word,length,play_game,already_guessed
    words =["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(words)
    length = len(word)
    count = 0
    display = "_ " * length
    already_guessed = []
    play_game = ""
def play_loop():
    global play_game
    play_game = input("Do you want to play again ? Y/N\n")
    while play_game not in ["y","n","Y","N"]:
        play_game = input("Do you want to play again ? Y/N\n")
    if play_game =="y" or play_game =="Y":
        main()
    elif play_game =="N" or play_game =="n":
        print("Thanks for playing\n")
        exit()
def hangman():
    global count,display,word,already_guessed,play_game
    limit = 5
    print("This is the hangman word: ",display)
    guess = input(" Enter your guess: ")
    guess = guess.strip()
    if len(guess.strip())==0 or len(guess.strip())>=2 or guess<="9":
        print("Invalid input , try again\n")
        hangman()
    elif guess in word:
        already_guessed.append(guess)
        index = word.find(guess)
        word = word[:index] + "_" + word[index+1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("try another letter \n")
    else:
        count+=1
        if count ==1:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count ==2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count ==3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count ==4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     o\n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count ==5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     o\n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
            print("The word was : ",already_guessed,word)
            play_loop()
    if word == "_" * length:
        print("The word is guessed correctly\n")
        play_loop()
    elif count !=limit:
        hangman()

main()
hangman()
