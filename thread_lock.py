import threading
import time

class Task1(threading.Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print('---running Task1----s')
                time.sleep(0.8)
                lock2.release()

class Task2(threading.Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print('---running Task2----s')
                time.sleep(0.8)
                lock3.release()
class Task3(threading.Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print('---running Task3----s')
                time.sleep(0.8)
                lock1.release()
t1 = Task1()
lock1 =threading.Lock()
t2 = Task2()
lock2 =threading.Lock()
lock2.acquire()
t3 = Task3()
lock3 =threading.Lock()
lock3.acquire()
t1.start()
t2.start()
t3.start()
