from abc import ABCMeta, abstractmethod

class Bonut(ABCMeta):
    
    @abstractmethod
    def color():
        
    @abstractmethod
    def shape ():
        

class Window(ABCMeta):
    
    @abstractmethod
    def transparency():
        
    @abstractmethod
    def material():      




class Car():
    
    def  __init__(self,win,bonut) -> None:
        
        self.window = win
        self.bonut = bonut
        
    