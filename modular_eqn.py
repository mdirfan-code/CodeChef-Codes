for _ in range(int(input())):
    n,m=map(int,input().split())
    c=0
    for i in range(1,n):
        for j in range(i+1,n+1):
            if((m % i) % j == (m % j) % i):
                c+=1
                print("(",i,",",j,"|",(m % i),",",(m % j),")")
    print(c)
