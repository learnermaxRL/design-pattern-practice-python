from abc import  ABCMeta,abstractmethod
class Animal:
    
    command_hist=[]
    curr_val= 30
    @classmethod
    def execute_command(cls,command):
        
        cls.curr_val = command.execute(cls.curr_val)
        cls.command_hist.append(command)
        print(cls.curr_val)
        
    @classmethod
    def undo_command(cls):
        comm = cls.command_hist.pop()
        cls.curr_val = comm.undo(cls.curr_val)
        print(cls.curr_val)
        

class Command(metaclass=ABCMeta):
    
        
    @abstractmethod
    def execute(self,val):
        pass
    
    @abstractmethod
    def undo(self,val):
        pass
    
class SpeakCommand(Command):
    
    def __init__(self,val):
        
        self.val = val
    
    def execute(self,val):
        return self.val+val
        
    def undo(self,val):
        
        return val-self.val
        
        
command = SpeakCommand(10)
cmd2 = SpeakCommand(20)

an = Animal()
an.execute_command(command)
an.execute_command(cmd2)
an.undo_command()