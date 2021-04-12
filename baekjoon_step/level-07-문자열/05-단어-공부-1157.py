## Title: 단어 공부
## Level: 7_05
## Number: 1157
## Date: 2021.04.13

word = input().upper()
result = ""
n = 0

for i in range(26):
	count = word.count(chr(i+65))
	if count > n:
		result = chr(i+65)
		n = count
	elif count == n:
		result = '?'

print(result)