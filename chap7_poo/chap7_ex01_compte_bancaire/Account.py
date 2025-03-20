
class Account:
    """Classe implementant la gestion d'un compte bancaire"""
    def __init__(self, owner,balance,currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency
    
    def display(self):
        print(f'Le solde de {self.owner} est {self.balance} {self.currency}')
    
    def deposit(self,amount):
        self.balance += amount
        #return self.balance
    def withdraw(self,amount):
        if amount > self.balance:
              print(f'Error: Not enough money available')
        else:
            self.balance -= amount
    

                    

#a = Account(owner='Paul', balance=200, currency='CHF')
#a.display()
#if __name__ == "__main__" :
    