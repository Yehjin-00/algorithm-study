## Title: A+B - 5
## Level: 4_01
## Number: 10952
## Date: 2021.04.08

check = True

while check:
	a, b = map(int, input().split())
	if a == 0 and b == 0:
		check = False
	else:
		print(a+b)