hh, mm = map(int, input().split())

t = hh*60 + mm - 45
if t < 0:
    t += 24*60

print(t//60, t%60)