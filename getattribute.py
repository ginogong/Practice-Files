class School(object):
    def __init__(self,sub):
        self.subject1 = sub
        self.subject2 = 'cpp'

    def __getattribute__(self,obj):
        if obj =="subject1":
            return 'python redirct'
        else:
            return object.__getattribute__(self,obj)


s1 = School('python')
print(s1.subject1)
print(s1.subject2)
