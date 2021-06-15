st=[]
def tr(l,x,memo={},memo2={}):
    memo2[0]=x
    memo[x]=[x]
    for i in st:
        s=1
        l[i].sort(reverse=True,key = lambda k:len(l[k]))
        ln=len(l[i])
        print(i)
        print(memo2)
        print(memo,x)
        if(i in memo2 ):
            lm=0
            if memo2[i] in memo:
                lm=len(memo[memo2[i]])
            else:
                memo[memo2[i]]=[]
            print("lm = ",lm)
            if(lm<ln):
                print("llli = ",l[i])
                while(lm<ln):
                    memo2[l[i][lm-1]]=memo2[i]*(lm)
                    memo[memo2[i]].append(memo2[l[i][lm-1]])
                    lm+=1
            ln=len(l[i])
            while(ln):
                ln-=1
                x+=memo[memo2[i]][ln]
            
                
        else:
            print("else",i)
            memo[memo2[i]]=[]
            while(s<=ln):
                memo2[l[s-1]]=memo2[i]*s
                memo[memo2[i]].append(memo2[l[s-1]])
                x+=memo2[l[s-1]]
                s+=1
    return   x % 1000000007

for _ in range(int(input())):
    n,x=map(int,input().split())
    ls= [[] for i in range(n)]
    for i in range(n-1):
        u,v=map(int,input().split())
        if(u-1 not in st):
            st.append(u-1)
        ls[u-1].append(v-1)
    print(st)
    print(ls)
    print(tr(ls,x))