#!/usr/bin/python3

# Std
import random
import argparse

# Local
from Projects.Problem_placakowy.Plecak import Plecak
from Projects.Problem_placakowy.Przedmiot import Przedmiot
from libs.logger import get_logger, set_logger

logger = get_logger('main')

# Zmienne poczatkowe
liczba_przedmiotow = 100  # liczba genow
min_obj_przedmiotu = 10
max_obj_przedmiotu = 99
max_liczba_pokolen = 100
czestotliwosc_mutacji = 1000  # jedna mutacja na 1000 genów

N = 100  # Liczba osobnikow

# Warunek stopu
max_liczba_pokolen_z_takim_samym_wynikiem = 5


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug",
                    help='Turn on debugging mode',
                    action="store_true")
    return parser.parse_args()


def show_basic_info():
    print("\nPodstawowe informacje o programie".upper())
    print(f"Liczba przedmiotow w plecaku/osobnikow: {liczba_przedmiotow}")
    print(f"Minimalna objetosc przedmiotu: {min_obj_przedmiotu}")
    print(f"Maksymalna objetosc przedmiotu: {max_obj_przedmiotu}")
    print(f"Liczba pokolen: {max_liczba_pokolen}")
    print(f"Czestotliwosc mutacji to raz na {czestotliwosc_mutacji} genow")
    print(f"\nWARUNKI STOPU:")
    print(f"Maxymalna liczba pokolen z takim samym wynikiem: {max_liczba_pokolen_z_takim_samym_wynikiem}")


def generacja_przedmiotow(liczba_osobnikow) -> list:
    logger.info("Generacja przedmiotow, ktore mozna wlozyc do plecaka")

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

    logger.info(f"Poczatkowa wielkosc populacji: {len(populacja)}")

    populacja_do_krzyzowania = populacja.copy()
    logger.info("Tworzenie losowych par do krzyzowania")
    pary_do_krzyzowania = losowe_parowanie(populacja_do_krzyzowania, max_liczba_par)

    rodzice_i_dzieci = []

    logger.info("Krzyzowanie")
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

    logger.info("Selekcja")
    pary_do_selekcji = losowe_parowanie(populacja, max_liczba_par)
    nowa_populacja = []

    for para in pary_do_selekcji:

        osobnik1 = para[0]
        osobnik2 = para[1]
        logger.debug(f"\nSelekcja turniejowa pomiedzy osobnikiem1 {osobnik1.get_geny()} a osobnikiem2 {osobnik2.get_geny()}")

        przys_osobnik1 = osobnik1.funkcja_przystosowania()
        przys_osobnik2 = osobnik2.funkcja_przystosowania()
        logger.debug(f"Przystosowanie osobnika1 to {przys_osobnik1}")
        logger.debug(f'Przystosowanie osobnika2 to {przys_osobnik2}')

        if przys_osobnik1 < 0:
            logger.debug(f"Przystosowanie {przys_osobnik1} nie spelnia warunku. Wygrywa osobnik2 {osobnik2.get_geny()}")
            nowa_populacja.append(osobnik2)

        elif przys_osobnik2 < 0:
            logger.debug(f"Przystosowanie {przys_osobnik2} nie spelnia warunku. Wygrywa osobnik1 {osobnik1.get_geny()}")
            nowa_populacja.append(osobnik1)

        elif przys_osobnik1 < przys_osobnik2:
            logger.debug(f"Wygrywa osobnik1 {osobnik1.get_geny()} z "
                  f"przystosowaniem {przys_osobnik1} i trafia on do nowego pokolenia")
            nowa_populacja.append(osobnik1)

        elif przys_osobnik2 < przys_osobnik1:
            logger.debug(f"Wygrywa osobnik2 {osobnik2.get_geny()} z "
                  f"przystosowaniem {przys_osobnik2} i trafia on do nowego pokolenia")
            nowa_populacja.append(osobnik2)

        else:
            logger.debug("Przystosowania obydwu osobnikow sa takie same. Decyduje los.")
            los = random.randrange(1, 3)  # los 1 lub 2
            if los == 1:
                logger.debug(f"Losowanie wygrywa osobnik1 {osobnik1.get_geny()}")
                nowa_populacja.append(osobnik1)

            elif los == 2:
                logger.debug(f"Losowanie wygrywa osobnik2 {osobnik2.get_geny()}")
                nowa_populacja.append(osobnik2)

            else:
                logger.debug(f"Wynik losu {los} jest bledny. Zwroc wyjatek")
                raise Exception

    return nowa_populacja


def mutacje_osobnikow(populacja: list, czestotliwosc: int):

    logger.info("Mutacja")
    logger.debug(f"\nCzestotliwosc mutacji to raz na {czestotliwosc} genow")
    logger.debug(f'Liczba osobnikow w populacji to: {len(populacja)}')
    logger.debug(f'Liczba genow jednego osobnika to: {liczba_przedmiotow}')

    suma_genow = liczba_przedmiotow * len(populacja)
    ile_razy_mutacja = int(suma_genow / czestotliwosc)
    co_ile_osobnikow_mutacja = int(czestotliwosc / liczba_przedmiotow)

    logger.debug(f'Sumaryczna liczba genow to: {suma_genow}')
    logger.debug(f'Mutacja zostanie przeprowadzona {ile_razy_mutacja} razy')
    logger.debug(f'Mutacja jednego osobnika co {co_ile_osobnikow_mutacja} osobnikow')

    for numer_mutacji in range(ile_razy_mutacja):
        numer_osobnika = numer_mutacji*co_ile_osobnikow_mutacja
        osobnik_do_zmutowania = populacja[numer_osobnika]
        logger.debug(f"Mutacja osobnika {numer_osobnika}")
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
        logger.info(f"Osobnik {number+1}: {_.get_geny()}")


def sprawdzenie_wyniku(najlepsze_przystosowanie: int, najlepsze_geny: list, przedmioty: list, objetosc_plecaka):

    if len(najlepsze_geny) == len(przedmioty):
        logger.info("Sprawdzenie wyniku")
        suma = 0
        for _ in range(len(przedmioty)):
            if najlepsze_geny[_]:
                suma = suma + przedmioty[_]
        logger.info(f"Suma przedmiotow wlozonych do pleacka to: {suma}")
        logger.info(f"Objetosc plecaka to: {objetosc_plecaka}")
        roznica = objetosc_plecaka - suma
        logger.info(f"Pozostalo miejsca w plecaku: {roznica}")
    else:
        logger.error("Dlugosc listy z ganami i przedmiotami nie jest taka sama. Bład w algorytmie.")
        raise Exception


if __name__ == '__main__':

    args = parse_arguments()
    debug = args.debug
    set_logger('main', debug)

    show_basic_info()

    print("\n")
    logger.info("Rozpoczynam działanie algorytmy generycznego")

    przedmioty = generacja_przedmiotow(liczba_przedmiotow)
    suma_objetosci_przedmiotow = 0

    lista_objetosci_przedmiotow = []
    for przedmiot in przedmioty:
        lista_objetosci_przedmiotow.append(przedmiot.get_objetosc())
        suma_objetosci_przedmiotow = suma_objetosci_przedmiotow + przedmiot.get_objetosc()

    logger.info(f"Laczna objetosc wszystkich {liczba_przedmiotow} przedmiotow to {suma_objetosci_przedmiotow}")

    objetosc_plecaka = int(suma_objetosci_przedmiotow / 1.5)

    logger.info(f'Objetosc plecaka to: {objetosc_plecaka}')
    logger.info(f"Rozmieszczenie przedmiotow w plecaku: {lista_objetosci_przedmiotow}")

    logger.info("Generacja populacji startowej")
    populacja = populacja_startowa()
    pokolenie = 1

    liczba_pokolen_z_takim_samym_wynikiem = 0
    poprzedni_wynik = 0

    for pokolenie in range(1, max_liczba_pokolen+1):
        print("\n")
        logger.info(f"Pokolenie {pokolenie}")
        nowa_populacja = zycie(populacja)
        populacja = nowa_populacja
        najlepsze_przystosowane = Plecak.najlepsze_przystysowanie
        logger.info(f"Najlepsze przystosowanie w tym pokoleniu to: {najlepsze_przystosowane}")

        if pokolenie == 1:
            # Jeżeli pierwsze pokolenie
            poprzedni_wynik = najlepsze_przystosowane
            liczba_pokolen_z_takim_samym_wynikiem = liczba_pokolen_z_takim_samym_wynikiem + 1
        else:
            # Jeżeli każde kolejne pokolenie
            if poprzedni_wynik == najlepsze_przystosowane:
                liczba_pokolen_z_takim_samym_wynikiem = liczba_pokolen_z_takim_samym_wynikiem + 1
                logger.info(f"Ilosc pokolen z takim samym "
                            f"najlepszym przystosowaniem to: {liczba_pokolen_z_takim_samym_wynikiem}")
            else:
                poprzedni_wynik = najlepsze_przystosowane
                liczba_pokolen_z_takim_samym_wynikiem = 0

        # Warunki stopu
        # Jeżeli znaleziono najlepsze mozliwe rozwiazanie
        if najlepsze_przystosowane == 0:
            logger.info("Znaleziono najlepsze rozwiazanie problemu. Maksymalne zapełnienie plecaka")
            break
        # Jezeli przez okreslona ilosc pokolen jest ten sam wynik
        if liczba_pokolen_z_takim_samym_wynikiem > max_liczba_pokolen_z_takim_samym_wynikiem:
            logger.info(f"Ilosc pokolen z tym samym najlepszym przystosowaniem "
                        f"jest wieksza od {max_liczba_pokolen_z_takim_samym_wynikiem}. Przerywam działanie programu.")
            break


    print("\n\n_______________________________________________________________________________________________________")
    logger.info(f"PODSUMOWANIE POKOLENIA {pokolenie}")
    logger.info(f"Objetosc plecaka: {objetosc_plecaka}")
    logger.info(f"Najlepsze przystosowanie: {Plecak.najlepsze_przystysowanie}")
    logger.info(f'Objetosci przedmiotow w plecaku')
    logger.info(lista_objetosci_przedmiotow)
    logger.info("Geny najlepszego osobnika")
    logger.info(Plecak.najlepszy_osobnik.get_geny())
    print("_______________________________________________________________________________________________________\n")
    sprawdzenie_wyniku(Plecak.najlepsze_przystysowanie, Plecak.najlepszy_osobnik.get_geny(),
                       lista_objetosci_przedmiotow, objetosc_plecaka)
