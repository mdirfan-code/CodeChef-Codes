for i in range(int(input())):
    D,d,a,b,c=map(int,input().split())
    l=D*d
    print(c if l >= 42 else b if l>=21 else a if l >= 10 else 0)
        