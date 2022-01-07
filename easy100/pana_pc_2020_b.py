import math

H, W = map(int, input().split())
w_move = math.ceil(W / 2)
if H % 2 == 0 and W % 2 == 0:
    ans = 2 * w_move * int(H / 2)
elif H % 2 == 0 and W % 2 == 1:
    ans = (2 * w_move - 1) * int(H / 2)
elif H % 2 == 1 and W % 2 == 0:
    ans = 2 * w_move * int((H - 1) / 2) + w_move
elif H % 2 == 1 and W % 2 == 1:
    ans = (2 * w_move - 1) * int((H - 1) / 2) + w_move

print(ans)