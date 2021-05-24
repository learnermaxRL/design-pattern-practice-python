from abc import abstractmethod,ABCMeta
class Observer:
    
    
    @abstractmethod
    def update(self,value):
        pass

class Observable:
    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        with suppress(ValueError):
            self._observers.remove(observer)

    def notify(self, modifier: Optional[Observer] = None) -> None:
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Wallpaper(Observer):
    
    def __init__(self):
        self.wallpaper = None
    
    def update(self):
        self.wallpaper = value
        print("Changed wallpaper to {}".format(value))
        
class ImageIcon(Observer):
    def __init__(self):
        self.wallpaper = None
    
    def update(self):
        self.wallpaper = value
        print("Changed icon to {}".format(value))
        


    
    