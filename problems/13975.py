# https://www.acmicpc.net/problem/13975

import heapq
from sys import stdin

input = stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    pages = list(map(int, input().split()))

    heapq.heapify(pages)
    ans = 0
    while len(pages) > 1:
        cost = heapq.heappop(pages) + heapq.heappop(pages)
        ans += cost
        heapq.heappush(pages, cost)

    print(ans)

