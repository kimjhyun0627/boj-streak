# https://www.acmicpc.net/problem/5212

from sys import stdin

input = lambda: stdin.readline().rstrip()


def remap(r, c):
    cnt = 0
    for dr, dc in ([-1, 0], [1, 0], [0, -1], [0, 1]):
        nr, nc = r + dr, c + dc
        if nr < 0 or nc < 0 or nr >= R or nc >= C:
            cnt += 1
            continue
        if graph[nr][nc] == ".":
            cnt += 1
    return "X" if cnt < 3 else "x"


R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

sr, sc, er, ec = R - 1, C - 1, 0, 0
for r in range(R):
    for c in range(C):
        if graph[r][c] == "X":
            graph[r][c] = remap(r, c)

for r in range(R):
    for c in range(C):
        if graph[r][c] == "X":
            sr = min(sr, r)
            sc = min(sc, c)
            er = max(er, r)
            ec = max(ec, c)

for gr in graph[sr : er + 1]:
    print(*["." if g == "x" else g for g in gr[sc : ec + 1]], sep="")
