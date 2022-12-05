# ex 1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in range(len(masini)):
    print(f'Masina  mea preferata este {masini[masina]}')
print('----------------------------------------------------')
for masina in masini:
    print(f'Masina  mea preferata este {masina}')
print('----------------------------------------------------')
i = 0
while i < len(masini):
    print(f'Masina  mea preferata este {masini[i]}')
    i += 1
print('----------------------------------------------------')
# ex 2
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
i = 0
while i < (len(masini)-2):
    i += 1
    if i != masini[0] or i != masini[8]:
        masini[i] = (masini[i].upper())
        print(masini)
print('----------------------------------------------------')
# ex 3
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    print(masina)
    if masina == masini[3]:
        print('Am găsit mașina dorită de dvs')
        break
    else:
        print(f'Am găsit mașina {masina}. Mai căutam')
print('----------------------------------------------------')
# ex 4
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Trabant' or masina == 'Lăstun':
        continue
    print(f'S-ar putea să vă placă mașina: {masina}')
# ex 5
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for masina in masini:
    if masina == 'Trabant' or masina == 'Lăstun':
        masini.remove(masina)
        masini_vechi.append(masina)
        print('------------------------------------')
        if 'Trabant' or 'Lăstun' in masini_vechi:
            element = 'Tesla'
            masini.append(element)
            print(masini_vechi)
            print(masini)
print('----------------------------------------------------')
# ex 6
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
    }
lista15000 = []
for key, value in pret_masini.items():      # subpunctul 2
    if value < 15000:
        lista15000.extend({key})            # subpunctul 1
        print(f'Pentru un buget de sub 15000 euro puteți alege masina {key, value}')  # subpunctul 3
        for item in lista15000:             # subpunctul 4
            print(item)
print('----------------------------------------------------')
# ex 7
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numar3 = []
for numar in numere:
    if numar == 3:
        numar3.append(numar)
        print(f'Nr 3 apare in lista de {len(numar3)} ori')
print('----------------------------------------------------')
# ex 8
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
    suma += numar
    print(f'Suma pana la nr {numar} din lista este {suma}')
print('----------------------------------------------------')
# ex 9
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
maximum = None
for numar in numere:
    if maximum is None or maximum < numar:
        maximum = numar
        print(f'Ultimul numar cel mai mare este {maximum}')
print('----------------------------------------------------')
# ex 10
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
lista_nr_negative = []
for numar in numere:
    if numar >= 0:
        numar = numar * (-1)
        lista_nr_negative.append(numar)
        print(lista_nr_negative)
    else:
        lista_nr_negative.append(numar)
print('----------------------------------------------------')
