## Title: 좌표 정렬하기 2
## Level: 12_07
## Number: 11651
## Date: 2021.05.03

def compare(a, b):
	if a[1] > b[1]:
		return True
	elif a[1] < b[1]:
		return False
	elif a[0] > b[0]:
		return True
	else:
		return False

import sys
input = sys.stdin.readline
num = [list(map(int, input().split())) for i in range(int(input()))]

def heapify(a, index, heap_size):
	mini = index
	left = 2*index + 1
	right = 2*index + 2

	if left < heap_size and compare(a[mini], a[left]):
		mini = left
	if right < heap_size and compare(a[mini], a[right]):
		mini = right
	if mini != index:
		a[mini], a[index] = a[index], a[mini]
		heapify(a, mini, heap_size)

for i in range(len(num)//2-1, -1, -1):
	heapify(num, i, len(num))

for i in range(len(num)-1, -1, -1):
	print(num[0][0], num[0][1])
	num[0], num[i] = num[i], num[0]
	heapify(num, 0, i)