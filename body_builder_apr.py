from functools import reduce 
for _ in range(int(input())):
    n,r = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    res=0
    ans=0
    for i in range(n):
        ans+=b[i]
        res = max(res,ans)
        if(i != n-1):
            ans -= r * (a[i+1] - a[i])
        if(ans<0):
            ans = 0
    print(res)



