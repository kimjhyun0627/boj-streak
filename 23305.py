# https://www.acmicpc.net/problem/23305

from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())

cur = [0] * 1000001

for c in list(map(int, input().split())):
    cur[c] += 1

result = 0
for w in list(map(int, input().split())):
    if cur[w] >= 1:
        cur[w] -= 1
    else:
        result += 1

print(result)
