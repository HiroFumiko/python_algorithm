N, W = map(int, input().split())
vw = []
for _ in range(N):
    v, w = map(int, input().split())
    vw.append((v, w))

dp = [[0] * (W+1) for i in range(N+1)]