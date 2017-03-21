'''
Harvey Mudd College - CS for All
Problem Name: Scrabble Scoring
Topic: Finding the higest score in a Scrabble rack
Lectures: Module 1, Lecture 1
URL: https://www.cs.hmc.edu/twiki/bin/view/ModularCS1/ScrabbleScoring!
'''
from sys import argv, exit
from collections import Counter

from resources.words import DICT # Dictionary of English words

SCORES = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1,
          "f": 4, "g": 2, "h": 4, "i": 1, "j": 8,
          "k": 5, "l": 1, "m": 3, "n": 1, "o": 1,
          "p": 3, "q": 10, "r": 1, "s": 1, "t": 1,
          "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10}


def validWord(word, rack):
    '''Checks to see if the rack can complete a given word'''
    word2, word1 = Counter(word), Counter(rack)
    return all(word2[k] <= word1.get(k, 0) for k in word2)


def scoreWord(word):
    '''Scores a word based on the Scrabble point system'''
    return sum(SCORES[i] for i in word)


def scoreList(rack):
    '''Returns list of lists containing [score: word]'''
    results = []
    for word in DICT:
        if validWord(word, rack):
            results.append([scoreWord(word), word])
    results.sort(reverse=True)
    return results


def bestWord(results):
    '''Determines which word is the best based on score'''
    best_score = max([i[0] for i in results]) 
    words = list(i[1] for i in results if i[0] == best_score)
    if len(words) == 1:
        word = words[0]
    else:
        # if there are more than one word with the same (best) score
        # import random.choice to random select which word to play.
        from random import choice
        word = choice(words)
    return word, best_score


if __name__ == '__main__':
    try:
        print()
        print(bestWord(scoreList([i for i in argv[1]])))
    except IndexError:
        rack = input('What is your Scrabble rack? ')
        if rack:
            print(bestWord(scoreList([i for i in rack])))
        else:
            print('Either rack not entered or not entered as a series of letters')
            print('System exiting...')
            exit(1)
    finally:
        print()


