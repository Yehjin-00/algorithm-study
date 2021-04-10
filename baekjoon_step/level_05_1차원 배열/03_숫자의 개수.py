## Title: 숫자의 개수
## Level: 5_03
## Number: 2577
## Date: 2021.04.10

import sys

num = int(input())
num *= int(input())
num *= int(input())

num = str(num)

num_dict = {}
for i in range(10):
	num_dict[i] = 0

for char in num:
	num_dict[int(char)] += 1

for i in range(10):
	print(num_dict[i])


"""
str count 함수

string.count(text)
string 안에 들어있는 text 개수를 세어준다.
"""