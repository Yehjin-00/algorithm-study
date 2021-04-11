## Title: 최댓값
## Level: 5_02
## Number: 2562
## Date: 2021.04.10

import sys

lst = list(map(int, sys.stdin.readlines()))
maxi = lst[0]
idx = 0

for i, num in enumerate(lst):
	if num > maxi:
		maxi = num
		idx = i

print(maxi)
print(idx+1)