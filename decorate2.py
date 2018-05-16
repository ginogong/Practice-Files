import functools

def note(func):
    ''' this is note doc '''
    @functools.wraps(func)
    def inner():
        ''' this is inner doc'''
        print"calling inner to do something"
        return func()
    return inner

@note
def foo():
    '''this is foo doc'''
    print('i am foo')

foo()
print(foo.__doc__)

