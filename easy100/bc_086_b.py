import math
a, b = map(str, input().split())
num = int(a + b)

# 平方根とって切り捨て
n = math.floor(math.sqrt(num))
if n ** 2 == num:
    print('Yes')
else:
    print('No')