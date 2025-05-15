# https://www.acmicpc.net/problem/10917

from sys import stdin
from collections import defaultdict, deque

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

if N == 1:
    print(0)
    exit()

queue = deque([(1, 0)])
visited = set()
visited.add(1)

while queue:
    node, cnt = queue.popleft()

    if node == N:
        print(cnt)
        exit()

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append((neighbor, cnt + 1))

print(-1)
