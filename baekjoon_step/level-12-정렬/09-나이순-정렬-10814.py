## Title: 나이순 정렬
## Level: 12_09
## Number: 10814
## Date: 2021.05.04

import sys
input = sys.stdin.readline

n = int(input())
member = []

for i in range(n):
	member.append([i]+input().split())

def compare(m1, m2):
	if m1[1]==m2[1]:
		return m1[0]-m2[0]
	else:
		return int(m1[1])-int(m2[1])

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

for i in range(len(member)//2-1, -1, -1):
	heapify(member, i, len(member))

for i in range(len(member)-1, -1, -1):
	print(member[0][1], member[0][2])
	member[0], member[i] = member[i], member[0]
	heapify(member, 0, i)