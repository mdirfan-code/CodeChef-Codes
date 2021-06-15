for i in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    arr1=[]
    arr2=[]
    k=-1
    for i in a:
        if(i==1):
            k=0
        arr1.append(k)
        if(k >-1):
            k+=1
    k=-1
    for i in a[::-1]:
        if(i==2):
            k=0
        arr2.insert(0,k)
        if(k!=-1):
            k+=1
    arr1[0]=0
    arr2[0]=0
    for i in b:

        if(arr1[i-1]==arr2[i-1]):
            print(arr1[i-1],end=' ')
        elif arr1[i-1] == -1 or arr2[i-1]==-1:
            print(max(arr1[i-1],arr2[i-1]),end=' ')
        else:
            print(min(arr1[i-1],arr2[i-1]),end=' ')
    print()
