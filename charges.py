for _ in range(int(input())):
    n,k=map(int,input().split())
    ch=list()
    for i in input():
        ch.append(int(i))
    cst=0
    q=list(map(int,input().split()))
    for i in range(n-1):
        cst+= (bool(ch[i] == ch[i+1]) +1)
    for i in q:
        ch[i-1] = bool(not ch[i-1]) 
        if(i>1):
            cst+= 1 if ch[i-2] == ch [i-1] else -1
        if(i<n):
             cst+= 1 if ch[i] == ch [i-1] else -1
        print(cst)
    

