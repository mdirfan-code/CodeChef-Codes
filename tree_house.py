def tr(l,n,v):
    ln =len(l[n])
    if(ln==0):
        return v
    x=v
    l[n].sort(reverse=True,key = lambda k:len(l[k]))
    for i in range(ln):
        vl=(i+1)*v
        x+=tr(l,l[n][i],vl)
    return x
    
for _ in range(int(input())):
    n,x=map(int,input().split())
    ls= [[] for i in range(n)]
    print(ls)
    for i in range(n-1):
        u,v=map(int,input().split())
        ls[u-1].append(v-1)
        print(ls)
    print(tr(ls,0,x))
    




    

