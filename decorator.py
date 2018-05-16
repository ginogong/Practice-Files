def docorate(func):
    def recording():
        print('befor callable')
        func()
        print('after callable')

    return recording


@docorate
def foo():
    print('foo is running')

foo()
