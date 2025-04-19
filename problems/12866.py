# https://www.acmicpc.net/problem/12866

from sys import stdin
from collections import Counter

input = lambda: stdin.readline().rstrip()

L = int(input())
S = Counter(input())

res = 1
for dna in ["A", "G", "T", "C"]:
    res *= S[dna]

print(res % 1000000007)
