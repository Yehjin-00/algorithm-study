## Title: 문자열 반복
## Level: 7_04
## Number: 2675
## Date: 2021.04.13

num = int(input())

for i in range(num):
	lst = input().split()
	for char in lst[1]:
		print(char * int(lst[0]), end="")
	print()