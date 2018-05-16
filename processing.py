import os
import time
num = 100
pid = os.fork()
print(pid)
if pid <0 :
    print('falied to call ')
elif pid ==0:
    num+=1
    time.sleep(2)
    print('%s is child process , my parent is %s,num:%d'%(os.getpid(),os.getppid(),num))

else:
    time.sleep(4)
    print('%s is parent process,my child is %s,num:%d'%(os.getpid(),pid,num))
