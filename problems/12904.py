# https://www.acmicpc.net/problem/12904

from sys import stdin

input = stdin.readline

S = input().rstrip()
T = input().rstrip()

while len(T) > len(S):
    if T[-1] == "A":
        T = T[:-1]
    else:
        T = T[:-1][::-1]

print(1 if T == S else 0)
