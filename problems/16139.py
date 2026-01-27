# https://www.acmicpc.net/problem/16139

from collections import defaultdict
from sys import stdin

input = stdin.readline

S = input().rstrip()
q = int(input())
questions = [(a, int(l), int(r)) for _ in range(q) for a, l, r in [input().split()]]

counts = [defaultdict(int) for _ in range(len(S)+1)]
for ii in range(1, len(S)+1):
    counts[ii] = counts[ii-1].copy()
    counts[ii][S[ii-1]] += 1

for a, l, r in questions:
    print(counts[r+1][a] - counts[l][a])