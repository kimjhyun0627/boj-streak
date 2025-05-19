from sys import stdin

input = lambda: stdin.readline().rstrip()

num = 123456 * 2 + 1
num_list = [1] * num
for ii in range(1, num):
    if ii == 1:
        continue
    for jj in range(2, int(ii**0.5) + 1):
        if ii % jj == 0:
            num_list[ii] = 0
            break

while True:
    n = int(input())

    if n == 0:
        break

    prime = 0
    for ii in range(n + 1, 2 * n + 1):
        prime += num_list[ii]
    print(prime)
