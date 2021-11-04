#!/usr/bin/python3

# Std
import random

# Local
from Projects.Problem_placakowy.Plecak import Plecak
from Projects.Problem_placakowy.Przedmiot import Przedmiot

# Zmienne poczatkowe
liczba_przedmiotow = 10
min_obj_przedmiotu = 10
max_obj_przedmiotu = 99
max_liczba_pokolen = 1

N = 10  # Liczba osobnikow


def generacja_przedmiotow(liczba_osobnikow) -> list:

    przedmioty = []

    for _ in range(liczba_osobnikow):
        przedmiot = Przedmiot(min_obj_przedmiotu, max_obj_przedmiotu)
        przedmioty.append(przedmiot)
    return przedmioty


def populacja_startowa() -> list:

    populacja = []

    for _ in range(N):
        nowy_osobnik = Plecak(przedmioty, objetosc_plecaka)
        populacja.append(nowy_osobnik)
    return populacja


def zycie(populacja: list):

    # Losowanie N/2 par
    max_liczba_par = int(N/2)

    print(f"Poczatkowa wielkosc populacji: {len(populacja)}")

    populacja_do_krzyzowania = populacja.copy()
    pary_do_krzyzowania = losowe_parowanie(populacja_do_krzyzowania, max_liczba_par)

    rodzice_i_dzieci = []

    for para in pary_do_krzyzowania:
        dziecko1, dziecko2 = para[0].krzyzowanie(para[1])
        rodzice_i_dzieci.append(para[0])
        rodzice_i_dzieci.append(para[1])
        rodzice_i_dzieci.append(dziecko1)
        rodzice_i_dzieci.append(dziecko2)

    print_pokolenie(rodzice_i_dzieci)


def losowe_parowanie(populacja: list, max_liczba_par: int) -> list:
    """Zwraca liste z parami osobnikow"""

    pary = []
    para = []
    liczba_par = 0

    while len(pary) < max_liczba_par:
        if len(para) < 2:
            wielkosc_populacji = len(populacja)
            losowa_liczba = random.randint(1, wielkosc_populacji)
            element = populacja.pop(losowa_liczba-1)
            para.append(element)
        else:
            liczba_par = liczba_par + 1
            # print(f"Wylosowana para {liczba_par} to: {para}")
            pary.append(para.copy())
            para.clear()
    return pary


def print_pokolenie(pokolenie: list):
    for number, _ in enumerate(pokolenie):
        print(f"Osobnik {number+1}: {_.get_geny()}")


przedmioty = generacja_przedmiotow(liczba_przedmiotow)
suma_objetosci_przedmiotow = 0

for przedmiot in przedmioty:
    suma_objetosci_przedmiotow = suma_objetosci_przedmiotow + przedmiot.get_objetosc()

print(f"Laczna objetosc wszystkich {liczba_przedmiotow} przedmiotow to {suma_objetosci_przedmiotow}")

objetosc_plecaka = int(suma_objetosci_przedmiotow / 1.5)

print(f'Objetosc plecaka to: {objetosc_plecaka}')

populacja = populacja_startowa()


for _ in range(max_liczba_pokolen):

    print(f"Pokolenie {_}")
    nowa_populacja = zycie(populacja)
    populacja = nowa_populacja