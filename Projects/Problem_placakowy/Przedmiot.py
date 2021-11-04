#!/usr/bin/python3

# Std
import random


class Przedmiot():

    def __init__(self, min_objetosc, max_objetosc):

        self.objetosc = random.randrange(min_objetosc, max_objetosc + 1)

    def get_objetosc(self) -> int:
        return self.objetosc
