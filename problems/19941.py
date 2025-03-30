# https://www.acmicpc.net/problem/19941

from sys import stdin
from collections import deque

input = stdin.readline

n, k = map(int, input().split())
table = [t for t in input().rstrip()]

count = 0

for ii in range(len(table)):
    if table[ii] == "P":
        for jj in range(max(0, ii - k), min(len(table), ii + k + 1)):
            if table[jj] == "H":
                table[jj] = "h"
                table[ii] = "p"
                count += 1
                break

print(count)
