# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    for secret_letter in secret_word:
        if secret_letter not in letters_guessed:
            return False
            
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    n1 = len(secret_word)
    n2 = len(letters_guessed)
    guessed_word = ""
    
    for i in range(n1):
        aux = False
        for j in range(n2):
            if secret_word[i] == letters_guessed[j]:
                aux = True
                guessed_word += secret_word[i]
                break
        if not aux:
            guessed_word += "_ "
            
    return guessed_word
            


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    n1 = len(letters_guessed)
    abc = string.ascii_lowercase
    for i in range(n1):
        abc = abc.replace(letters_guessed[i], "")
        
    return abc
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    warming = 3
    letters_guessed = [] #list (mutable)
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long."
          .format(len(secret_word)))
    
    while guesses > 0 and not is_word_guessed(secret_word,letters_guessed):
        print("------------")
        abc = get_available_letters(letters_guessed)
        print("You have {} guesses left.".format(guesses))
        print("Available Letters: {}".format(abc))
        letter = input("Please guess a letter: ")
        
        
        if len(letter) != 1 or not str.isalpha(letter):
            if warming == 0:
                guesses = guesses-1
                print("You lost a guess")
            else:
                warming = warming-1
                print("Oops! That is not a valid letter. You have {} warmings left: {}"
                      .format(warming,get_guessed_word(secret_word, letters_guessed)))
        else:
            letter = str.lower(letter)
            
            if letter in letters_guessed:
                if warming == 0:
                    guesses = guesses-1
                    print("You lost a guess")
                else:
                    warming = warming-1
                    print("Oops! You've already guessed that letter: {}"
                          .format(get_guessed_word(secret_word, letters_guessed)))                
            elif letter not in secret_word:
                letters_guessed.append(letter)
                print('Oops! That letter is not in my word: {}'
                      .format(get_guessed_word(secret_word,letters_guessed)))
                if letter in ('a', 'e', 'i', 'o', 'u'): 
                    guesses = guesses-2
                else:
                    guesses = guesses-1
                    guesses = guesses - 1
            else:
                letters_guessed.append(letter)
                print("Good guess: {}"
                      .format(get_guessed_word(secret_word,letters_guessed)))
            
            
    print("-----------")
    if is_word_guessed(secret_word,letters_guessed):
        score = guesses*len(set(secret_word))
        print("Congratulations, you won!")
        print("Your total score for this game is: {}".format(score))
    else:
        print("Sorry, you ran out of guesse. The world was {}"
              .format(secret_word))


        
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_wordAux = my_word.replace(" ", "")
    other_wordAux = other_word.replace(" ", "")
    
    if len(my_wordAux) != len(other_wordAux):
       return False
    
    for letter in my_wordAux:
        if letter not in other_wordAux and letter != '_':
            return False
   
    
    aux = my_wordAux.replace('_','')
    
    if get_guessed_word(other_word, aux) != my_word:
            return False
            
    return True
            
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    wordsFound = []
    for word in wordlist:
        if match_with_gaps(my_word,word):
            wordsFound.append(word)

    if not wordsFound:
        print('No matches found')
    else:
        print(' '.join(map(str, wordsFound)))
         
def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6 
    warming = 3
    letters_guessed = []
    print("")
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long".format(len(secret_word)))
    
    while guesses>0 and not is_word_guessed(secret_word,letters_guessed):
        print("")
        print("------------")
        print("")
        abc = get_available_letters(letters_guessed)
    
        print("You have {} guesses left".format(guesses))
        print("Available letters: {}".format(abc))
        letter = input("Please guess a letter: ")
        
        if letter == '*':
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
        
        elif len(letter) != 1 or not str.isalpha(letter):
            if warming == 0:
                guesses = guesses-1
                print("You lost a guess")
            else:
                warming = warming-1
                print("Oops! That is not a valid letter. You have {} warmings left: {}".format(warming,get_guessed_word(secret_word,letters_guessed)))
        else:
            letter = str.lower(letter)
            if letter in letters_guessed:
                if(warming == 0):
                    guesses = guesses-1
                    print("You lost a guess")
                else:
                    warming = warming-1
                    print("Oops! You had guessed this letter. You have {} warmings left: {}".format(warming,get_guessed_word(secret_word,letters_guessed)))                
            elif letter not in secret_word:
                letters_guessed.append(letter)
                print('Oops! That letter is not in my word {}'.format(get_guessed_word(secret_word,letters_guessed)))
                if letter in ('a', 'e', 'i', 'o', 'u'): 
                    guesses = guesses-2
                else:
                    guesses = guesses-1
            else:
                letters_guessed.append(letter)
                print("Good guess: {}".format(get_guessed_word(secret_word,letters_guessed)))


    print("")
    
    if is_word_guessed(secret_word,letters_guessed):
        score = guesses*len(set(secret_word))
        print("Your total score for this game is: {}".format(score))
    else:
        print("Sorry, The world is {}".format(secret_word))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    """
    secret_word = choose_word(wordlist)
    
    hangman(secret_word)
    """
###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)