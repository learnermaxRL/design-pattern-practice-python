
from typing import Any

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
        
        return getattr(sys.modules[__name__], classname)()
        
        

for _ in range(3):
    
    print(AnimalFactory.get_object("Dog"))
    
    
        
    
    
        