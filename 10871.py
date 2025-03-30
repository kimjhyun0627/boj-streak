n, x = map(int, input().split())
nums = list(map(int, input().split()))

print(' '.join(map(str, [n for n in nums if n < x])))