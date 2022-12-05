from clasaCont import Cont

cont1 = Cont('RO222222', 'Alex Dadacus', 100)
cont2 = Cont('RO333333', 'Roxana Dadacus', 1500)

cont1.afisare_sold()
cont1.debitare_cont(150)
cont1.creditare_cont(1000)
print('----------------------')
cont2.afisare_sold()
cont2.debitare_cont(1000)
cont2.creditare_cont(2000)
