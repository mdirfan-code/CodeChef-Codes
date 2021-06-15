for _ in range(int(input())):
    n,x,k=map(int,input().split())
    print("YES" if((x/k) == (x//k) or ((n+1-x)/k) == ((n+1-x)//k)) else "NO")