from sys import stdin
from math import sqrt

input = stdin.readline

while True:
    try:
        r, s = map(float, input().split())
        print(round(sqrt((r*(s+0.16))/0.067)))
    except:
        break