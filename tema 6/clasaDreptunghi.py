class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self. culoare = culoare

    def descrie(self):
        print(f'Dreptunghiul are lungimea = {self.lungime}, latimea = {self.latime} si culoarea {self.culoare}')

    def aria(self):
        aria = self.lungime * self.latime
        print(f'Aria dreptunghiului = {aria}')

    def perimetrul(self):
        perimetrul = 2 * (self.lungime + self. latime)
        print(f'Perimetrul dreptunghiului = {perimetrul}')

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare
