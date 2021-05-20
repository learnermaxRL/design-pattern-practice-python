#task is to build a class which can construct multiple types of candies with different shape and sizes
from abc import ABC

class CandyBuilder:
    
    def set_shape(self):
        pass
        
    def set_taste(self):
        pass
        
    def set_color(self):
        pass
    
    def set_packaging(self):
        pass
    
    def __repr__(self):
        return "Shape: {0.shape} | Color: {0.color}".format(self)
    
class MangoToffee(CandyBuilder):
    
    def set_shape(self,):
         setattr(self,"shape","round")
         
    def set_taste(self):
        setattr(self,"taste","sweet")
        
    def set_color(self):
        setattr(self,"color","yellow")
        
class OrangeToffee(CandyBuilder):
    
    def set_shape(self,):
         setattr(self,"shape","round_round")
         
    def set_taste(self):
        setattr(self,"taste","sour sweet")
        
    def set_color(self):
        setattr(self,"color","orange")
        
def construct_toffee(cls):
    toffee = cls()
    toffee.set_shape()
    toffee.set_color()
    return toffee

x = construct_toffee(MangoToffee)
print(x)

y = construct_toffee(OrangeToffee)
print(y)