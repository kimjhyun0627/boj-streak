# https://www.acmicpc.net/problem/14620

from sys import stdin
from itertools import combinations

input = stdin.readline


def calculate_flower_cost(x, y, cost_grid):
    if x <= 0 or y <= 0 or x >= N - 1 or y >= N - 1:
        return 10000
    return (
        cost_grid[x][y]
        + cost_grid[x + 1][y]
        + cost_grid[x - 1][y]
        + cost_grid[x][y - 1]
        + cost_grid[x][y + 1]
    )


def get_flower_positions(x, y):
    return [(x, y), (x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]


def check_overlap(x1, y1, x2, y2, x3, y3):
    pos1 = set(get_flower_positions(x1, y1))
    pos2 = set(get_flower_positions(x2, y2))
    pos3 = set(get_flower_positions(x3, y3))

    if pos1 & pos2 or pos1 & pos3 or pos2 & pos3:
        return True
    return False


N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

flower_costs = [[0] * N for _ in range(N)]
valid_positions = []

for ii in range(1, N - 1):
    for jj in range(1, N - 1):
        cost_val = calculate_flower_cost(ii, jj, cost)
        flower_costs[ii][jj] = cost_val
        if cost_val < 10000:
            valid_positions.append((ii, jj, cost_val))

min_cost = 10000

for (i1, j1, cost1), (i2, j2, cost2), (i3, j3, cost3) in combinations(
    valid_positions, 3
):
    if cost1 + cost2 >= min_cost:
        continue

    if not check_overlap(i1, j1, i2, j2, i3, j3):
        min_cost = min(min_cost, cost1 + cost2 + cost3)

print(min_cost)
