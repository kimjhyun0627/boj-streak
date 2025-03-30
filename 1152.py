str = input()

spaces = str.count(' ')

if str[0] == ' ':
    spaces -= 1
if str[-1] == ' ':
    spaces -= 1
print(spaces+1)