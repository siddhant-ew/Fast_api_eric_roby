## polymorphism
# Just having same methods but different o/p

class cat:
    def start(self):
        return "meew"
class dog:
    def start(self):
        return "Bhook"
    

animals = [dog(), cat()]
for i in animals:
    print(i.start())



## polymorphism with inheritance

class vehicle:

    def __init__(self,colour:str, type:str, luxury:str = 'luxury'):
        self.colour = colour
        self._type = type
        self.luxury = luxury

    def defender(self,luxury='fuckin luxury car'):
        return f"The defender is {luxury} having colour {self.colour} and type of {self._type}"
    
    def xuv(self,luxury='SUV car'):
        return f"the XUV700 is {luxury} having colour {self.colour} and type of {self._type}"

        
car1 = vehicle("Black", "SUV")
print(car1.defender())
print(car1.xuv())
