# ex 1
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)
print('-----------------')
# ex 2
print(note_muzicale.count('do'))
print('-----------------')
# ex 3
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
lista_unita = list1 + list2     # metoda 1
print(lista_unita)
list1.extend(list2)             # metoda 2
print(list1)
print('-----------------')
# ex 4
list1.sort()
print(list1)
list1.pop(0)
print(list1)
print('-----------------')
# ex 5
if not list1:
    print('lista e goala')
else:
    print('linsta nu e goala')
print('-----------------')
# ex 6
list1.clear()
print(list1)    # verific si prin print daca am sters lista
print('-----------------')
# ex 7
if not list1:
    print('lista e goala')
else:
    print('linsta nu e goala')
print('-----------------')
# ex 8
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())
print('-----------------')
# ex 9
print(f'Ana a luat nota {dict1["Ana"]}, Gigel a luat nota {dict1["Gigel"]}, Dorel a luat nota {dict1["Dorel"]}')
print('-----------------')
# ex 10
dict1["Dorel"] = 6
print(dict1["Dorel"])
print(dict1)
print('-----------------')
# ex 11
dict1.pop("Gigel")
print(dict1)
dict1.update(Ionica=9)
print(dict1)
print('-----------------')
# ex 12
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')  # setul nu poate contine duplicate
print(zile_sapt)
print('-----------------')
# ex 13
if weekend.issubset(zile_sapt):
    print('setul weekend este un subset al setului zilele_sapt')
else:
    print('weekend nu este subset')
print('-----------------')
# ex 14
print(zile_sapt.difference(weekend))    # diferenta dintre zile_sapt si weekend
print(weekend.difference(zile_sapt))
print('-----------------')
# ex 15
intersectia_seturi = zile_sapt.intersection(weekend)
print(intersectia_seturi)
