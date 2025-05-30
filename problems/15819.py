# https://www.acmicpc.net/problem/15819

from sys import stdin

input = lambda: stdin.readline().rstrip()

N, I = map(int, input().split())
words = [input() for _ in range(N)]

words.sort()

print(words[I - 1])
