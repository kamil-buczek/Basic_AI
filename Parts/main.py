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

    # objetosc_plecaka = int(suma_objetosci_przedmiotow / 1.5)
    objetosc_plecaka = calokowita_objetosc_plecaka

    logger.info(f'Objetosc plecaka to: {objetosc_plecaka}')
    logger.info(f"Rozmieszczenie przedmiotow w plecaku: {lista_objetosci_przedmiotow}")

    logger.info("Generacja populacji startowej")
    populacja = populacja_startowa(przedmioty)
    pokolenie = 1

    liczba_pokolen_z_takim_samym_wynikiem = 0
    poprzedni_wynik = 0

    for pokolenie in range(1, max_liczba_pokolen+1):
        print("\n")
        logger.info(f"Pokolenie {pokolenie}")
        nowa_populacja = zycie(populacja)
        populacja = nowa_populacja
        najlepsze_przystosowane = Plecak.najlepsze_przystosowanie
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
    logger.info(f"Najlepsze przystosowanie: {Plecak.najlepsze_przystosowanie}")
    logger.info(f'Objetosci przedmiotow w plecaku')
    logger.info(lista_objetosci_przedmiotow)
    logger.info("Geny najlepszego osobnika")
    logger.info(Plecak.najlepszy_osobnik.get_geny())
    print("_______________________________________________________________________________________________________\n")
    sprawdzenie_wyniku(Plecak.najlepsze_przystosowanie, Plecak.najlepszy_osobnik.get_geny(),
                       lista_objetosci_przedmiotow, objetosc_plecaka)
