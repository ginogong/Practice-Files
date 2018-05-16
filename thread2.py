import threading
import time

def sing():
    for i in range(4):
        print('This thread is for sing')
        time.sleep(5)
def dance():
    for i in range(5):
        print('This thread is for dance')
        time.sleep(5)

t1 = threading.Thread(target=sing,args=())
t2 = threading.Thread(target=dance,args=())
t1.start()
t2.start()

while True:
    lenth = len(threading.enumerate())
    print 'now there is %d threads'% lenth
    if lenth <=1:
        break
    time.sleep(0.5)
