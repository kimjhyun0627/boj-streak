# https://www.acmicpc.net/problem/1439

from sys import stdin

input = stdin.readline

S = input().strip()

zero2one = 0 if S[0] == "0" else 1
one2zero = 0 if S[0] == "1" else 1
for ii in range(1, len(S)):
    if S[ii] != S[ii - 1]:
        if S[ii] == "0":
            one2zero += 1
        else:
            zero2one += 1

print(min(zero2one, one2zero))
