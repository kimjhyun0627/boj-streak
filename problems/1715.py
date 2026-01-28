# https://www.acmicpc.net/problem/1715

import heapq
from sys import stdin

input = stdin.readline

N = int(input())
cards = [int(input()) for _ in range(N)]

heapq.heapify(cards)

ans = 0
while len(cards) > 1:
    temp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, temp)
    ans += temp

print(ans)
