def add(s):
    return int(s[0]) + int(s[1])
def pol(p,n,m):
    if p[0] > p[1]:
        return m - p[1]
    else:
        return n - p[0]


for _ in range(int(input())):
    n,m=map(int,input().split())
    s=n+m
    print("YES" if (s - add(input().split())) < (s - pol(map(int,input().split()),n,m)) else "NO")
        
        


# for _ in range(int(input())):
#     n,m=map(int,input().split())
#     x,y=map(int,input().split())
#     a,b=map(int,input().split())
#     print("YES" if (m+n) - (x+y) < (m+n) - (a) else "NO")
#     # while(x<=n or y<=m):
    #     x,y=(x+1,y) if (a,b) != (x+1,y) and x+1<=n else (x,y+1)
    #     if x==n and y==m :
    #         print("YES")
    #         break
    #     a,b= (a+1,b) if (x,y) == (a+1,b) else (a,b+1) if (x,y) == (a,b+1) else  (a+1,b+1) if (x,y) == (a+1,b+1) else (a+int(x > a and a < n) , b+int(y > b and b < m))
    #     if(x==a and y==b):
    #         print("NO")
    #         break
        
        

# :
#     return 

