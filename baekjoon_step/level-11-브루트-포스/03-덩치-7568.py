## Title: 덩치
## Level: 11_03
## Number: 7568
## Date: 2021.04.24

import sys

def compare(a, b):
	if a[0] > b[0] and a[1] > b[1]:
		return True
	else: 
		return False

num = sys.stdin.readline()

people = []
for line in sys.stdin:
	people.append(list(map(int, line.split())))

for person in people:
	rank = 1
	for c_person in people:
		if compare(c_person, person):
			rank += 1
	print(rank, end=" ")