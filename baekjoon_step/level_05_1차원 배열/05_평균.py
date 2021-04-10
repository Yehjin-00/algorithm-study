## Title: 평균
## Level: 5_05
## Number: 1546
## Date: 2021.04.10

num = input()
num = list(map(int, input().split()))

def cheat(n):
	return n/max(num)*100

num = list(map(cheat, num))

print(sum(num)/len(num))


"""
lambda 사용한 map

num = input()
num = list(map(int, input().split()))
num = list(map(lambda x: x/max(num)*100, num))

print(sum(num)/len(num))
"""