# https://www.acmicpc.net/problem/20546

from sys import stdin

input = stdin.readline

asset = int(input())
prices = list(map(int, input().rstrip().split()))

asset_bnp = asset
stock_bnp = 0
for p in prices:
    if asset_bnp >= p:
        stock_bnp += asset_bnp // p
        asset_bnp -= p * (asset_bnp // p)

asset_timing = asset
stock_timing = 0
trend = 0
for ii in range(1, 14):
    if prices[ii] > prices[ii - 1]:
        trend = trend + 1 if trend > 0 else 1
    elif prices[ii] < prices[ii - 1]:
        trend = trend - 1 if trend < 0 else -1
    else:
        trend = 0

    if trend >= 3:
        asset_timing += stock_timing * prices[ii]
        stock_timing = 0
    if trend <= -3:
        stock_timing += asset_timing // prices[ii]
        asset_timing -= prices[ii] * (asset_timing // prices[ii])

bnp = asset_bnp + stock_bnp * prices[-1]
timing = asset_timing + stock_timing * prices[-1]

print("BNP" if bnp > timing else "TIMING" if bnp < timing else "SAMESAME")
