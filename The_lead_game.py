s1,s2,wp,ml=0,0,0,0
for _ in range(int(input())):
    p1,p2 = map(int,input().split())
    s1,s2 = s1+p1,s2+p2
    d=abs(s1-s2)
    if( d > ml):
        ml=d
        wp = 1 if s1 > s2 else 2

print(wp,ml,sep=" ")