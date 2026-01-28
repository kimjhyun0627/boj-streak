# https://www.acmicpc.net/problem/2529

from itertools import combinations, permutations
from sys import stdin

input = stdin.readline

K = int(input())
ineqalities = list(input().split())

ans = []
for c in permutations(range(0, 10), len(ineqalities) + 1):
    is_valid = True
    for ii in range(len(c) - 1):
        if ineqalities[ii] == "<" and c[ii] < c[ii + 1]:
            continue
        elif ineqalities[ii] == ">" and c[ii] > c[ii + 1]:
            continue
        else:
            is_valid = False
            break
    if is_valid:
        ans.append(c)

print("".join(str(a) for a in ans[-1]))
print("".join(str(a) for a in ans[0]))
