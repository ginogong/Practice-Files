#coding=UTF-8
from multiprocessing import Pool, Manager
import os,random,time

def writer(q):
    for item in "gino":
        print("正在writing %s into %s"%(item,q))
        q.put(item)
        time.sleep(2)

def reader(q):
    while True:
        if not q.empty():
            item = q.get()
            print("正在reading %s from %s"%(item,q))
            time.sleep(2)
        else:
            break
q = Manager().Queue()


pool = Pool(4)
pool.apply(writer,(q,))
pool.applc(reader,(q,))
pool.close()
pool.join()
print "all infomation is read"
