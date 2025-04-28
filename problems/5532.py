# https://www.acmicpc.net/problem/5532

from sys import stdin

input = lambda: stdin.readline().rstrip()

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

print(L - max((A // C + 1 if A % C else A // C), (B // D + 1 if B % D else B // D)))
