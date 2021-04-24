## Title: 피보나치 수 - 5
## Level: 10_02
## Number: 10870
## Date: 2021.04.24

def fibo(n):
	if n < 2:
		return n
	else:
		return fibo(n-1) + fibo(n-2)

print(fibo(int(input())))