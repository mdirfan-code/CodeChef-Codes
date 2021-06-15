from math import ceil
from functools import reduce
for _ in range(int(input())):
    l=list(map(int,input().split()))
    l.append(0)
    a=reduce(lambda x,y:x+y,l[l[0]+2:])
    m=(a//l[1])+1
    b=bool(a%l[1])
    print(a)
    print(m,m+(ceil((l[l[0]+1]-(a-((m-1)*l[1])))/l[1])*b))



