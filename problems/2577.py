a = int(input())
b = int(input())
c = int(input())
res = str(a * b * c)

for ii in range(0, 10):
    print(res.count(str(ii)))