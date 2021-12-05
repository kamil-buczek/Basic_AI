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