# https://www.acmicpc.net/problem/1189

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

r, c, k = map(int, input().split())
graph = [[n for n in input().rstrip()] for _ in range(r)]


direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
count = 0


def dfs(x, y, cost):
    global count
    if x == 0 and y == c - 1:
        if cost == k:
            count += 1
            return

    for dx, dy in direction:
        if 0 <= x + dx and x + dx < r and 0 <= y + dy and y + dy < c:
            if graph[x + dx][y + dy] == ".":
                graph[x + dx][y + dy] = "!"
                dfs(x + dx, y + dy, cost + 1)
                graph[x + dx][y + dy] = "."


graph[r-1][0] = '!'
dfs(r - 1, 0, 1)
print(count)
