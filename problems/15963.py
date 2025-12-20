# https://www.acmicpc.net/problem/15963

from sys import stdin

input = stdin.readline

N, M = map(int, input().rstrip().split())

print(1 if N == M else 0)
