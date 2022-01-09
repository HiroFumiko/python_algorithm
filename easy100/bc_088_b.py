import heapq
N = int(input())
A = list(map(int, input().split()))
A = [-1 * a for a in A]
heapq.heapify(A)

alice = 0
bob = 0
for i in range(N):
    if i % 2 == 0:
        alice += heapq.heappop(A) * -1
    else:
        bob += heapq.heappop(A) * -1

print(alice - bob)