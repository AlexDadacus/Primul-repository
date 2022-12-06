# ABSTRACTION
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):  # aici implementam o clasa abstracta

    PI = 3.14

    @abstractmethod   # aici implementam o metoda abstracta
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')

# INHERITANCE


class Patrat(FormaGeometrica, ABC):

    def __init__(self, __latura):   # ENCAPSULATION
        self.__latura = __latura

    def get_latura(self):
        print(f'Getter: Latura mea este: {self.__latura} ')  # getter
        return self.__latura

    def set_latura(self, noua_latura):
        self.__latura = noua_latura
        print(f'Setter: Noua latura este: {noua_latura}')  # setter

    def del_latura(self):
        self.__latura = None
        print(f'Deleter: Am sters latura')  # deleter

    def aria(self):
        aria = self.__latura * self.__latura
        print(f'aria patratului este {aria}')   # POLYMORPHISM


class Cerc(FormaGeometrica, ABC):

    def __init__(self, __raza):
        self.__raza = __raza

    def get_raza(self):
        print(f'Getter: Raza mea este: {self.__raza} ')  # getter
        return self.__raza

    def set_raza(self, noua_raza):
        self.__raza = noua_raza
        print(f'Setter: Noua raza este: {noua_raza}')  # setter

    def del_raza(self):
        self.__raza = None
        print(f'Deleter: Am sters raza')  # deleter

    def aria(self):
        aria = self.PI * (self.__raza * self.__raza)    # POLYMORPHISM
        print(f'aria este {aria}')


patrat2 = Patrat(4)
patrat2.descrie()
patrat2.get_latura()
patrat2.aria()
patrat2.set_latura(8.9)
patrat2.aria()
patrat2.del_latura()
patrat2.get_latura()
print('-----------------------------')
cerc1 = Cerc(9)
cerc1.descrie()
cerc1.get_raza()
cerc1.aria()
cerc1.set_raza(10.4)
cerc1.aria()
cerc1.del_raza()
cerc1.get_raza()
