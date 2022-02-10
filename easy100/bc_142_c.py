N = int(input())
A = list(map(int, input().split()))

res = []
for i in range(N):
    idx = A.index(i+1)
    res.append(idx+1)

print(' '.join(map(str, res)))