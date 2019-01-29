class MyClass(object):
    common = 10
    def __init__(self):
        self.myvariable = 3
    def myfunction(self, arg1, arg2):
        return self.myvariable

    # This is the class instantiation

classinstance = MyClass()
print(classinstance.myfunction(1, 2))
# 3

# This variable is shared by all instances.
classinstance2 = MyClass()
print(classinstance.common)
# 10
print(classinstance2.common)
# 10

# Note how we use the class name
# instead of the instance.
MyClass.common = 30
print(classinstance.common)
# 30
print(classinstance2.common)
# 30

# This will not update the variable on the class,
# instead it will bind a new object to the old
# variable name.

classinstance.common = 10
classinstance.common
#10
classinstance2.common
#30
MyClass.common = 50

# This has not changed, because "common" is
# now an instance variable.
classinstance.common
# 10
classinstance2.common
# 50



# This class inherits from MyClass. The example
# class above inherits from "object", which makes
# it what's called a "new-style class".
# Multiple inheritance is declared as:
# class OtherClass(MyClass1, MyClass2, MyClassN)
class OtherClass(MyClass):
    # The "self" argument is passed automatically
    # and refers to the class instance, so you can set
    # instance variables as above, but from inside the class.
    def __init__(self, arg1):
        self.myvariable = 4
        print(arg1)

classinstance = OtherClass("hello")
# hello
print(classinstance.myfunction(1, 2))
# 4


# This class doesn't have a .test member, but
# we can add one to the instance anyway. Note
# that this will only be a member of classinstance.

classinstance.test = 10
print(classinstance.test)
# 10


#####################################
# __init__ 
# it is mandatory to inform the variables
# if you have __init__
#####################################
class Dog:
    def __init__(self,breed):
        self.breed = breed
        
sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')
# dog = Dog() # TypeError: __init__() missing 1 required positional argument: 'breed'



###################
# Polymorphism
###################

class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):

    def speak(self):
        return self.name+' says Meow!'

niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())



