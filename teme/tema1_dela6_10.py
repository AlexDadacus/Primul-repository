# ex 6
nume = input('Numele tau este: ')
print(nume)
prenume = input('Prenumele tau este: ')
print(prenume)
nume_complet = len(nume) + len(prenume)
print(f'Numele complet are: {nume_complet} caractere')

# ex 7
lungimea = int(input('Lungimea dreptunghiului este: '))
latimea = int(input('Latimea dreptunghiului este: '))
aria = lungimea * latimea
print(f'Aria dreptunghiului este: {aria}')

# ex 8
propozitie = 'Coral is either the stupidest animal or the smartest rock'
print('Cuvantul -the- apare de: ', propozitie.count(' the '), 'ori')

# ex 9
print('Cuvantul -the- apare de: ', propozitie.count(' THE '), 'ori')

# ex 10
print(propozitie.isnumeric())
assert propozitie == propozitie.isnumeric()