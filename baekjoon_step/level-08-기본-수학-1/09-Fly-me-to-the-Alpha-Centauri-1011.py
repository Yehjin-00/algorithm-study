## Title: Fly me to the Alpha Centauri
## Level: 8_09
## Number: 1011
## Date: 2021.04.13

# 제대로 된 규칙을 먼저 찾는게 중요한 듯 싶다. 처음에 문제 자체를 잘못 접근함.
# 같은 숫자가 반복될 수 있다는 사실을 뒤늦게 깨달았다.

import sys

num = input()

for line in sys.stdin:
	x, y = map(int, line.split())
	distance = y-x

	i = 0
	length = 0
	while length < distance:
	    length += (i//2) + 1
	    i += 1

	print(i)