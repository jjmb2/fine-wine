#!/usr/bin/python

import random

def get_rand_index(word_array):
    return random.randint(0, len(word_array))

def main():

    with open("adjectives.txt", "r") as f:
        adjectives = f.readlines()
        adjectives = [line.strip() for line in adjectives]

    with open("nouns.txt", "r") as f:
        nouns = f.readlines()
        nouns = [line.strip() for line in nouns]

    adjective_1 = adjectives[get_rand_index(adjectives)]
    adjective_2 = adjectives[get_rand_index(adjectives)]
    noun_1 = nouns[get_rand_index(nouns)]

    print(f"A {adjective_1} wine with hints of {adjective_2} {noun_1}.")
    
if __name__ == "__main__":
    main()
