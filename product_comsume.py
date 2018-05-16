import threading
import random
import time
import Queue

class Producer(threading.Thread):
    def run(self):
        while True:
            if queue.qsize() < 300:
                for i in range(50):
                    queue.put('product' + str(i))
                    print 'produce the '+ str(i)
                    time.sleep(1)
class Comsumer(threading.Thread):
    def run(self):
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = queue.get()
                    print 'comsume the '+ msg
                    time.sleep(1)
global queue
queue = Queue.Queue()
for i in range(100):
    queue.put('product'+str(i))


for i in range(3):
    p = Producer()
    p.start()
    time.sleep(random.random())

for i in range(6):
    c = Comsumer()
    c.start()
    time.sleep(random.random())
