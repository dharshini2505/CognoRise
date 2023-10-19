import random
from hangman import hangman

words=["computer","engineer","software","python","coding"]
word=random.choice(words)

def  StartGame(words):
    guess_word = ["_"for i in word]
    tries = 0
    print(hangman[tries])
    print("Guess a Word: {}".format(" ".join(guess_word)))
    
    while True:
        user = input("Guess a Letter [a-z]:")
        if not user.isalpha():
            print("pleas enter [a-z] only.")
            continue
        if user in word:
            indexes = [ i for i in range(len(word)) if word[i] == user ]
            for index in indexes :
                guess_word[index] = user
            print("=" * 50)
            print("Good : {}".format("".join(guess_word)))
            
            if "".join(guess_word) == word:
                return "Wow! You Guessed :)"
        else:
            tries = tries + 1
            print(hangman[tries])
            if tries == 6:
                return " Sorry!! Game Over"
            print("sorry!!.Try again : {}".format("".join(guess_word)))
        

if __name__ == "__main__":
        while True:
            StartGame(word)
            Play_again = input("Do You Want Play Again[y/n] : ")
            if Play_again == "y":
                word = random.choice(words)
                continue
            else:
                break