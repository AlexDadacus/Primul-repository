# ex 1
# o variabila este o cutie din memoria unui PC care contine diferite tipuri de valori

# ex 2
#variabila tip string
casa_propietar = 'Nelu Cortea'
#variabila tip integer
casa_numar = 43
#variabila tip float
venit_familie = 60.400
# variabila tip boolean
copii = True

# ex 3

print(type(casa_propietar))
print(type(casa_numar))
print(type(venit_familie))
print(type(copii))

# ex 4
venit_familie = round(venit_familie)
print(venit_familie)
print(type(venit_familie))

# ex 5
print(f'Propietarul casei este {casa_propietar}')
print(f'Casa are numarul {casa_numar}')
print(f'Venitul familiei este de {venit_familie} lei ora')
print(f'Aceasta familie are copii? >> {copii}')
