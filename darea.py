def seMax(lst,i,j):
    maxm=0
    for k in lst:
        if(maxm < k[i][j] ):
            maxm = k[i][j]
    return maxm 
def seMin(lst,i,j):
    minm=lst[0][i][j]
    for k in lst:
        if(minm > k[i][j] ):
            minm = k[i][j]
    return minm

for i in range(int(input())):
    n=int(input())
    pnt=[]
    for _ in range(n):
        inp = list(map(int,input().split()))
        if(inp not in pnt):
            pnt.append(inp)
    n = len(pnt)
    i=0
    pnt.sort(key= lambda x:x[0])
    verl=[]
    while(i<n):
        lst=list()
        lst.append(pnt[i])
        while(i<n and lst[-1][0] == pnt[i][0]):
            i+=1
        lst.append(pnt[i-1])
        lst.sort()
        verl.append(lst)
  
    vlen=len(verl)

    pnt.sort(key= lambda x:x[1])
    horl=[]
   
    i=0
    while(i<n):
        lst=list()
        lst.append(pnt[i])
        while(i<n and lst[-1][1] == pnt[i][1]):
            i+=1
        lst.append(pnt[i-1])
        lst.sort()
        horl.append(lst)
   
    hlen=len(horl)
    areas=[]
    for i in range(hlen-1):
        lr1,br1=seMax(horl[0:i+1],1,0)-seMin(horl[0:i+1],0,0),horl[i][0][1]-horl[0][0][1]
        lr2,br2=seMax(horl[i+1:],1,0)-seMin(horl[i+1:],0,0),horl[hlen-1][0][1]-horl[i+1][0][1]
        areas.append((lr1*br1)+(lr2*br2))
    for i in range(vlen-1):
        lr1,br1=seMax(verl[0:i+1],1,1)-seMin(verl[0:i+1],0,1),verl[i][0][0]-verl[0][0][0]
        lr2,br2=seMax(verl[i+1:],1,1)-seMin(verl[i+1:],0,1),verl[hlen-1][0][0]-verl[i+1][0][0]
        areas.append((lr1*br1)+(lr2*br2))
    print(areas)
    if(len(areas)):
        print(min(areas))
        continue
    
    print(0)