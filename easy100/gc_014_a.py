A, B, C = map(int, input().split())

res = 0
while True:
    if A % 2 != 0 or B % 2 != 0 or C % 2 != 0:
        break
    elif A == B and A == C:
        res = -1
        break
    else:
        next_A = (B / 2) + (C / 2)
        next_B = (A / 2) + (C / 2)
        next_C = (A / 2) + (B / 2)

        A = next_A
        B = next_B
        C = next_C

        res += 1

print(res)