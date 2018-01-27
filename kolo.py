class Zwierze:
    def __init__(self, imie, gatunek):
        self.imie = imie
        self.gatunek = gatunek

    def __repr__(self):
        return 'Imię: %s Gatunek: %s' % (self.imie, self.gatunek)

class Ssak(Zwierze): pass

class Ptak(Zwierze):
    def lataj(self):
        return 'Właśnie lecę!'

class Zoo:
    zwierzeta = []
    def dodaj_zwierze(self, zwierze):
        self.zwierzeta.append([zwierze]);

    def __repr__(self):
        return '%s' % self.zwierzeta


orka = Ssak('Beata', 'Orka')