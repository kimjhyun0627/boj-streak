# https://www.acmicpc.net/problem/2493

from sys import stdin

input = stdin.readline

N = int(input())
towers = list(map(int, input().split()))

stack = []
ans = [0 for _ in range(N)]
for ii in range(N - 1, -1, -1):
    while stack and stack[-1][1] < towers[ii]:
        ans[stack.pop()[0]] = ii + 1
    stack.append([ii, towers[ii]])

print(*ans)
