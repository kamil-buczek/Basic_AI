def krzyzowanie(self, osobnik: 'Plecak') -> ('Plecak', 'Plecak'):
    rodzic1 = self
    rodzic2 = osobnik

    liczba_genow = len(rodzic1.get_osobnik())

    logger.debug(f"Krzyzowanie osobnika {rodzic1.get_geny()} oraz {rodzic2.get_geny()}")

    dziecko1_geny = []
    dziecko2_geny = []

    punkt_krzyzowania = liczba_genow / 2

    for _ in range(liczba_genow):
        if _ < punkt_krzyzowania:  # przed punktem krzyzowania
            dziecko1_geny.append(rodzic1.get_geny()[_])
            dziecko2_geny.append(rodzic2.get_geny()[_])
        else:  # po punkcie krzyzowania
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