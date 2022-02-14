N = int(input())
V = list(map(int, input().split()))

def func(a: int, b: int) -> float:
    return (a + b) / 2

if N < 3:
    res = (V[0] + V[1]) / 2
else:
    V.sort()
    for i in range(N-1):
        if i == 0:
            tmp = func(V[i], V[i+1])
        else:
            tmp = func(tmp, V[i+1])

    res = tmp

print(res)

