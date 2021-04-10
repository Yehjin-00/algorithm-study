## Title: 나머지
## Level: 5_04
## Number: 10818
## Date: 2021.04.10

import sys

lst = list(map(int, sys.stdin.readlines()))

mod = []
for i in range(10):
	if lst[i]%42 not in mod:
		mod.append(lst[i]%42)

print(len(mod))