## Title: 팩토리얼
## Level: 10_01
## Number: 10872
## Date: 2021.04.24

def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)

print(factorial(int(input())))