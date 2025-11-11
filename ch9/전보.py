import heapq
INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x][y]=z

def dijk(start):
    q = []
    heapq.heappush(q, (0, start))
    graph[c][c]=0
    while q:
        d, now = heapq.heappop(q)
        if graph[c][now]<d:
            continue
        for j in range(1, n+1):
            if graph[c][j] > d+graph[now][j]:
                graph[c][j] = d+graph[now][j]
                heapq.heappush(graph[c][j], j)

dijk(c)
cnt = 0
maxtime = 0
for i in range(1, n+1):
    if graph[c][i]<INF:
        cnt+=1
        maxtime = max(maxtime, graph[c][i])
print(cnt-1, maxtime)