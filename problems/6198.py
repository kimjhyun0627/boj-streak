# https://www.acmicpc.net/problem/6198

from sys import stdin

input = stdin.readline

N = int(input())
buildings = [int(input()) for _ in range(N)]

stack = []
res = []
for building in buildings[::-1]:
    cnt = 0
    while stack and stack[-1][0] < building:
        top = stack.pop()
        cnt += top[1] + 1
    res.append(cnt)
    stack.append((building, cnt))

print(sum(res))