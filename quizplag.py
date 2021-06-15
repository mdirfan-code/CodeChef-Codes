for _ in range(int(input())):
    n,m,k= map(int,input().split())
    l=list(map(int,input().split()))
    pl=[]
    acc=dict()
    for i in l:
        if i<=n and not (i in acc and acc[i]==2):
            if(i in acc):
                acc[i]+=1
                pl.append(i)
                continue
            acc[i]=1
    pl.sort()
    print(len(pl),*pl)
            
