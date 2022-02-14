N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

cur = 1
flag = 1
for i in range(101010):
    cur = A[cur-1]
    if cur == 2:
        flag = 0
        break

if flag == 0:
    print(i + 1)
else:
    print(-1)