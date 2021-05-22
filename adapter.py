class AnimalSpeakAdapter():
    
    def __init__(self,,obj,**adpater_methods) -> None:
        
        for key,value in adpater_methods:
            setattr(self,key,getattr(obj,value))
        

class Dog:
    
    def bark(self):
      print("Buw!")
      
class Cat:
    
    def meow(self):
      print("meow!")
      
class Cow:
    
    def moo(self):
      print("Moo!")
      
cow = AnimalSpeakAdapter(Cow(),"moo")
dog = AnimalSpeakAdapter(Dog(),"bark")
cat = AnimalSpeakAdapter(Cat(),"meow")
      
cow.speak()
dog.speak()
cat.speak()


      
      