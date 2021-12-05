def funkcja_przystosowania(self) -> float:
    suma_objetosci = 0
    osobnik = self.get_osobnik()
    obj_plecaka = self.get_objetosc_placaka()

    for _ in osobnik:
        if _[0]:
            suma_objetosci = suma_objetosci + _[1]

    przystosowanie = obj_plecaka - suma_objetosci
    return przystosowanie