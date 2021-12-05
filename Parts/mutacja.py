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