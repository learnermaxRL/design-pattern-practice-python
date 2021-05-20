
from typing import Any
import sys
import random

class Animal:
    
    def walk(self):
        pass
    
    def talk(self):
        pass
    
class Dog(Animal):
    def bark():
        return "Bhow"
    
class Whale(Animal):
    
    def moo():
        return "moo"
    
    
class AnimalFactory:
    
    @classmethod
    def get_object(cls,classname :str)->Any:
        
        return type(classname)()
        # return getattr(sys.modules[__name__],classname)()
        
class Birds:
    
    def walk(self):
        pass
    
    def talk(self):
        pass
    

class Peigon(Birds):
    def chirp():
        return "****"
    
class Crow(Birds):
    
    def __init__(self) -> None:
        super().__init__()
        if hasattr(self,'r'):
            print("Already has r")
        else:
            self.r = random.randrange(10)
            print(self.r)
    
    def cawcaw():
        return "cawcaw"
    
    
class AnimalFactory:
    
    @classmethod
    def get_object(cls,classname :str)->Any:
        
        return getattr(sys.modules[__name__], classname)()
       

class BirdsFactory:
    
    @classmethod
    def get_object(cls,classname :str)->Any:
        # print(type(classname))
    
        return getattr(sys.modules[__name__], classname)()
       


class LivingThings:
    
    @classmethod
    def get_object(cls,types,name):
        
        # print(types,name)
        if types.lower() == "animals":
            return AnimalFactory.get_object(name)
        
        elif types.lower() == "birds":
            return BirdsFactory.get_object(name)
            
        
print(sys.modules[__name__])

for _ in range(6):
    
    a = (LivingThings.get_object("birds","Crow"))
    print(a)
    print(id(a))
    
    
        
    
    
        