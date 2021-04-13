## Title: 달팽이는 올라가고 싶다
## Level: 8_04
## Number: 2869
## Date: 2021.04.13


# 시간 초과 코드
a, b, v = map(int, input().split())

climb = 0
day = 0

while climb < v:
	climb += a
	day += 1
	if climb < v:
		climb -= b

print(day)


# 시간 내에 잘 실행된 코드
import math

a, b, v = map(int, input().split())

print(math.ceil((v-a)/(a-b)) + 1)

# n >= (v - a) / (a - b)