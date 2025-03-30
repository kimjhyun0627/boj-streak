# https://www.acmicpc.net/problem/1005

from collections import deque
from sys import stdin

input = stdin.readline

t = int(input())
res = []

for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    dp = [0] * (n + 1)

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    queue = deque()
    for ii in range(1, n + 1):
        if indegree[ii] == 0:
            queue.append(ii)
            dp[ii] = time[ii]

    while queue:
        tmp = queue.popleft()

        for ii in graph[tmp]:
            indegree[ii] -= 1
            dp[ii] = max(dp[tmp] + time[ii], dp[ii])
            if indegree[ii] == 0:
                queue.append(ii)

    w = int(input())
    res.append(dp[w])


for ii in res:
    print(ii)
