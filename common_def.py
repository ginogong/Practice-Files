def add(a,b,*args,**kwargs):
    res =a +b
    l1 = args

    dic = kwargs
    if len(l1):
        for i in l1:
            res += i
    if len(dic):
        for k,v in dic.items():
            res += dic[k]
    return res

l1 = add(3,2,1,2,3,4,5,6,7,x=2,y=5,z=10)
print(l1)

