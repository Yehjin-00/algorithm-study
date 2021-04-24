## Title: 별 찍기 - 10
## Level: 10_03
## Number: 2447
## Date: 2021.04.24

def star(n):
    if n == 3:
        return ['***', '* *', '***']
    else:
        pre = star(n//3)
        result = []
        for line in pre:
            result.append(line*3)
        for line in pre:
            result.append(line+' '*len(line)+line)
        for line in pre:
            result.append(line*3)
        return result

for i in star(int(input())):
    print(i)