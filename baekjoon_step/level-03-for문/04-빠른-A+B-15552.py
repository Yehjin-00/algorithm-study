## Title: 빠른 A+B
## Level: 3_04
## Number: 15552
## Date: 2021.04.08

import sys

num = int(input())

for i in range(num):
	a, b = map(int, sys.stdin.readline().split())
	print(a+b)

"""
sys.stdin.readline()

- input()과 동일하게 사용가능!
- 사용하는 이유? 시간적으로 input()보다 좋다!
- 한 줄을 받을때 주의!
	: line 별로 읽어서 \n 이 포함되어 있으니 마지막에 .rstrip() 혹은 .strip() 사용하기!
"""