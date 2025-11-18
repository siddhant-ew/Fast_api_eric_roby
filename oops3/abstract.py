from abc import ABC, abstractmethod

class gadi(ABC):
    @abstractmethod

    def start_engine(self):
        print("engine has been started")
        pass

    def off_engine(self):
        print("engine has beed turned off")
        pass

class car(gadi):

    def start_engine(self):
        print("car's engine started")

    def off_engine(self):
        print("car's engine turned off")

class truck(gadi):

    def start_engine(self):
        print("truck's engine started")
    def off_engine(self):
        print("truck's engine turned off")
    
vehicles = [car(), truck()]
for v in vehicles:
    v.start_engine()
    v.off_engine()
