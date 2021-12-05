def generacja_przedmiotow(liczba_osobnikow) -> list:
    logger.info("Generacja przedmiotow, ktore mozna wlozyc do plecaka")

    przedmioty = []
    for _ in range(liczba_osobnikow):
        przedmiot = Przedmiot(min_obj_przedmiotu, max_obj_przedmiotu)
        przedmioty.append(przedmiot)
    return przedmioty