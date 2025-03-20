class Multiples:

    def __init__(self, number):
        self.number = number
        self.current = 0
    
    def next(self):
        
        self.current += self.number
        return self.current