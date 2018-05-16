import os
import time

pid = os.fork()
if pid==0:
    print('this is child process 11')
    time.sleep(1)
else:
    print('this is parent process 11')
    time.sleep(2)

pid = os.fork()
if pid==0:
    time.sleep(3)
    print('this is child process 22')
else:
    time.sleep(2)
    print('this is parent process 22')



