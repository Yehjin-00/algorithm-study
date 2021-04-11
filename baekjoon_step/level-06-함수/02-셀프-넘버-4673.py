## Title: 셀프 넘버
## Level: 6_02
## Number: 4673
## Date: 2021.04.11

def d(n):
	result = n
	for char in str(n):
		result += int(char)
	return result

d_lst = [d(n) for n in range(10000)]

for i in range(1, 10001):
	if i not in d_lst:
		print(i)

"""
set 자료형
- 그냥 집합임
- 차집합 구하기: set(list) - set(list)
"""