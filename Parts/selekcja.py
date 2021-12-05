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
            osobnik2.czy_najlepszy_osobnik()

        elif przys_osobnik2 < 0:
            logger.debug(f"Przystosowanie {przys_osobnik2} nie spelnia warunku. Wygrywa osobnik1 {osobnik1.get_geny()}")
            nowa_populacja.append(osobnik1)
            osobnik1.czy_najlepszy_osobnik()

        elif przys_osobnik1 < przys_osobnik2:
            logger.debug(f"Wygrywa osobnik1 {osobnik1.get_geny()} z "
                  f"przystosowaniem {przys_osobnik1} i trafia on do nowego pokolenia")
            nowa_populacja.append(osobnik1)
            osobnik1.czy_najlepszy_osobnik()

        elif przys_osobnik2 < przys_osobnik1:
            logger.debug(f"Wygrywa osobnik2 {osobnik2.get_geny()} z "
                  f"przystosowaniem {przys_osobnik2} i trafia on do nowego pokolenia")
            nowa_populacja.append(osobnik2)
            osobnik2.czy_najlepszy_osobnik()

        else:
            logger.debug("Przystosowania obydwu osobnikow sa takie same. Decyduje los.")
            los = random.randrange(1, 3)  # los 1 lub 2
            if los == 1:
                logger.debug(f"Losowanie wygrywa osobnik1 {osobnik1.get_geny()}")
                nowa_populacja.append(osobnik1)
                osobnik1.czy_najlepszy_osobnik()

            elif los == 2:
                logger.debug(f"Losowanie wygrywa osobnik2 {osobnik2.get_geny()}")
                nowa_populacja.append(osobnik2)
                osobnik2.czy_najlepszy_osobnik()

            else:
                logger.debug(f"Wynik losu {los} jest bledny. Zwroc wyjatek")
                raise Exception

    return nowa_populacja