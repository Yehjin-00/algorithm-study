## Title: 다이얼
## Level: 7_08
## Number: 5622
## Date: 2021.04.13

result = 0

for char in input():
	if ord(char) > 90:
		result += 0
	elif ord(char) > 86:
		result += 10
	elif ord(char) > 83:
		result += 9
	elif ord(char) > 79:
		result += 8
	else:
		result += (ord(char)-56)//3

print(result)