import random
from words import words
import string

Game = "HANGMAN"
Game_Bold = '\033[1;4m' + Game + '\033[0m' 
print(f"Welcome To {Game_Bold}")
print("\n")

Random_Word = random.choice(words).upper()
letters = set(Random_Word)
Valid1 = []
Used_alphabets = set()
lives = 6
Exit = "False"

while True:
       Wrong = 0
       print(f"---There are {lives} lives left---")
       print("The Letters you have used : "," ".join(Used_alphabets))

       print(f"The Word is {len(Random_Word)} Characters long.")

       Word = ['_'] * len(Random_Word)
       #print("Word : "," ".join(Word))

       alphabets = set(string.ascii_uppercase)

       guess = input("Guess The Letter : ").upper()

       
       if guess in alphabets - Used_alphabets:
              Used_alphabets.add(guess)
              if guess in letters:
                     letters.remove(guess)
              else:
                     lives = lives -1
       elif guess in Used_alphabets:
              print("You have already used this letter")
       
       else:
              print("Invalid Character")
       
       Valid1 = [guess if guess in Used_alphabets else '_' for guess in Random_Word] 
       print("Word : "," ".join(Valid1))
       
       if lives == 0 or len(letters) == 0:
              break

if lives == 0:
       print("Wow, You have lost")
       print(f"The Word was {Random_Word}")
       
if len(letters) == 0:
       print("Wow, You Have Won")