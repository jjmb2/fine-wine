#!/usr/bin/python

import random

def getRandIndex(word_array):
    return random.randint(0, len(word_array))

def main():

    with open("adjectives.txt", "r") as f:
        adjectives = f.readlines()
        adjectives = [line.strip() for line in adjectives]

    with open("nouns.txt", "r") as f:
        nouns = f.readlines()
        nouns = [line.strip() for line in nouns]

    adjective_1 = adjectives[getRandIndex(adjectives)]
    adjective_2 = adjectives[getRandIndex(adjectives)]
    noun_1 = nouns[getRandIndex(nouns)]

    print(f"A {adjective_1} wine with hints of {adjective_2} {noun_1}.")
    
if __name__ == "__main__":
    main()
