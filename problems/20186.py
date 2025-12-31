# https://www.acmicpc.net/problem/20186

from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

print(sum(sorted(arr, reverse=True)[:K]) - sum([ii for ii in range(K)]))
