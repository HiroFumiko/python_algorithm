N, M, X = map(int, input().split())
A = list(map(int, input().split()))

cost = []
for i in range(N+1):
    if i in A:
        cost.append(1)
    else:
        cost.append(0)

c1 = 0
for i in range(X):
    c1 += cost[i]

c2 = 0
for i in range(X, N+1):
    c2 += cost[i]

print(c1) if c1 <= c2 else print(c2)