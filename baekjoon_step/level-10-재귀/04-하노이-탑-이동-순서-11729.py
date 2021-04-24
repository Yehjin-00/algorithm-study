## Title: 하노이 탑 이동 순서
## Level: 10_04
## Number: 11729
## Date: 2021.04.24

def move(n, start, end, lst, count):
    if n == 1:
        lst.append(f"{start} {end}")
        count += 1
        return count
    else:
        where = list(set([1,2,3])-set([start,end]))[0]
        count = move(n-1, start, where, lst, count)
        lst.append(f"{start} {end}")
        count = move(n-1, where, end, lst, count)
        count += 1
        return count

lst = []
count = move(int(input()), 1, 3, lst, 0)

print(count)
for i in lst:
    print(i)


# 조오금 발전시킨 코드
def move(n, start, end):
    if n == 1:
        print(start, end)
    else:
        where = 6-start-end
        move(n-1, start, where)
        print(start, end)
        move(n-1, where, end)

num = int(input())
print(2**num-1)
move(num, 1, 3)