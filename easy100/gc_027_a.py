N, x = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
c = 0
for i in range(N):
    if x >= A[i]:
        x -= A[i]
        c += 1
    else:
        break

if c == 0 or x == 0:
    print(c)
else:
    print(c - 1)