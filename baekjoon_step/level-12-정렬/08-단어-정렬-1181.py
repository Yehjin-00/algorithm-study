## Title: 단어 정렬
## Level: 12_08
## Number: 1181
## Date: 2021.05.03

def compare(a, b):
	if a == b:
		return 0
	elif len(a)-len(b)==0:
		for i in range(len(a)):
			if a[i] > b[i]:
				return 1
			elif a[i] < b[i]:
				return -1
	else:
		return len(a)-len(b)


import sys
input = sys.stdin.readline
num = [input().strip() for i in range(int(input()))]

def heapify(a, index, heap_size):
	mini = index
	left = 2*index + 1
	right = 2*index + 2

	if left < heap_size and compare(a[mini], a[left])>0:
		mini = left
	if right < heap_size and compare(a[mini], a[right])>0:
		mini = right
	if mini != index:
		a[mini], a[index] = a[index], a[mini]
		heapify(a, mini, heap_size)

for i in range(len(num)//2-1, -1, -1):
	heapify(num, i, len(num))

for i in range(len(num)-1, -1, -1):
	if i<len(num)-1 and compare(num[i+1], num[0])==0:
		num[0], num[i] = num[i], num[0]
		heapify(num, 0, i)
	else:
		print(num[0])
		num[0], num[i] = num[i], num[0]
		heapify(num, 0, i)
