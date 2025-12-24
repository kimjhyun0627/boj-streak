# https://www.acmicpc.net/problem/1269

from sys import stdin

input = stdin.readline

_, _ = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len((A - B).union(B - A)))
