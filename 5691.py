# https://www.acmicpc.net/problem/5691

from sys import stdin
input = stdin.readline

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    print(min(a,b) - (max(a,b) - min(a,b)))