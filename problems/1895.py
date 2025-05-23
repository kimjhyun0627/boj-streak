# https://www.acmicpc.net/problem/1895

from sys import stdin

input = lambda: stdin.readline().rstrip()

R, C = map(int, input().split())

image = []
for _ in range(R):
    image.append(list(map(int, input().split())))

T = int(input())

res = 0
for ii in range(R - 2):
    for jj in range(C - 2):
        res += (
            1
            if sorted(
                [image[x][y] for x in range(ii, ii + 3) for y in range(jj, jj + 3)]
            )[4]
            >= T
            else 0
        )


print(res)
