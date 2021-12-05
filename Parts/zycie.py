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