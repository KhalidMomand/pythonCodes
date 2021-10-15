#!/usrs/bin/env python3

class Polynomial:

   
   #__init__ method is used to initialize the instance of the class 
   def __init__(self,*coeffs):
      self.coeffs = coeffs


   
   #__repr__ method is used to give extra information about the class.
   def __repr__(self):
      return 'Polynomial(*{!r})'.format(self.coeffs)


   
   #__add__ method is used to add instances of this class togther.
   def __add__(self,other):

      return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))
   

   #__len__ method is used to show len of instance/instances of this class.
   def __len__(self):
      return len(self.coeffs)





p1 = Polynomial(1, 2, 3)
p2 = Polynomial(1, 2, 3)


print(len(p1))
print(len(p2))



