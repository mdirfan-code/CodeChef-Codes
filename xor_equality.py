ls=[1,1]
tt=[]
for _ in range(int(input())):
    tt.append(int(input()))
for i in range(2,max(tt)+1):
    ls.append(ls[-1]*2)
for i in tt:
    print(ls[i])