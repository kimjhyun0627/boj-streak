# https://www.acmicpc.net/problem/13023

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline


def dfs(x, level, visited):

    if level == 4:
        return True

    res = False
    for f in friends[x]:
        if not visited[f]:
            visited[f] = True
            if dfs(f, level + 1, visited):
                res = True
                break
            visited[f] = False

    return res


N, M = map(int, input().split())
friends = [[] for _ in range(N)]
for _ in range(M):
    fr, to = map(int, input().split())
    friends[fr].append(to)
    friends[to].append(fr)

for ii in range(len(friends)):
    if dfs(ii, 0, [False if jj != ii else True for jj in range(N)]):
        print(1)
        exit()

print(0)
