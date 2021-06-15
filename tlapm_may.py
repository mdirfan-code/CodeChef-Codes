for _ in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    v = int((x1/2)*(2+(x1-1)))
    v += int(((y1-1)/2)*((2*x1)+(y1-2)))
    v += int(((x2-1)/2)*((2*x1)+((x2-x1-1)-1)))
    

    