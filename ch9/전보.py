import heapq

INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
