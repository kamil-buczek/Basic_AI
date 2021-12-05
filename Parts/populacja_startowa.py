def populacja_startowa(przedmioty: list) -> list:

    populacja = []
    for _ in range(N):
        nowy_osobnik = Plecak(przedmioty, objetosc_plecaka)
        populacja.append(nowy_osobnik)
    return populacja