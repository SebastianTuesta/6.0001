# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 19:34:05 2017

@author: Sebastian
"""

# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    wordAux = word.lower()
    
    component1 = 0
    for i in wordAux:
        component1 += SCRABBLE_LETTER_VALUES.get(i,0)
    
    component2 = len(wordAux)
    
    answer = component1*component2
    
    if component2 == n:
        answer += 50
    return answer
    

#
# Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    new_hand = hand.copy()
    
    for letter in word.lower():
        if new_hand.get(letter, 0) != 0:
            new_hand[letter] -= 1
            if new_hand[letter] == 0:
                del new_hand[letter]

    return new_hand

#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > hand.get(letter,0):
            return False

#
# Problem #5: Playing a hand
#
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    sum_ = 0
    for i in hand:
        sum_ += hand[i]

    return sum_

    
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE (download ps4a.py to see)
    new_hand = hand.copy()
    total_points_hand = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(new_hand) > 0:        
        # Display the hand
        print("Current Hand: ", end="")
        displayHand(new_hand)
        
        # Ask user for input
        word = input("Enter word, or a \".\" to indicate that you are finished: ")
        # If the input is two exclamation points:
        if word == '.':
            """
            CODE HELP:
                DIFFERENCE BETWEEN ... == ...  and ... is ...
                    An is expression evaluates to True if two variables point to the same (identical) object.

                    An == expression evaluates to True if the objects referred to by the variables are equal (have the same contents).
            """
            
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not two exclamation points):
        else:
            
            # If the word is valid:
            
            if isValidWord(word,new_hand, wordList):
                word_points = getWordScore(word, n)
                total_points_hand += word_points
                print("\" {} \" earned {}  points. Total:  {}  points"
                      .format(word,word_points,total_points_hand))
                # Tell the user how many points the word earned,
                # and the updated total score
                new_hand = updateHand(new_hand, word)
            # Otherwise (the word is not valid):
            else:
                print("Invalid word, please try again.")
                # Reject invalid word (print a message)
               
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print()
    if word == '.':
        print("Goodbye! Total score:  {} points.".format(total_points_hand))
    else:
        print("Ran out of letter. Total score :  {}  points".format(total_points_hand))

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.
 
    This word should be calculated by considering all the words
    in the wordList.
 
    If no words in the wordList can be made from the hand, return None.
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
 
    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
     
    # For each word in the wordList
    for word in wordList:
     
     
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
 
            # Find out how much making that word is worth
            score = getWordScore(word, HAND_SIZE)
            # If the score for that word is higher than your best score
            if maxScore < score:
                # Update your best score, and best word accordingly
                maxScore = score
                bestWord = word
 
    # return the best word you found.
    return bestWord
        
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.
 
    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
  
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    totalScore = 0
     
    while calculateHandlen(hand) > 0:
     
        print("Current Hand:")
        displayHand(hand)
         
        word = compChooseWord(hand, wordList)
        print("Computer entered: {}".format(word))
        #print "Computer entered:", word
         
        if word == None:
            break;
        else:
            points = getWordScore(word, HAND_SIZE)
            totalScore += points
            print('\" {} \" earned {} points. Total: {} points'
                  .format(word, points, totalScore))
             
            hand = updateHand(hand, word)
                 
    print("Total score: {} points.".format(totalScore))
    

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    """
    boolean = False
    
    while True:
        chooseOption = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if chooseOption == 'e':
            break
        elif chooseOption == 'n':
            lastHand = dealHand(HAND_SIZE)
            playHand(lastHand, wordList, HAND_SIZE)
            boolean = True
        elif chooseOption == 'r':
            if boolean:
                playHand(lastHand, wordList, HAND_SIZE)
            else:
                print("You have not played a hand yet. Please play a new hand first!")
        else:
            print("Invalid command.")
    """
    
    boolean = False
    
    while True:
        chooseOption = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if chooseOption == 'n':
            while True:
                chooseOption = input("Enter u to have yourself play, c to have the computer play: ")
                
                if chooseOption == 'u':
                    lastHand = dealHand(HAND_SIZE)
                    playHand(lastHand, wordList, HAND_SIZE)
                    boolean = True
                    break
                elif chooseOption == 'c':
                    lastHand = dealHand(HAND_SIZE)
                    compPlayHand(lastHand, wordList, HAND_SIZE)
                    boolean = True
                    break
                else: 
                    print("Invalid command.")
        elif chooseOption == 'r':
            if boolean:
                chooseOption = input("Enter u to have yourself play, c to have the computer play: ")
            
                if chooseOption == 'u':
                    playHand(lastHand, wordList, HAND_SIZE)
                elif chooseOption == 'c':
                    compPlayHand(lastHand, wordList, HAND_SIZE)
            else:
                print("You have not played a hand yet. Please play a new hand first!")
        elif chooseOption == 'e':
            break
        else:
            print("Invalid command.")
#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#

if __name__ == '__main__':
    word_list = load_words()
    playGame(word_list)
    