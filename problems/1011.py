# https://www.acmicpc.net/problem/1011

from sys import stdin

input = stdin.readline

T = int(input())
for _ in range(T):
    moved = 0
    cur_speed = 0
    answer = 0
    x, y = map(int, input().split())
    dist = y - x

    while True:
        cur_speed += 1
        moved += cur_speed * 2
        answer += 2
        if moved - cur_speed >= dist:
            print(answer - 1)
            break
        if moved >= dist:
            print(answer)
            break
