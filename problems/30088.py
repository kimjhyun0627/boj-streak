# https://www.acmicpc.net/problem/30088

from sys import stdin

input = stdin.readline

N = int(input())
cost = []
for _ in range(N):
    cost.append(sum(list(map(int, input().split()))[1:]))

cost.sort()

ans = sum([sum(cost[: ii + 1]) for ii in range(N)])

print(ans)
