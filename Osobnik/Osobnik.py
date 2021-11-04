#!/usr/bin/python3

# Std
from abc import abstractmethod, ABC


class Osobnik(ABC):

    def __init__(self):
        pass

    def mutacja(self):
        pass

    def krzyzowanie(self, osobnik: 'Osobnik') -> ('Osobnik', 'Osobnik'):
        pass


