def __init__(self, przedmioty: list, obj_plecaka: int, is_dziecko=False):
    super().__init__()

    osobnik = []

    if is_dziecko:
        for przedmiot_obj in przedmioty:
            gen = [0, przedmiot_obj]  #
            osobnik.append(gen)
    else:
        for przedmiot in przedmioty:
            allel = random.randrange(0, 2)  # Generuje 0 lub 1
            gen = [allel, przedmiot.get_objetosc()]
            osobnik.append(gen)

    self.osobnik = osobnik
    self.objetosc_plecaka = obj_plecaka