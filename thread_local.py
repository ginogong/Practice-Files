import threading

def get_name():
    name = local_school.student
    print '%s is the name of %s'%(name,threading.current_thread().name)

def assign_name(name):
    local_school.student = name
    get_name()

local_school = threading.local()
t1 = threading.Thread(target=assign_name,args=('gino',),name='gino_name')
t2 = threading.Thread(target=assign_name,args=('gyx',),name='gyx_name')
t1.start()
t2.start()

