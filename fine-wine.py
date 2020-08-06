#!/usr/bin/python

import random

def txt_to_list(file_name):
    with open(file_name, "r") as f:
        word_list = f.readlines()
        word_list = [line.strip() for line in word_list]
    return word_list

def get_rand_index(word_array):
    return random.randint(0, len(word_array))

def print_description(adjective_1, adjective_2, noun_1):
    if adjective_1[0] in ['a','e','i','o','u']:
        article = 'An'
    else:
        article = "A"

    print(f"{article} {adjective_1} wine with hints of {adjective_2} {noun_1}.")

def main():

    adjectives = txt_to_list("adjectives.txt")
    nouns = txt_to_list("nouns.txt")

    adjective_1 = adjectives[get_rand_index(adjectives)]
    adjective_2 = adjectives[get_rand_index(adjectives)]
    noun_1 = nouns[get_rand_index(nouns)]

    print_description(adjective_1, adjective_2, noun_1)
    
if __name__ == "__main__":
    main()
