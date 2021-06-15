def isSorted(l,n):
    for i in range(n-1):
        if(l[i]>l[i+1]):
            return False
    return True
for _ in range(int(input())):
    n=int(input())
    deck= list(map(int,input().split()))
    fl=[]
    for i in range(n-1):
        if(deck[i]>deck[i+1]):
            fl.append((i,i+1))
            if(len(fl)>1):
                print("NO")
                break
    lf=len(fl)
    if(lf<=1):
        if(lf==0):
            print("YES")
        else:
            deck=deck[fl[0][1]:]+deck[:fl[0][1]]
            if(isSorted(deck,n)):
                print("YES")
            else:
                print("NO")
            
    