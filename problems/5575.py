# https://www.acmicpc.net/problem/5575

from sys import stdin

input = lambda: stdin.readline().rstrip()

for _ in range(3):
    time = list(map(int, input().split()))
    dur = (time[3] * 60 * 60 + time[4] * 60 + time[5]) - (
        time[0] * 60 * 60 + time[1] * 60 + time[2]
    )
    print(dur // 3600, dur % 3600 // 60, dur % 60)
