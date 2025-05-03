# https://www.acmicpc.net/problem/14581

from sys import stdin

input = lambda: stdin.readline().rstrip()

for ii in range(3):
    for jj in range(3):
        print(":", input() if ii == jj == 1 else "fan", ":", sep="", end="")
    print("")
