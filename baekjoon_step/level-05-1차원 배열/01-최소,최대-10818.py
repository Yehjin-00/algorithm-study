## Title: 최소, 최대
## Level: 5_01
## Number: 10818
## Date: 2021.04.10

num = int(input())
lst = list(map(int, input().split()))

print(min(lst), max(lst))

"""
min, max 함수 안 쓰기

num = int(input())
lst = list(map(int, input().split()))

mini = lst[0]
maxi = lst[0]

for i in lst:
	if i < mini:
		mini = i
	if i > maxi:
		maxi = i

print(mini, maxi)

"""