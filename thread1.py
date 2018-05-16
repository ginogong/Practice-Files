import threading
import time

def fun(num):
    print("this is %s threading"% num)

for i in range(6):
    t = threading.Thread(target=fun,args=(i+1,))
    t.start()

