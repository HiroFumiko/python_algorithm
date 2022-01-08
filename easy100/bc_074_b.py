import math

N = int(input())
K = int(input())
X = list(map(int, input().split()))

dist = 0
for i in range(N):
    if abs(X[i] - 0) < abs(X[i] - K):
        dist += abs(X[i] - 0) * 2
    else:
        dist += abs(X[i] - K) * 2

print(dist)