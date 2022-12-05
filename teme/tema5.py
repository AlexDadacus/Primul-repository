# ex 1
a = float(input('introdu valoarea primului nr: '))
b = float(input('introdu valoarea celui de-al doilea nr: '))


def suma_2numere(a, b):
    c = a + b
    print(f'suma celor doua nr este: {c}')


suma_2numere(a, b)
print('------------------')


# ex 2
numar = float(input('introdu numar pt a vedea daca e par/impar: '))


def adevarat_fals(numar):
    if numar % 2 == 0:
        print(True)
    elif numar % 2 != 0:
        print(False)


adevarat_fals(numar)
print('------------------')


# ex 3
nume = str(input('introdu nume: '))
prenume = str(input('introdu prenume: '))
nume_mijlociu = str(input('introdu prenume: '))


def numarare_caractere(nume, prenume, nume_mijlociu):
    t = len(nume) + len(prenume) + len(nume_mijlociu)
    print(f'Numărul total de caractere este: {t}')


numarare_caractere(nume, prenume, nume_mijlociu)
print('------------------')


# ex 4
lungime = float(input('introdu lungime dreptunghi: '))
latime = float(input('introdu latime dreptunghi: '))


def aria_dreptunghiului(lungime, latime):
    aria_d = lungime * latime
    print(f'Aria dreptunghiului este: {aria_d}')


aria_dreptunghiului(lungime, latime)
print('------------------')


# ex 5
raza = float(input('introdu raza cercului: '))


def aria_cercului(raza):
    pi = 3.14159
    aria_c = pi * (raza * raza)
    print(f'Aria cercului este: {aria_c}')


aria_cercului(raza)
print('------------------')


# ex 6
string = str(input('Introdu caractere: '))
litera = str(input('Introdu litera pentru a fi gasita: '))


def gaseste_caracter(string):
    if litera in string:
        print(True)
    else:
        print(False)


gaseste_caracter(string)
print('------------------')


# ex 7
string1 = str(input('introdu caractere pt a vedea nr caractere mici/mari: '))


def lower_upper(string1):
    carac_mici = sum(map(str.islower, string1))
    print(f'Nr de caractere lower case este {carac_mici}')
    carac_mari = sum(map(str.isupper, string1))
    print(f'Nr de caractere upper case exte {carac_mari}')


lower_upper(string1)
print('------------------')


# ex 8
lista = input('introdu lista pentru a selecta nr pozitive: ')


def lista_nr_pozitive(lista):
    lista_goala = []
    for item in lista:
        for subitem in item.split():
            if(subitem.isdigit()):
                lista_goala.append(subitem)
                for subitem in lista_goala:
                    if subitem == '0':
                        lista_goala.remove('0')
    print(lista_goala)


lista_nr_pozitive(lista)
print('------------------')


# ex 9
x = float(input('introdu valoarea lui x pentru a fi comparat: '))
y = float(input('introdu valoarea lui y pentru a fi comparat: '))


def comparatie_2numere(x, y):
    if x > y:
        print(f'Primul număr {x} este mai mare decat al doilea nr {y}')
    elif y > x:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    elif x == y:
        print('Numerele sunt egale.')


comparatie_2numere(x, y)
print('------------------')


# ex 10
nr = input('introdu numar pt a fi introdus in set: ')
set1 = input('introdu set: ')


def numar_si_set(nr, set1):
    set2 = set(set1)
    if nr in set2:
        print(f'nu am adaugat numărul {nr} în set. Acesta există deja {set2}')
        return False
    else:
        set2.add(nr)
        print(f'am adaugat numărul nou {nr} în set {set2}')
        return True


numar_si_set(nr, set1)
