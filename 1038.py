# https://www.acmicpc.net/problem/1038

from itertools import combinations

N = int(input())

result = []
for ii in range(1, 11):
    for jj in combinations(range(10), ii):
        num = "".join(list(map(str, reversed(list(jj)))))
        result.append(int(num))

result.sort()
if N >= len(result):
    print(-1)
else:
    print(result[N])
