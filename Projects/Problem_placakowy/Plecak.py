#!/usr/bin/python3

# Std
import random

# Local
from Osobnik.Osobnik import Osobnik
from libs.logger import get_logger

logger = get_logger('main')


class Plecak(Osobnik):

    najlepsze_przystosowanie = 10000000
    najlepszy_osobnik = None

    def __init__(self, przedmioty: list, obj_plecaka: int, is_dziecko=False):
        super().__init__()

        osobnik = []

        if is_dziecko:
            for przedmiot_obj in przedmioty:
                gen = [0, przedmiot_obj]
                osobnik.append(gen)
        else:
            for przedmiot in przedmioty:
                allel = random.randrange(0, 2)  # Generuje 0 lub 1
                gen = [allel, przedmiot.get_objetosc()]
                osobnik.append(gen)

        self.osobnik = osobnik
        self.objetosc_plecaka = obj_plecaka

    def get_osobnik(self) -> list:
        return self.osobnik

    def get_geny(self) -> list:
        geny = [_[0] for _ in self.get_osobnik()]
        return geny

    def get_objetosci(self) -> list:
        obj = [_[1] for _ in self.get_osobnik()]
        return obj

    def set_geny(self, geny: list):
        for number, _ in enumerate(self.get_osobnik()):
            _[0] = geny[number]

    def get_objetosc_placaka(self) -> int:
        return self.objetosc_plecaka

    def funkcja_przystosowania(self) -> float:

        suma_objetosci = 0
        osobnik = self.get_osobnik()
        obj_plecaka = self.get_objetosc_placaka()

        for _ in osobnik:
            if _[0]:
                suma_objetosci = suma_objetosci + _[1]

        przystosowanie = obj_plecaka - suma_objetosci
        return przystosowanie

    def czy_najlepszy_osobnik(self):
        """Porownuje funkcje przystosowania tego osobnika do najlepszej i ustawia na ta jezeli jest lepsza"""
        przystosowanie_osobnika = self.funkcja_przystosowania()

        if Plecak.najlepsze_przystosowanie > przystosowanie_osobnika >= 0:
            Plecak.najlepsze_przystosowanie = przystosowanie_osobnika
            Plecak.najlepszy_osobnik = self

    def krzyzowanie(self, osobnik: 'Plecak') -> ('Plecak', 'Plecak'):

        rodzic1 = self
        rodzic2 = osobnik

        liczba_genow = len(rodzic1.get_osobnik())

        logger.debug(f"Krzyzowanie osobnika {rodzic1.get_geny()} oraz {rodzic2.get_geny()}")

        dziecko1_geny = []
        dziecko2_geny = []

        for _ in range(liczba_genow):
            if _ < liczba_genow/2:
                dziecko1_geny.append(rodzic1.get_geny()[_])
                dziecko2_geny.append(rodzic2.get_geny()[_])
            else:
                dziecko1_geny.append(rodzic2.get_geny()[_])
                dziecko2_geny.append(rodzic1.get_geny()[_])

        dziecko1 = Plecak(rodzic1.get_objetosci(), rodzic1.get_objetosc_placaka(), is_dziecko=True)
        dziecko1.set_geny(dziecko1_geny)

        dziecko2 = Plecak(rodzic2.get_objetosci(), rodzic2.get_objetosc_placaka(), is_dziecko=True)
        dziecko2.set_geny(dziecko2_geny)

        logger.debug(f"Rodzic1 geny: {rodzic1.get_geny()}")
        logger.debug(f"Rodzic2 geny: {rodzic2.get_geny()}")
        logger.debug(f"Dziecko1 geny: {dziecko1.get_geny()}")
        logger.debug(f"Dziecko2 geny: {dziecko2.get_geny()}\n\n")

        return dziecko1, dziecko2

    def mutacja(self):

        logger.debug("Przeprowadzam mutację osobnika")
        liczba_genow_osobnik = len(self.osobnik)
        wylosowana_liczba = random.randrange(0, liczba_genow_osobnik)
        logger.debug(f"Mutuje gen numer {wylosowana_liczba}")
        logger.debug(f'Gen przed mutacją: {self.osobnik[wylosowana_liczba]}')

        gen = self.osobnik[wylosowana_liczba][0]
        if gen == 1:
            gen = 0
        elif gen == 0:
            gen = 1
        self.osobnik[wylosowana_liczba][0] = gen

        logger.debug(f'Gen po mutacji: {self.osobnik[wylosowana_liczba]}')
