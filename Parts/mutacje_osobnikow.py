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