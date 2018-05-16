class Person(object):
    def __init__(self):
        self.__num = 100


    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self,num):
        self.__num = num
        return self.__num

p1 = Person()
print(p1.num)
p1.num = 30
print(p1.num)



