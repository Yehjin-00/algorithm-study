## Title: 영화감독 숌
## Level: 11_05
## Number: 1436
## Date: 2021.04.25

num = int(input())
i = 0
count = 0
while True:
	i += 1
	if '666' in str(i):
		count += 1
		if count == num:
			print(i)
			break