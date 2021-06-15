from math import ceil
for i in range(int(input())):
    xa,xb,Xa,Xb=map(int,input().split())
    print(ceil(Xa/xa)+ceil(Xb/xb))