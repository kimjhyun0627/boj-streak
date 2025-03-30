# https://www.acmicpc.net/problem/14681

x = int(input())
y = int(input())

if x > 0:
    print(1 if y > 0 else 4)
if x < 0:
    print(2 if y > 0 else 3)
