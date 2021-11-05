#!/usr/bin/python3

# Std
import random

# Local
from Projects.Problem_placakowy.Plecak import Plecak
from Projects.Problem_placakowy.Przedmiot import Przedmiot

# Zmienne poczatkowe
liczba_przedmiotow = 100  # liczba genow
min_obj_przedmiotu = 10
max_obj_przedmiotu = 99
max_liczba_pokolen = 100
czestotliwosc_mutacji = 100  # jedna mutacja na 100 genów

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

    liczba_genow = liczba_przedmiotow

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

    mutacje_osobnikow(rodzice_i_dzieci, czestotliwosc_mutacji)
    nowa_populacja = selekcja(rodzice_i_dzieci, max_liczba_par*2)
    return nowa_populacja


def selekcja(populacja: list, max_liczba_par: int) -> list:

    pary_do_selekcji = losowe_parowanie(populacja, max_liczba_par)
    nowa_populacja = []

    for para in pary_do_selekcji:


        osobnik1 = para[0]
        osobnik2 = para[1]
        print(f"\nSelekcja turniejowa pomiedzy osobnikiem1 {osobnik1.get_geny()} a osobnikiem2 {osobnik2.get_geny()}")

        przys_osobnik1 = osobnik1.funkcja_przystosowania()
        przys_osobnik2 = osobnik2.funkcja_przystosowania()
        print(f"Przystosowanie osobnika1 to {przys_osobnik1}")
        print(f'Przystosowanie osobnika2 to {przys_osobnik2}')

        if przys_osobnik1 < 0:
            print(f"Przystosowanie {przys_osobnik1} nie spelnia warunku. Wygrywa osobnik2 {osobnik2.get_geny()}")
            nowa_populacja.append(osobnik2)


        elif przys_osobnik2 < 0:
            print(f"Przystosowanie {przys_osobnik2} nie spelnia warunku. Wygrywa osobnik1 {osobnik1.get_geny()}")
            nowa_populacja.append(osobnik1)


        elif przys_osobnik1 < przys_osobnik2:
            print(f"Wygrywa osobnik1 {osobnik1.get_geny()} z "
                  f"przystosowaniem {przys_osobnik1} i trafia on do nowego pokolenia")
            nowa_populacja.append(osobnik1)

        elif przys_osobnik2 < przys_osobnik1:
            print(f"Wygrywa osobnik2 {osobnik2.get_geny()} z "
                  f"przystosowaniem {przys_osobnik2} i trafia on do nowego pokolenia")
            nowa_populacja.append(osobnik2)


        else:
            print("Przystosowania obydwu osobnikow sa takie same. Decyduje los.")
            los = random.randrange(1, 3)  # los 1 lub 2
            if los == 1:
                print(f"Losowanie wygrywa osobnik1 {osobnik1.get_geny()}")
                nowa_populacja.append(osobnik1)

            elif los == 2:
                print(f"Losowanie wygrywa osobnik2 {osobnik2.get_geny()}")
                nowa_populacja.append(osobnik2)

            else:
                print(f"Wynik losu {los} jest bledny. Zwroc wyjatek")
                raise Exception
    return nowa_populacja


def mutacje_osobnikow(populacja: list, czestotliwosc: int):

    print(f"\nCzestotliwosc mutacji to raz na {czestotliwosc} genow")
    print(f'Liczba osobnikow w populacji to: {len(populacja)}')
    print(f'Liczba genow jednego osobnika to: {liczba_przedmiotow}')

    suma_genow = liczba_przedmiotow * len(populacja)
    ile_razy_mutacja = int(suma_genow / czestotliwosc)
    co_ile_osobnikow_mutacja = int(czestotliwosc / liczba_przedmiotow)

    print(f'Sumaryczna liczba genow to: {suma_genow}')
    print(f'Mutacja zostanie przeprowadzona {ile_razy_mutacja} razy')
    print(f'Mutacja jednego osobnika co {co_ile_osobnikow_mutacja} osobnikow')

    for numer_mutacji in range(ile_razy_mutacja):
        numer_osobnika = numer_mutacji*co_ile_osobnikow_mutacja
        osobnik_do_zmutowania = populacja[numer_osobnika]
        print(f"\n\nMutacja osobnika {numer_osobnika}")
        osobnik_do_zmutowania.mutacja()


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
            pary.append(para.copy())
            para.clear()
    return pary


def print_pokolenie(pokolenie: list):
    print("\n")
    for number, _ in enumerate(pokolenie):
        print(f"Osobnik {number+1}: {_.get_geny()}")


przedmioty = generacja_przedmiotow(liczba_przedmiotow)
suma_objetosci_przedmiotow = 0

lista_objetosci_przedmiotow = []

for przedmiot in przedmioty:
    lista_objetosci_przedmiotow.append(przedmiot.get_objetosc())
    suma_objetosci_przedmiotow = suma_objetosci_przedmiotow + przedmiot.get_objetosc()

print(f"Laczna objetosc wszystkich {liczba_przedmiotow} przedmiotow to {suma_objetosci_przedmiotow}")

objetosc_plecaka = int(suma_objetosci_przedmiotow / 1.5)

print(f'Objetosc plecaka to: {objetosc_plecaka}')
print(f"Rozmieszczenie przedmiotow: {lista_objetosci_przedmiotow}")

populacja = populacja_startowa()


for _ in range(max_liczba_pokolen):

    print(f"Pokolenie {_}")
    nowa_populacja = zycie(populacja)
    populacja = nowa_populacja
    print("\n\n______________________________________")
    print(f"PODSUMOWANIE POKOLENIE {_}")
    print(f"Objetosc plecaka: {objetosc_plecaka}")
    print(f"Najlepsze przystosowanie: {Plecak.najlepsze_przystysowanie}")
    print(f'Objetosci przedmiotow w plecaku')
    print(lista_objetosci_przedmiotow)
    print("Geny najlepszego osobnika")
    print(Plecak.najlepszy_obobnik.get_geny())
    print("______________________________________\n")