#coding=UTF-8
from multiprocessing import Process, Queue
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
q = Queue()
pw = Process(target=writer,args=(q,))
pw.start()
pw.join()

pr = Process(target=reader,args=(q,))
pr.start()
pr.join()

print "all infomation is read"
