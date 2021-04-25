## Title: 분해합
## Level: 11_02
## Number: 2231
## Date: 2021.04.25

def get_number(end):	
	for i in range(end):
		total = i
		for char in str(i):
			total += int(char)
		if total == int(num):
			return i
	return 0

num = int(input())
print(get_number(num))