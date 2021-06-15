t=int(input())
ans=[]
for k in range(t):
    
    n=int(input())
    l=list(map(int ,input().split()))

    l.sort(reverse=True)
    
    b1=l[0]
    b2=l[1]
    for i in range(2,n):
        if(b1<=b2):
            b1+=l[i]
        else:
            b2+=l[i]  
    ans.append(max(b1,b2))
for k in ans:
    print(k)    