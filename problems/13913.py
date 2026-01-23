# https://www.acmicpc.net/problem/13913

from sys import stdin
from collections import deque

input = stdin.readline

N, K = map(int, input().split())

graph = [-1 for _ in range(100001)]

queue = deque([N])

while queue:
    cur = queue.popleft()
    if cur == K:
        break
    for next in [cur - 1, cur + 1, cur * 2]:
        if next < 0 or next > 100000:
            continue
        if graph[next] == -1:
            queue.append(next)
            graph[next] = cur

ans = [K]
while ans[-1] != N:
    ans.append(graph[ans[-1]])

print(len(ans) - 1)
print(*ans[::-1])
