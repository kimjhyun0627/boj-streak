# https://www.acmicpc.net/problem/30825

from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

target = 0
idx = 0
while idx < N and target != N - 1:
    if arr[idx] - arr[target] < K * (idx - target):
        continue
    if arr[idx] - arr[target] >= K * (idx - target):
        target = idx
    idx += 1

res = 0
for ii in range(N):
    res += arr[target] + K * (ii - target) - arr[ii]

print(res)
