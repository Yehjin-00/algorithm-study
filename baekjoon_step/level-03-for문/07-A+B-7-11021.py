## Title: A+B - 7
## Level: 3_07
## Number: 11021
## Date: 2021.04.08

import sys

num = int(input())

for i in range(num):
	a, b = map(int, sys.stdin.readline().split())
	print(f"Case #{i+1}: {a+b}")