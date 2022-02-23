import itertools
N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

ret_max = -1
for m1, m2 in itertools.combinations(range(M), 2):
    c = 0
    for a in A:
        c += a[m1] if a[m1] >= a[m2] else a[m2]

    if ret_max < c:
        ret_max = c

print(ret_max)