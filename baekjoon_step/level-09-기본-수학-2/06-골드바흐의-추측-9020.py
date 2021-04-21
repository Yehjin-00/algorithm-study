## Title: 골드바흐의 추측
## Level: 9_06
## Number: 9020
## Date: 2021.04.21

import sys

b = input()
b = 10000

# prime list 만들기
check_list = [True] * (b+1)
check_list[1] = False

for i in range(2, int(b**0.5)+1):
	if not check_list[i]: continue
	for v in range(i*2, b+1, i):
		check_list[v] = False

prime_list = [i for i in range(2, b+1) if check_list[i]]

for line in sys.stdin:
	line = int(line)
	x = line//2

	if x!=2 and x%2==0:
		x -= 1

	while line-x not in prime_list or x not in prime_list:
			x -= 2
	print(x, line-x)