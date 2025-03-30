# https://www.acmicpc.net/problem/14235

from sys import stdin
import heapq

input = lambda: stdin.readline().rstrip()

N = int(input())

presents = []
for _ in range(N):
    point = list(map(int, input().split()))

    cost = 0
    if len(point) == 1 and point[0] == 0:
        if presents:
            print(-heapq.heappop(presents))
        else:
            print(-1)

    else:
        for p in point[1:]:
            heapq.heappush(presents, -p)
