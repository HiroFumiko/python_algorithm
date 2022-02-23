import itertools
N = int(input())
S = input()
# S = [int(s) for s in S]

# ans = 0
# for q in itertools.product(range(10), repeat=3): # ３つの数の直積集合を予め作っておく
#     i = 0
#     for s in S:
#         if s == q[i]:
#             if i == 2:
#                 ans += 1
#                 break
#             else:
#                 i += 1

st = [set() for _ in range(3)]

for s in S:
    print(st)
    for pre in st[1]:
        st[2].add(pre + s)
    for pre in st[0]:
        st[1].add(pre+s) # 2桁目
    st[0].add(s) # 1桁目

ans = len(st[2])
print(ans)