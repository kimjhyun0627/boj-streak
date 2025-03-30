# https://www.acmicpc.net/problem/2661

n = int(input())


def isGood(idx):
    for ii in range(1, idx // 2 + 1):
        if res[idx - ii : idx] == res[idx - ii * 2 : idx - ii]:
            return False
    return True


def create(idx):
    if idx == n and isGood(idx):
        print(*res[:idx], sep="")
        exit(0)
    for ii in range(1, 4):
        if idx and ii == res[idx - 1]:
            continue
        res[idx] = ii

        if isGood(idx):
            create(idx + 1)


res = [0 for _ in range(82)]
create(0)
