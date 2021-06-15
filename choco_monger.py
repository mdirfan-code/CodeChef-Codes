def ltd(l):
    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
for _ in range(int(input())):
    c=0
    n,x = map(int,input().split())
    ch = list(map(int,input().split()))
    chd = ltd(ch)
    for i in sorted(chd.values()):
        if(x>0):
            x-=(i-1)
        c+=1
    if(x>0):
        c-=x
    print(c)


