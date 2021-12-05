def sprawdzenie_wyniku(najlepsze_przystosowanie: int, najlepsze_geny: list, przedmioty: list, objetosc_plecaka):

    if len(najlepsze_geny) == len(przedmioty):
        logger.info("Sprawdzenie wyniku")
        suma = 0

        end_string = '0'

        for _ in range(len(przedmioty)):
            if najlepsze_geny[_]:
                logger.debug(f"Suma przed dodaniem: {suma}")
                logger.debug(f'Dodaje przedmiot o objetosci: {przedmioty[_]}')
                suma = suma + przedmioty[_]
                end_string = end_string + f'+{przedmioty[_]}'
                logger.debug(f'Suma po dodaniu: {suma}')

        logger.info(f"Suma przedmiotow wlozonych do pleacka to: {suma}")
        logger.info(f"Objetosc plecaka to: {objetosc_plecaka}")
        roznica = objetosc_plecaka - suma
        logger.info(f"Pozostalo miejsca w plecaku: {roznica}")
        logger.info(f'Koncowy string dodawania to: {end_string}')

        if roznica != najlepsze_przystosowanie:
            err_mgs = f'Pozostałe miejsce w plecaku= {roznica} nie zgadza się z najlepszym przystosowaniem= {najlepsze_przystosowanie}'
            logger.error(err_mgs)
            raise Exception(err_mgs)
        else:
            logger.info("Pozostałem miejsce w plecaku zgadza się z najlepszym przystosowaniem")

    else:
        logger.error("Dlugosc listy z ganami i przedmiotami nie jest taka sama. Bład w algorytmie.")
        raise Exception