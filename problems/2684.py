# https://www.acmicpc.net/problem/2684

from sys import stdin

input = lambda: stdin.readline().rstrip()

P = int(input())


for _ in range(P):
    res = {
        "TTT": 0,
        "TTH": 0,
        "THT": 0,
        "THH": 0,
        "HTT": 0,
        "HTH": 0,
        "HHT": 0,
        "HHH": 0,
    }
    line = input()
    for ii in range(len(line) - 2):
        res[line[ii : ii + 3]] += 1

    print(*[res[key] for key in res])
