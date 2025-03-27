class Account:
    """Classe implementant la gestion d'un compte bancaire"""
    def __init__(self, owner,balance,currency):
        self.owner = owner
        self.balance_history = [balance]
        #self.balance=balance
        self.currency = currency
    
    def display(self):
        print(f'Le solde de {self.owner} est {self.balance_history[0]} {self.currency}')
    
    def deposit(self,amount):
        balance = self.balance_history[0] + amount
        self.balance_history.insert(0,balance)
        #append(self.balance_history)
        #return self.balance
    def withdraw(self,amount):
        if amount > self.balance_history[0]:
            print(f'Error: Not enough money available')
        else:
            balance = self.balance_history[0] - amount
            self.balance_history.insert(0,balance)
    def __getitem__(self,index):
        if index < len(self.balance_history):
            return self.balance_history[index]
        else:
            raise IndexError("Not enough transactions")
        
          
    
    
