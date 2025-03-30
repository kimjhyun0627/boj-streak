# https://www.acmicpc.net/problem/1174

from sys import stdin
from itertools import combinations

input = stdin.readline

N = int(input())
res = set()

for ii in range(1, 11):
    for c in combinations(range(0, 10), ii):
        c = sorted(c, reverse=True)
        res.add(int("".join(map(str, c))))

res = sorted(res)
print(res[N - 1] if N <= len(res) else -1)
