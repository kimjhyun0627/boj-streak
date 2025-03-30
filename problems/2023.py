# https://www.acmicpc.net/problem/2023

N = int(input())


def isPrime(num):
    if num == 1:
        return False
    for ii in range(2, int(num**0.5) + 1):
        if num % ii == 0:
            return False

    return True


def find(num, level):
    if level == N:
        print(num)
        return

    for ii in range(1, 10):
        if isPrime(num * 10 + ii):
            find(num * 10 + ii, level + 1)


find(0, 0)
