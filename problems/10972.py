# https://www.acmicpc.net/problem/10972

from sys import stdin

input = stdin.readline


def next(arr: list):

    if n == 1:
        return False

    if arr[-2] < arr[-1]:
        arr[-2], arr[-1] = arr[-1], arr[-2]
        return True

    fr, to = 0, len(arr) - 1
    while arr[to] < arr[to - 1]:
        to -= 1
        if to <= 0:
            return False

    if arr[to - 1] > arr[-1]:
        while arr[to - 1] > arr[-1 - fr]:
            fr += 1
        arr[to - 1], arr[-1 - fr] = arr[-1 - fr], arr[to - 1]
        arr[to:] = reversed(arr[to:])
    else:
        arr[to - 1], arr[-1] = arr[-1], arr[to - 1]
        arr[to:] = reversed(arr[to:])

    return True


n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

if next(arr):
    print(*arr)
else:
    print(-1)
