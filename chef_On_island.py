for _ in range(int(input())):
    x,y,xr,yr,d=map(int,input().split())
    print("YES" if min(x/xr,y/yr) >= d else "NO" )