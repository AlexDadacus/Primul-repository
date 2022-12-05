class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Raza cercului este {self.raza}')
        print(f'Culoarea cercului este {self.culoare}')

    def aria(self):
        pi = 3.14
        aria = pi * (self.raza * self.raza)
        print(f'Aria cercului este {aria}')

    def diametru(self):
        diametru = self.raza * 2
        print(f'diametru = {diametru}')

    def circumferinta(self):
        def diametru():
            diametru = self.raza * 2
            print(f'diametru = {diametru}')
            return diametru
        pi = 3.14
        circumferinta = pi * diametru()
        print(f'circumferinta = {circumferinta}')
