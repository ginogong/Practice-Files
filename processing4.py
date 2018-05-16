#coding=utf-8
import os
from multiprocessing import Process
import time

def fun(name,num,**kwargs):
    time.sleep(3)
    print("子进程为 name:%s,num:%d"%(name,num))
    print("child process will sleep 3 seconds")
    time.sleep(3)
    print("this info will be display")
    for k,v in kwargs.items():
        print("传入的kwargs的参数分别为 %s,%s"%(k,v))
print('这是父进程的开始 ID为%d'%os.getpid())
p = Process(target=fun, name='p1',args=('test',10),kwargs={"a":10,"b":20})
print('通过Process创建了一个子进程p1,时间为：%s'%time.ctime())
p.start()
print('子进程开始执行的时间为%s'%time.ctime())
print("child process is doing his bussiness")
for i in range(6):
    print("闲着也是闲着，我来记个数吧: %s"%i)
    time.sleep(1)
    print('父进程等待子进程执行完，当前时间为%s'%time.ctime())

p.join()
print('子进程的名字：%s,id:%d'%(p.name,p.pid))
p.terminate()
print('子进程已经结束,时间为%s'%time.ctime())
