# https://www.acmicpc.net/problem/2304

from sys import stdin

input = lambda: stdin.readline().rstrip()

m = 0
m_idx = 0
box = [0 for _ in range(1001)]
N = int(input())

for _ in range(N):
    L, H = map(int, input().split())
    box[L] = H
    if m < H:
        m_idx = L
        m = H

cur = 0
res = 0
for ii in range(m_idx + 1):
    cur = max(cur, box[ii])
    res += cur

cur = 0
for ii in range(1000, m_idx, -1):
    cur = max(cur, box[ii])
    res += cur

print(res)
