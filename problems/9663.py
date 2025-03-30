# https://www.acmicpc.net/problem/9663

n = int(input())

result = 0
row = [0] * n


def check(x):
    for ii in range(x):
        if row[x] == row[ii] or abs(row[x] - row[ii]) == x - ii:
            return False
    return True


def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for ii in range(n):
            row[x] = ii
            if check(x):
                dfs(x+1)


dfs(0)
print(result)
