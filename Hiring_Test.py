def test(qp,x,y):
    f,p=0,0
    for i in qp:
        if i == 'F':
            f+=1
            if (f >= x) or (f == x-1 and p>=y):
                return '1'
            continue
        if i == 'P':
            p+=1
            if (f >= x) or (f == x-1 and p>=y):
                return '1'
    return '0'
            
for _ in range(int(input())):
    m,n=map(int,input().split())
    x,y=map(int,input().split())
    ans=""
    for i in range(m):
        ans+=test(input(),x,y)
    print(ans)

