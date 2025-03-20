import math
class Fraction:
    def __init__(self,numerateur,denominateur =1):
        if denominateur == 0:
            raise ValueError("Le dénominateur ne peut pas être zéro.")
        pgcd = math.gcd(numerateur, denominateur)
        self.numerateur =numerateur //pgcd
        self.denominateur = denominateur //pgcd

    
    def display(self):
        
        if self.denominateur == 1 :
            print(f'{self.numerateur}')
        else:
            print(f'{self.numerateur}/{self.denominateur}')
    
    def neg(self):
        """ Retourne la forme négative"""
        return Fraction(-self.numerateur,self.denominateur)
    
    def add(self,f):
        """Somme de fraction """
        num =self.numerateur*f.denominateur + self.denominateur*f.numerateur
        den=self.denominateur*f.denominateur
        return Fraction(num, den)
    
    def sub(self,f):
        """Difference de fraction """
        num =self.numerateur*f.denominateur - self.denominateur*f.numerateur
        den=self.denominateur*f.denominateur
        return Fraction(num, den)
    
    def mul(self,f):
        """Produit de fraction """
        num =self.numerateur*f.numerateur
        den=self.denominateur*f.denominateur
        return Fraction(num, den)
        

        
