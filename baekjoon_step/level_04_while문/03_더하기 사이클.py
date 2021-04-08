## Title: 더하기 사이클
## Level: 4_03
## Number: 1110
## Date: 2021.04.08

target = input()
cycle = 1

if len(target) == 1:
	target = "0" + target

num = target[1] + str(int(target[0])+int(target[1]))[-1]

while target != num:
	num = num[1] + str(int(num[0]) + int(num[1]))[-1]
	cycle += 1

print(cycle)

"""
string 으로 접근하지 않고 아래와 같이 몫과 나머지로도 접근이 가능해보인다.
"""

target = int(input())
num = (target%10)*10 + (target//10+target%10)%10
cycle = 1

while target != num:
	cycle += 1
	num = (num%10)*10 + (num//10+num%10)%10

print(cycle)