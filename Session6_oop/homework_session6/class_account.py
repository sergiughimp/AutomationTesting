'''
4.Clasa Cont
    Atribute: iban, titular_cont, sold
    Constructor pentru toate atributele
    Metode:
        ● afisare_sold() - Titularul x are în contul y suma de n lei
        ● debitare_cont(suma)
        ● creditare_cont(suma)
'''

class Account:
    def __init__(self, iban, account_holder, sold):
        self.iban = iban
        self.account_holder = account_holder
        self.sold = sold

    def show_sold(self):
        print(f"The account holder {self.account_holder} with iban {self.iban} has ${self.sold} in his sold")
    def debit_account(self, amount):
        self.sold += amount
        print(f"You debited the account with ${amount} and now you have ${self.sold} in you sold")
    def credit_account(self, amount):
        if amount > self.sold:
            print(f"The amount {amount} that you want to credit is to big. Try a lower amount")
        else:
            self.sold -= amount
            print(f"You credited your sold with ${amount}, now you have {self.sold} in you account ")

account1 = Account("RO001", "Tom", 345)
account1.show_sold()
account1.debit_account(35)
account1.credit_account(35)