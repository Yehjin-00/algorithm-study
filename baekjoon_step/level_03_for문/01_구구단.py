## Title: 구구단
## Level: 3_01
## Number: 2739
## Date: 2021.04.08

num = int(input())

for i in range(9):
	result = num * (i+1)
	print(f"{num} * {i+1} = {result}")