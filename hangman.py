import random

# import only system from os
from os import system, name

# import all hangman module
from hangman_words import word_list
from hangman_art import hangman_stage
from hangman_art import hangman_logo

# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
chosen_word=random.choice(word_list)

display=[]
print(hangman_logo)
#fill the letters
for i in range(len(chosen_word)):
    display+="_"
    word_0=" ".join(display)
print(f"Guess the word.  The Word has {len(chosen_word)} letters: ")
print(word_0)

end_of_game=False
hung=0
lives=6
while not end_of_game:
    guess=input("\nchose a letter from a to z:- ")
    guess_letter=guess.lower()
     # Clearing the Screen
     
    if guess_letter not in display:
        
        if guess_letter in chosen_word: 
            for i in range(len(chosen_word)):
                if (chosen_word[i]==guess_letter):
                    display[i]=guess_letter
                
        else:
            print(f"you guess {guess_letter},that's not in word ,you lose a life.")
            hung+=1
            lives-=1
            if lives==0:
                end_of_game=True
                print(chosen_word)
                print("you loose")
                
        word=" ".join(display)            
        print(word)
        print(hangman_stage[hung])
        
    else:
        print(f"you already guessed {guess_letter}")
        
    if "_" not in display:
        end_of_game=True 
        print("you win")

    


