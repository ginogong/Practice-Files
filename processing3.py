from multiprocessing import Process
import os
def fun(name):
    print('child id :%d,parent id:%d, name:%s'%(os.getpid(),os.getppid(),name))

print('parent process')
p=Process(target=fun,args=('test',))
p.start()
p.join()
print('child process ends')
