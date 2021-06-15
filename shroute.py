import heapq
def dijkstra(graph, start, ends):
    ans=[]
    for end in ends:
        end-=1
        fl=0
        heap = [(0, start)]  # cost from start node,end node
        visited = set()
        while heap:
            (cost, u) = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            if u == end:
                ans.append(cost)
                fl=1
                break
            for v, c in graph[u]:
                if v in visited:
                    continue
                next = cost + c
                heapq.heappush(heap, (next, v))
        if(fl==0):
            ans.append(-1)
    return ans
def createGraph(a,n):
    G={}
    for i in range(n):
        G[i]=list()
    
    for i,t in enumerate(a):
        if t != 0:
            G[0].append([i,0])
        elif(a[0]==1):
            G[0].append([i,i])


    for j in range(1,n):
        k=1
        if(a[j]==1):
            for i in range(j+1,n):
                G[j].append([i,k])
                k+=1
        if(a[j]==2):
            for i in range(j-1,0,-1):
                G[j].append([i,k])
                k+=1
    return G 
    
        
            
        
for i in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    G=createGraph(a,n)
    print(G)
    # print(*dijkstra(G,0,b))
    

