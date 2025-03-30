# https://www.acmicpc.net/problem/9215

from sys import stdin
from math import lcm, gcd

input = stdin.readline

t = 0
while True:
    t += 1

    n = int(input().rstrip())
    if not n:
        break

    integers = 0
    denominators = []
    numerators = []

    for _ in range(n):

        num = list(map(int, input().rstrip().replace(",", "/").split("/")))

        if len(num) == 1:
            integers += num[0]
        if len(num) == 2:
            numerators.append(num[0])
            denominators.append(num[1])
        if len(num) == 3:
            integers += num[0]
            numerators.append(num[1])
            denominators.append(num[2])

    dn = denominators[0]
    for d in denominators:
        dn = lcm(d, dn)

    for ii in range(len(denominators)):
        x = dn / denominators[ii]
        numerators[ii] *= x

    integers += sum(numerators) // dn
    s = sum(numerators) % dn
    g = gcd(int(s), dn)

    if integers and numerators:
        if s:
            print(f"Test {t}: {int(integers)},{int(s/g)}/{int(dn/g)}")
        else:
            print(f"Test {t}: {int(integers)}")
    elif integers:
        print(f"Test {t}: {int(integers)}")
    elif s:
        print(f"Test {t}: {int(s/g)}/{int(dn/g)}")
    else:
        print(f"Test {t}: {int(integers)}")
