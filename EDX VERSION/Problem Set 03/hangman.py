# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 19:50:32 2017

@author: Sebastian
"""

import string
import random

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

wordlist = load_words()    

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for secret_letter in secretWord:
        if secret_letter not in lettersGuessed:
            return False
            
    return True
    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    n1 = len(secretWord)
    n2 = len(lettersGuessed)
    guessedWord = ""
    
    for i in range(n1):
        aux = False
        for j in range(n2):
            if secretWord[i] == lettersGuessed[j]:
                aux = True
                guessedWord += secretWord[i]
                break
        if not aux:
            guessedWord += "_ "
            
    return guessedWord
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    n1 = len(lettersGuessed)
    
    abc = string.ascii_lowercase
    for i in range(n1):
        abc = abc.replace(lettersGuessed[i], "")
        
    return abc

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guesses = 8
    warming = 3
    letters_guessed = [] #list (mutable)

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    
    while guesses > 0 and not isWordGuessed(secretWord,letters_guessed):
        print("------------")
        abc = getAvailableLetters(letters_guessed)
        print("You have {} guesses left.".format(guesses))
        print("Available Letters: {}".format(abc))
        letter = input("Please guess a letter: ")
        
        
        if len(letter) != 1 or not str.isalpha(letter):
            if warming == 0:
                guesses = guesses-1
                print("You lost a guess")
            else:
                warming = warming-1
                print("Oops! That is not a valid letter. You have {} warmings left: {}".format(warming,getGuessedWord(secretWord, letters_guessed)))
        else:
            letter = str.lower(letter)
            
            if letter in letters_guessed:
                if warming == 0:
                    guesses = guesses-1
                    print("You lost a guess")
                else:
                    warming = warming-1
                    print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, letters_guessed)))                
            elif letter not in secretWord:
                letters_guessed.append(letter)
                print('Oops! That letter is not in my word: {}'.format(getGuessedWord(secretWord,letters_guessed)))
                guesses = guesses - 1
            else:
                letters_guessed.append(letter)
                print("Good guess: {}".format(getGuessedWord(secretWord,letters_guessed)))
            
            
    print("-----------")
    if isWordGuessed(secretWord,letters_guessed):
        score = guesses*len(set(secretWord))
        print("Congratulations, you won!")
        print("Your total score for this game is: {}".format(score))
    else:
        print("Sorry, you ran out of guesse. The world was {}".format(secretWord))

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    
    hangman(secret_word)
        