from multiprocessing import Pool
import time,random,os

def worker(name):
    start_time = time.time()
    print('my pid is:%s ,my name:%s,start at %s'%(os.getpid(),name,start_time))
    time.sleep(5)
    stop_time = time.time()
    last_time = stop_time - start_time
    print 'my name:%s,stop at %s,last for: %s'%(name,start_time,last_time )

pool = Pool(4)
for i in range(10):
    pool.apply_async(worker,(i,))
    #print('the %sth process is created'%i)


pool.close()
pool.join()
