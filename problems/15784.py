# https://www.acmicpc.net/problem/15784

from sys import stdin

input = stdin.readline

N, a, b = map(int, input().split())
seats = [list(map(int, input().split())) for _ in range(N)]

ans = "HAPPY"

for ii in range(N):
    if ii != a - 1 and seats[ii][b - 1] > seats[a - 1][b - 1]:
        ans = "ANGRY"
        break
    if ii != b - 1 and seats[a - 1][ii] > seats[a - 1][b - 1]:
        ans = "ANGRY"
        break

print(ans)
