for _ in range(int(input())):
    n,k,f=map(int,input().split())
    tt=set()
    for i in range(n):
        s,e=map(int,input().split())
        for j in range(s,e):
            if j in tt:
                tt.remove(j)
    f=len(tt)
    print("YES" if(f>=k)else"NO") 