# https://www.acmicpc.net/problem/15658

from sys import stdin

input = lambda: stdin.readline().rstrip()


def dfs(res, add, sub, mult, div, idx):
    global mx, mn

    if idx == N:
        mx = max(mx, res)
        mn = min(mn, res)
        return

    if add:
        dfs(res + arr[idx], add - 1, sub, mult, div, idx + 1)
    if sub:
        dfs(res - arr[idx], add, sub - 1, mult, div, idx + 1)
    if mult:
        dfs(res * arr[idx], add, sub, mult - 1, div, idx + 1)
    if div:
        dfs(int(res / arr[idx]), add, sub, mult, div - 1, idx + 1)


N = int(input())
arr = list(map(int, input().split()))
add, sub, mult, div = map(int, input().split())

mx, mn = -(10**9), 10**9
dfs(arr[0], add, sub, mult, div, 1)

print(mx)
print(mn)
