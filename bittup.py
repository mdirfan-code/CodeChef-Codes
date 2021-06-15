def modExpo(x,y,md=1000000007):
    ans=1
    x = x % md
    while(y>0):
        
        if(y & 1):
            ans = (ans* x) % md
        y = y>>1
        x=(x*x)% md
    return ans

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    nt=modExpo(2,n) - 1
    ans=modExpo(nt,m)
    print(ans)