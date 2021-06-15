def Or(args):
    res=args[0]
    for i in args[1:]:
        res = res | i
    return res
def And(args):
    res=args[0]
    for i in args[1:]:
        res = res & i
    return res
def orofand(n,arg):
    ls=[]
    for i in range(n):
        ls.append(And(arg[i]))
    return Or(ls)
for _ in range(int(input())):
    n,q = map(int,input().split())
    l = list(map(int,input().split()))
    print(orofand(n,l))
    for o_ in range(q):
        x,v=map(int,input().split())
        l[x-1]=v
        print(orofand(n,l))



    
