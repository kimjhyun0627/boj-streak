# https://www.acmicpc.net/problem/23882

from sys import stdin

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())

arr = list(map(int, input().split()))

swap_count = 0
for last_idx in range(N - 1, 0, -1):
    max_val = arr[0]
    max_idx = 0
    for i in range(1, last_idx + 1):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i

    if last_idx != max_idx:
        arr[last_idx], arr[max_idx] = arr[max_idx], arr[last_idx]
        swap_count += 1
        if swap_count == K:
            print(*arr)
            exit()

if swap_count < K:
    print("-1")
