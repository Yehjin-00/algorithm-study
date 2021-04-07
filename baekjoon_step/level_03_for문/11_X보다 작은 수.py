## Title: X보다 작은 수
## Level: 3_11
## Number: 10871
## Date: 2021.04.08

num, crit = map(int, input().split())

num_list = list(map(int, input().split()))

for i in range(num):
	if num_list[i] < crit:
		print(num_list[i], end=" ")
