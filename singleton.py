from typing import Any

# init also runs after new call so we need to take care of that

class SingleTon:
    
    inst=None
    init = False
    def __new__(cls) -> Any:
        
        if not cls.inst:
            cls.inst = super().__new__(cls)
            
        return cls.inst
    
    def __init__(self) -> None:
        print(SingleTon.inst)
        if  not SingleTon.init:
            print("Inst")
            self.x = 1
            type(self).init = True
    
    def incerment(self):
        self.x+=1
        return self.x
        
    
for i in range(3):
    a =  (SingleTon().incerment())
    print(a)