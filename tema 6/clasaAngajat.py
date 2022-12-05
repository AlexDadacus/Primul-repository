class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Angajatul: {self.nume}')

    def nume_complet(self):
        print(f'Numele complet al angajatului este: {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar al anagajatului este: {self.salariu} de lei')

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        print(f'Salariul anual al angajatului este: {salariu_anual} lei')

    def marire_salariu(self, procent):

        self.salariu_lunar()
        procent1 = (procent/100) * self.salariu
        print(f'Procentul cu care va fi marit salariul lunar este de {procent} la suta')
        noul_salariu_lunar = procent1 + self.salariu
        print(f'Noul salariu lunar este: {noul_salariu_lunar} de lei')

        self.salariu_anual()
        noul_salariu_anual = noul_salariu_lunar * 12
        print(f'Noul salariu anual este: {noul_salariu_anual} de lei')
