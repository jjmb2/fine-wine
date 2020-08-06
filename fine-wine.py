#!/usr/bin/python

def main():

    with open("adjectives.txt", "r") as f:
        adjectives = f.readlines()
        adjectives = [line.strip() for line in adjectives]

    with open("nouns.txt", "r") as f:
        nouns = f.readlines()
        nouns = [line.strip() for line in nouns]

if __name__ == "__main__":
    main()
