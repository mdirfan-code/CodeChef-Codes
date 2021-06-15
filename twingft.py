for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    k=(k*2)
    i=0
    t1=[0,0]
    while(i<k):
        t1[i%2]+=a[i]
        i+=1
    t1[(i+1)%2]+=a[i]
    print(max(*t1))

