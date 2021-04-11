## Title: 한수
## Level: 6_03
## Number: 1065
## Date: 2021.04.11

def solve(n):
	if n < 100:
		return 1
	elif n//100+n%10 == (n//10%10)*2:
		return 1
	else:
		return 0

num = int(input())
print(sum(solve(i) for i in range(1, num+1)))