

#Classy Classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    @property
    def info(self): 
        return '{}s age is {}'.format(self.name, self.age)

names=["john","matt","alex","cam"]
ages=[16,25,57,39]
for i in range(4):
    name,age=names[i],ages[i]
    person=Person(name,age)
    print(person.info)

    

#Basic subclasses - Adam and Eve

class Human:
    pass
class Man(Human):
    pass
class Woman(Human):
    pass
def God():
    Adam = Man()
    Eva = Woman()
    return [Adam,Eva]

paradise = God()
print(paradise[0])

#Color Ghost

import random

class Ghost():

    colors = ["white","yellow","purple","red"]

    def __init__(self):
        self.color = random.choices(Ghost.colors)

ghost = Ghost()
print(ghost.color)

ghost2 = Ghost()
print(ghost2.color)




#Regular Ball Super Ball

class Ball():
    def __init__(self,object = None):
        if object == None:
            self.ball_type = "regular"
        else:
            self.ball_type = object
  
     
ball1 = Ball()
ball2 = Ball("ggg")
print(ball1.ball_type)
print(ball2.ball_type)


