for i in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    arr=[]

    for i,t in enumerate(a):
        if t != 0:
            arr.append(0)
        elif(a[0]==1):
            arr.append(i)
        else:
            arr.append(-1)

    for j in range(1,n):
        k=1
        if(a[j]==1):
            for i in range(j+1,n):
                if(arr[i]==-1):
                    arr[i] = k
                    k+=1
                    continue
                arr[i]= min(arr[i],k)
                k+=1
            continue
        if(a[j]==2):
            for i in range(j-1,0,-1):
                if(arr[i]==-1):
                    arr[i] = k
                    k+=1
                    continue
                arr[i]= min(arr[i],k)
                k+=1
    for i in b:
        print(arr[i-1],end=' ')    
    print()