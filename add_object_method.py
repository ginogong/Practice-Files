import types

class Person(object):

    def __init__(self,name,age):
        self.name=name
        self.age=age


def showinfo(self):
    print("%s's age is %d"%(self.name,self.age))
@classmethod
def fun1(cls):
    print("this is a classmethod")

@staticmethod
def fun2(a,b):
    return a + b
p1 = Person('gino',30)
p1.show = types.MethodType(showinfo,p1)
p1.show()

Person.fun1 = fun1
Person.fun2 = fun2

p1.fun1()
print(p1.fun2(3,4))
