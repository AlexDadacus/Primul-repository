# ex 1
# structura if else evalueaza o conditie pusa si daca e adevarata executa ramura din if, altfel executa ramura else sau
# iese din structura
#
# ex 2
X = int(input('Alege un numar: '))
if X > 0:
    print(f'numarul {X} este numar natural')
else:
    print(f'numarul nu este natural')

# ex 3
X = int(input('Alege un numar: '))
if X > 0:
    print(f'numarul {X} este numar pozitiv')
elif X == 0:
    print(f'numarul ales e 0 si este numar neutru')
else:
    print(f'numarul {X} este numar negativ')

# ex 4
X = int(input('Alege un numar: '))
if -2 < X < 13:
    print(f'numarul {X} este in intervalul -2 si 13')
else:
    print(f'numarul {X} nu este in intervalul -2 si 13')

# ex 5
X = int(input('Alege numarul X: '))
Y = int(input('Alege numarul Y: '))
diferenta = X-Y
if diferenta < 5:
    print('Diferenta < 5')
elif diferenta == 5:
    print('Diferenta = 5')
else:
    print('Diferenta > 5')

# ex 6
X = int(input('Alege numarul X: '))
if X not in range(5, 27):
    print(f'numarul {X} nu e intervalul 5 si 27')
else:
    print(f'{X} este in intervalul 5 si 27')

# ex 7
X = int(input('Alege numarul X: '))
Y = int(input('Alege numarul Y: '))
if X == Y:
    print('Numerele alese sunt egale')
elif X > Y:
    print(f'numarul X = {X} este mai mare')
else:
    print(f'numarul Y = {Y} este mai mare')

# ex 8
X = int(input('Alege latura triunghiului X: '))
Y = int(input('Alege latura triunghiului Y: '))
Z = int(input('Alege latura triunghiului Z: '))
if (X > 0) & (Y > 0) & (Z > 0):            # pentru ca valorile sa nu fie 0 sau negative
    print('nu e nicio valoare negativa')
    if (X == Y) & (Y == Z):
        print('Triunghiul este echilateral')
    elif (X == Y) | (Y == Z) | (Z == X):
        print('Triunghiul este isoscel')
    else:
        print('Triunghiul este oarecare')
else:
    print('una sau toate valorile sunt negative/0')

# ex 9
litera = input('Alege litera: ')
prima_litera = litera[0]                  # in cazul in care se pun mai multe caractere, cerinta spune doar o litera
print(f'trebuie sa alegi o singura litera. aici primul caracter e: {litera[0]}')
vocale = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
simboluri = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=')
if prima_litera in vocale:
    print(f'{prima_litera} este vocala')
elif prima_litera.isnumeric():            # in cazul in care avem numar primul caracter
    print(f'{prima_litera} e un numar')
elif prima_litera in simboluri:
    print(f'{prima_litera} este simbol')  # in cazul in care avem simbol primul caracter
else:
    print(f'{prima_litera} este consoana')

# ex 10
note_ro = float(input('nota elevului roman: '))
nota = round(note_ro)
print(nota)
if nota in range(1, 4):
    nota = 'F'
    print(f'Nota transformata este {nota}')
elif nota in range(4, 6):
    nota = 'E'
    print(f'Nota transformata este {nota}')
elif nota in range(6, 7):
    nota = 'D'
    print(f'Nota transformata este {nota}')
elif nota in range(7, 8):
    nota = 'C'
    print(f'Nota transformata este {nota}')
elif nota in range(8, 9):
    nota = 'B'
    print(f'Nota transformata este {nota}')
elif nota in range(9, 11):              # aici nu ia capatul, n-am gasit ceva sa includ si endpoint-ul
    nota = 'A'
    print(f'Nota transformata este {nota}')
else:
    print(f'nota nu exista')
