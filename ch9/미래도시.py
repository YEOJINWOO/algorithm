n, m = map(int, input().split())
arr = [[-1]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
x, k = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if arr[j][i]!=-1 and arr[i][k]!=-1:
                if arr[j][k]==-1:
                    arr[j][k] = arr[j][i] + arr[i][k]
                else:
                    arr[j][k] = min(arr[j][k], arr[j][i]+arr[i][k])
if arr[1][k]==-1 or arr[k][x]==-1:
    print(-1)
else:
    print(arr[1][k] + arr[k][x])