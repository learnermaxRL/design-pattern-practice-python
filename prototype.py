import copy
import sys
from typing import Any

class Animal:
    
    def walk(self):
        pass
    
    def talk(self):
        pass
    
    def clone(self):
        return copy.deepcopy(self)
    

class Dog(Animal):
    def bark():
        return "Bhow"
    
class Whale(Animal):
    
    def moo():
        return "moo"
    
    
class Proto:
    
    protos = {}
   
        
    @classmethod
    def register_proto(cls,classname:str):
        try:
            thismodule = sys.modules[__name__]
        except Exception as e:
            print(e)
            
        cls.protos[classname] = getattr(thismodule,classname)()
    
    @classmethod
    def get_object(cls,classname :str)->Any:
        
        if classname not in cls.protos:
            return None
        else:
            return cls.protos[classname].clone()
        

Proto.register_proto("Dog")
Proto.register_proto("Whale")

for _ in range(3):
    
    print(Proto.get_object("Dog"))
    
    
        
    
    
        