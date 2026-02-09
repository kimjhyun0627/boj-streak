# https://www.acmicpc.net/problem/1946

from sys import stdin

input = stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    scores = sorted(scores, key=lambda x: x[0])
    min_score = scores[0][1]
    count = 1
    for ii in range(1, N):
        if scores[ii][1] < min_score:
            count += 1
            min_score = scores[ii][1]
    print(count)
