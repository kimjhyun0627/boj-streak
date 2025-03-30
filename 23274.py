# https://www.acmicpc.net/problem/23274

from sys import stdin
from math import sqrt

input = stdin.readline

(
    kari_start_x,
    kari_start_y,
    ola_start_x,
    ola_start_y,
    kari_finish_x,
    kari_finish_y,
    ola_finish_x,
    ola_finish_y,
) = map(int, input().split())

print(
    max(
        sqrt((kari_start_x - ola_start_x) ** 2 + (kari_start_y - ola_start_y) ** 2),
        sqrt((kari_finish_x - ola_finish_x) ** 2 + (kari_finish_y - ola_finish_y) ** 2),
    )
)
