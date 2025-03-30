# https://www.acmicpc.net/problem/2193

N = int(input())
dp = []
dp.append(0)
dp.append(1)

for _ in range(2, N + 1):
    dp.append(dp[-1] + dp[-2])

print(dp[-1])
