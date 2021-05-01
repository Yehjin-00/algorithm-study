## Title: 수 정렬하기 - 2
## Level: 12_02
## Number: 2751
## Date: 2021.05.01

# 병합 정렬 (시간 초과)
import sys

num = sys.stdin.readline()
num = []
for line in sys.stdin.readlines():
	num.append(int(line))

def merge(a, b):
	result = []
	while len(a) + len(b) != 0:
		if len(a) == 0:
			result += b
			b = []
		elif len(b) == 0:
			result += a
			a = []
		elif a[0] < b[0]:
			result.append(a.pop(0))
		else:
			result.append(b.pop(0))
	return result

def mergesort(c):
	if len(c) > 1:
		a = mergesort(c[:len(c)//2])
		b = mergesort(c[len(c)//2:])
		return merge(a, b)
	else:
		return c

for i in mergesort(num):
	print(i)

# 병합 정렬 2차 시도
import sys

num = sys.stdin.readline()
num = []
for line in sys.stdin.readlines():
	num.append(int(line))

def merge(a, b):
	result = []
	m, n = 0, 0
	while True:
		if m == len(a):
			result += b[n:]
			return result
		elif n == len(b):
			result += a[m:]
			return result
		elif a[m] < b[n]:
			result.append(a[m])
			m += 1
		else:
			result.append(b[n])
			n += 1
	return []

def mergesort(c):
	if len(c) > 1:
		a = mergesort(c[:len(c)//2])
		b = mergesort(c[len(c)//2:])
		return merge(a, b)
	else:
		return c

for i in mergesort(num):
	print(i)

# 힙 정렬 (시간 초과)
import sys

num = sys.stdin.readline()
num = []
for line in sys.stdin.readlines():
	num.append(int(line))

def heapify(a):
	for i in range(len(a)//2-1, -1, -1):
		if a[i] > a[i*2+1]:
			a[i], a[i*2+1] = a[i*2+1], a[i]
		if len(a)>=i*2+3 and a[i] > a[i*2+2]:
			a[i], a[i*2+2] = a[i*2+2], a[i]
	return a

while len(num)>0:
	num = heapify(num)
	print(num[0])
	num = num[1:]

# 힙 정렬 (재도전-성공)
# https://ratsgo.github.io/data%20structure&algorithm/2017/09/27/heapsort/
num = [int(input()) for i in range(int(input()))]

def heapify(a, index, heap_size):
	mini = index
	left = 2*index + 1
	right = 2*index + 2

	if left < heap_size and a[mini] > a[left]:
		mini = left
	if right < heap_size and a[mini] > a[right]:
		mini = right
	if mini != index:
		a[mini], a[index] = a[index], a[mini]
		heapify(a, mini, heap_size)

for i in range(len(num)//2-1, -1, -1):
	heapify(num, i, len(num))

for i in range(len(num)-1, -1, -1):
	print(num[0])
	num[0], num[i] = num[i], num[0]
	heapify(num, 0, i)



