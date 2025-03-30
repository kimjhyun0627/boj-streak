# https://www.acmicpc.net/problem/14500

from sys import stdin

input = stdin.readline


def rotate_90(shape):
    return [(-y, x) for (x, y) in shape]


def flip_horizontal(shape):
    return [(x, -y) for (x, y) in shape]


def flip_vertical(shape):
    return [(-x, y) for (x, y) in shape]


def normalize(shape):
    min_x = min(x for x, y in shape)
    min_y = min(y for x, y in shape)
    return sorted((x - min_x, y - min_y) for x, y in shape)


def generate_all_transformations(shape):
    transformations = set()
    current = shape

    for _ in range(4):
        current = rotate_90(current)
        transformations.add(tuple(normalize(current)))

    current = flip_horizontal(shape)
    for _ in range(4):
        current = rotate_90(current)
        transformations.add(tuple(normalize(current)))

    return transformations


shapes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
]

unique_shapes = set()
for shape in shapes:
    unique_shapes.update(generate_all_transformations(shape))

n, m = map(int, input().strip().split())

board = [list(map(int, input().strip().split())) for _ in range(n)]

res = 0

for ii in range(n):
    for jj in range(m):
        for arr in unique_shapes:
            A_i, A_j = ii + arr[0][0], jj + arr[0][1]
            B_i, B_j = ii + arr[1][0], jj + arr[1][1]
            C_i, C_j = ii + arr[2][0], jj + arr[2][1]
            D_i, D_j = ii + arr[3][0], jj + arr[3][1]
            if (
                0 <= A_i < n
                and 0 <= B_i < n
                and 0 <= C_i < n
                and 0 <= D_i < n
                and 0 <= A_j < m
                and 0 <= B_j < m
                and 0 <= C_j < m
                and 0 <= D_j < m
            ):
                res = max(
                    res,
                    board[A_i][A_j]
                    + board[B_i][B_j]
                    + board[C_i][C_j]
                    + board[D_i][D_j],
                )

print(res)
