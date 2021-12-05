def czy_najlepszy_osobnik(self):
    """Porownuje funkcje przystosowania tego osobnika do najlepszej i ustawia na ta jezeli jest lepsza"""
    przystosowanie_osobnika = self.funkcja_przystosowania()

    if Plecak.najlepsze_przystosowanie > przystosowanie_osobnika >= 0:
        Plecak.najlepsze_przystosowanie = przystosowanie_osobnika
        Plecak.najlepszy_osobnik = self