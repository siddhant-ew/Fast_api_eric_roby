from abc import ABC, abstractmethod

# ABC = Abstract Base Class

# @abstractmethod is a decorator in Python that you use inside an abstract class to say,
# “Every child class must create its own version of this method.” The abstract class only gives the rule or idea, 
# but doesn’t provide the actual code for the method. Because it’s just a blueprint, you cannot create an object of an abstract class. 
# Only the child classes that implement all the abstract methods can be used to make objects. This helps ensure that all child classes follow the same structure.

class gadi(ABC):
    @abstractmethod

    def start_engine(self):
        print("engine has been started")
        pass

    def off_engine(self):
        print("engine has been turned off")
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


# a = gadi() ---we cannot use the abstract class for the object making, the type error will throw like this - 
#               TypeError: Can't instantiate abstract class gadi without an implementation for abstract method 'start_engine'

# Real Reason Why Abstraction Is Important (Practical Explanation):
    # Abstraction is important because it helps you design clean, predictable, and error-free software, 
    # especially when multiple developers or multiple types of objects are involved.
    # Think of abstraction as creating a contract or mandatory rule-set that all subclasses must follow.

# Imagine you're building a software system with 10 engineers.
# If everyone writes methods however they want, your project will become a mess.

# Example problem without abstraction:
# One developer names method start().
# Another names it start_engine().
# Another names it turnOn().

# Now your main program cannot depend on any consistent method name.
# Abstraction fixes this.