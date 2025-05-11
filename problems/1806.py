# https://www.acmicpc.net/problem/1806

from sys import stdin

input = lambda: stdin.readline().rstrip()

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
length = 100000
temp_sum = arr[0]

while left <= right:
    if temp_sum >= S:
        length = min(length, right - left + 1)
        temp_sum -= arr[left]
        left += 1
    else:
        right += 1
        if right < N:
            temp_sum += arr[right]
        else:
            break

if length == 100000:
    print(0)
else:
    print(length)
