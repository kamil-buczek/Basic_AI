def get_osobnik(self) -> list:
    return self.osobnik


def get_geny(self) -> list:
    geny = [_[0] for _ in self.get_osobnik()]
    return geny


def get_objetosci(self) -> list:
    obj = [_[1] for _ in self.get_osobnik()]
    return obj


def set_geny(self, geny: list):
    for number, _ in enumerate(self.get_osobnik()):
        _[0] = geny[number]


def get_objetosc_placaka(self) -> int:
    return self.objetosc_plecaka