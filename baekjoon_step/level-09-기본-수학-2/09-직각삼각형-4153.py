## Title: 직각삼각형
## Level: 9_09
## Number: 4153
## Date: 2021.04.23

import sys

def double(n):
	return int(n)**2

for line in sys.stdin:
	a = list(map(double, line.split()))
	if sum(a)==0:
		continue
	elif sum(a)//2 in a:
		print('right')
	else:
		print('wrong')