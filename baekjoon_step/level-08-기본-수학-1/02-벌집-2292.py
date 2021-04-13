## Title: 벌집
## Level: 8_02
## Number: 2292
## Date: 2021.04.13

num = int(input())
i = 0

while num > 0:
	if i == 0:
		num -= 1
	else:
		num -= i * 6
	i += 1

print(i)