# https://www.acmicpc.net/problem/13333

from sys import stdin

input = stdin.readline

N = int(input())
indice = list[int](map[int](int, input().split()))
indice.append(0)
indice.sort(reverse=True)

ans = 0
for k in range(1, N + 1):
    if indice[k - 1] >= k and indice[k] <= k:
        ans = k

print(ans)
