# https://www.acmicpc.net/problem/2910

from sys import stdin
from collections import defaultdict

input = stdin.readline

n, c = map(int, input().split())
message = list(map(int, input().split()))
order = []
freq = defaultdict(int)

for m in message:
    freq[m] += 1

for k, v in dict(sorted(dict(freq).items(), key=lambda x: x[1], reverse=True)).items():
    for _ in range(v):
        print(k, end=" ")
