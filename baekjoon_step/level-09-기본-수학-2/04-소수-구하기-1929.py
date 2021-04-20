## Title: 소수 구하기
## Level: 9_04
## Number: 1929
## Date: 2021.04.19

a, b = map(int, input().split())

check_list = [True] * (b+1)
check_list[1] = False

for i in range(2, int(b**0.5)+1):
	if not check_list[i]: continue
	for v in range(i*2, b+1, i):
		check_list[v] = False

for idx, value in enumerate(check_list):
	if idx>=a and value:
		print(idx)