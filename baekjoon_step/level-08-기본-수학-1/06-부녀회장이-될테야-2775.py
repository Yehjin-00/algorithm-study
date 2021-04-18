## Title: 부녀회장이 될테야
## Level: 8_06
## Number: 2775
## Date: 2021.04.18

# 첫번째 풀이: 재귀를 써보자! -> 시간초과

# a층 b호
# a층 (b-1)호 + (a-1)층 b호

import sys

def living_people(a, b):
	if a == 0:
		return b
	elif b == 1:
		return 1
	else:
		return living_people(a, b-1) + living_people(a-1, b)


num = int(input())
for i in range(num):
	k = int(sys.stdin.readline())
	n = int(sys.stdin.readline())
	print(living_people(k, n))


# 두번째 풀이: 그냥 문제 그대로 구현 -> 통과

# 3층: 1 5 15 35
# 2층: 1 4 10 20
# 1층: 1 3 6 10
# 0층: 1 2 3 4 
# -층: 1 1 1 1 1 1 1 1 

import sys

num = int(input())
for i in range(num):
	k = int(sys.stdin.readline())
	n = int(sys.stdin.readline())
	
	floor = [1] * n

	for i in range(k+1):
		temp = [1] * n
		for room in range(n):
			temp[room] = sum(floor[:room+1])
		floor = temp
	print(floor[-1])


# 세번째 풀이: Combination 사용 -> 통과

import sys

num = int(input())
for i in range(num):
	k = int(sys.stdin.readline())
	n = int(sys.stdin.readline())

	a = 1
	b = 1
	
	for i in range(k+1):
		a *= k+n-i
		b *= k+1-i

	print(int(a/b))











