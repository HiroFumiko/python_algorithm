import math

N = int(input())
X = list(map(int, input().split()))

P = sum(X) / len(X)
P_ceil = math.ceil(P)
P_floor = math.floor(P)

X_Pc = [(x - P_ceil) ** 2 for x in X]
X_Pf = [(x - P_floor) ** 2 for x in X]

if sum(X_Pc) > sum(X_Pf):
    print(sum(X_Pf))
else:
    print(sum(X_Pc))