## Title: OX퀴즈
## Level: 5_06
## Number: 8958
## Date: 2021.04.10

import sys

num = int(input())

for line in sys.stdin:
	result = 0
	score = 1

	for char in line:
		if char == "O":
			result += score
			score += 1
		else:
			score = 1

	print(result)


"""
sys.stdin 에 대해서 좀 더 자세한 이해가 필요해보인다.
"""