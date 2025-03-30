n = int(input())

for ii in range(n):
    res = input()
    cont = 0
    score = 0
    for r in res:
        if r == 'O':
            cont += 1
            score += cont
        else:
            cont = 0
    
    print(score)