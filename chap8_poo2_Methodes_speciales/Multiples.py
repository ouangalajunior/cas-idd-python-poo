
class Multiples:
    def __init__(self, number, number_max = None):
        self.number = number
        self.number_max = number_max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.number_max is not None and self.current >= self.number_max-self.number:
            raise StopIteration
        
        self.current += self.number
        return self.current
        
            
        
        


for i in Multiples(3):
    
    print(i)

    
