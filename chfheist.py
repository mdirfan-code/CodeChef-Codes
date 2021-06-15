for i in range(int(input())):
    d,pd,p,q=map(int,input().split())
    n=d//pd
    a=pd*p
    df=q*pd
    tot=int((n/2)*((2*a)+((n-1)*df)))+((p+(q*n))*(d%pd))
    print(tot)