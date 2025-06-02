# https://www.acmicpc.net/problem/15729

from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
paper = list(map(int, input().split()))
ans = [0 for _ in range(N)]

res = 0
for ii in range(len(ans)):
    if ans[ii : ii + 3] == paper[ii : ii + 3]:
        continue
    if ans[ii] != paper[ii]:
        ans[ii : ii + 3] = [(a + 1) % 2 for a in ans[ii : ii + 3]]
        res += 1

print(res)
