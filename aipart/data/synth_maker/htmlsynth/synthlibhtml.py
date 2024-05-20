import random


class items_stuff:
    
    alphabets_U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabets_L = alphabets_U.lower()

    nums = "12345567890"

    all_stuff = alphabets_L+alphabets_U+nums

    def __init__(self) -> None:
        self.posat = 0

    def incrementpos(self):
        self.posat += 1

    def getpos(self):
        self.posat += 1
        return items_stuff.all_stuff[self.posat-1]





