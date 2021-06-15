for _ in range(int(input())):
    a,b,c,d,k=map(int,input().split())
    t=k-(abs(c-a)+abs(d-b))
    print("NO" if t%2 else "YES")