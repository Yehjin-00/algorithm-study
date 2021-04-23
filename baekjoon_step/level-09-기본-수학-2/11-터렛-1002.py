## Title: 터렛
## Level: 9_11
## Number: 1002
## Date: 2021.04.23

import sys

num = sys.stdin.readline()

for line in sys.stdin:
	x1, y1, r1, x2, y2, r2 = map(int, line.split())

	if (x1, y1) == (x2, y2):
		if r1==r2:
			print(-1)
		else:
			print(0)
	else:
		distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
		if distance > r1+r2 or distance < abs(r1-r2):
			print(0)
		elif distance == r1+r2 or distance == abs(r1-r2):
			print(1)
		else:
			print(2)
