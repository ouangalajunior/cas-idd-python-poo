import math
class Fraction:
    '''
    >>> f = Fraction(2,3)
    >>> f
    2/3
    >>> f = Fraction(4,6)
    >>> f
    2/3
    >>> -f
    -2/3
    >>> g = Fraction(4)
    >>> g
    4
    >>> print(f+g)
    14/3
    >>> print(f-g)
    -10/3
    >>> print(f*g)
    8/3
    
    '''

  
    def __init__(self,numerateur,denominateur =1):
        if denominateur == 0:
            raise ValueError("Le dénominateur ne peut pas être zéro.")
        pgcd = math.gcd(numerateur, denominateur)
        self.numerateur =numerateur //pgcd
        self.denominateur = denominateur //pgcd
    
    def __repr__(self):
        """Affiche la fraction sous une forme lisible dans l'interpréteur."""
        return str(self)
    
    def __str__(self):
        """Affiche la fraction sous forme lisible."""
        return str(self.numerateur) if self.denominateur==1 else f"{self.numerateur}/{self.denominateur}"

    """ 
    def display(self):
        
        if self.denominateur !=1:
            print("%d/%d" % (self.numerateur,self.denominateur))
        else:
            print("%d" % self.numerateur) """
    def __neg__(self):
        """ Retourne la forme négative"""
        return Fraction(-self.numerateur,self.denominateur)
    
    def __add__(self,f):
        """Somme de fraction """
        num =self.numerateur*f.denominateur + self.denominateur*f.numerateur
        den=self.denominateur*f.denominateur
        return Fraction(num, den)
    
    def __sub__(self,f):
        """Difference de fraction """
        num =self.numerateur*f.denominateur - self.denominateur*f.numerateur
        den=self.denominateur*f.denominateur
        return Fraction(num, den)
    
    def __mul__(self,f):
        """Produit de fraction """
        num =self.numerateur*f.numerateur
        den=self.denominateur*f.denominateur
        return Fraction(num, den)
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()