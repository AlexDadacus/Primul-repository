class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.titular_cont = titular_cont
        self.iban = iban
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self, suma):
        if suma <= self.sold:
            self.sold -= suma
            print(f'ati cheltuit {suma} de lei iar acum aveti in cont {self.sold} de lei')
        else:
            print('fonduri insuficiente')

    def creditare_cont(self, suma):
        self.sold += suma
        print(f'ati credidat {suma} de lei si aveti in cont {self.sold} de lei')
