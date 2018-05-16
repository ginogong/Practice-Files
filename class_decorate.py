class Log(object):
    def __init__(self,func):
        print('initializing!')
        print('this func name is %s'%func.__name__)
        self.__func = func

    def __call__(self):
        print('calling the class to decorate')
        self.__func()


@Log
def test():
    print("this is a test")

test()
