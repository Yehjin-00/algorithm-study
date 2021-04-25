## Title: 체스판 다시 칠하기
## Level: 11_04
## Number: 1018
## Date: 2021.04.25

import sys

n, m = map(int, sys.stdin.readline().split())

b = 'BWBWBWBW'
w = 'WBWBWBWB'

tile = []
for line in sys.stdin:
	tile.append(line)

result = []
for col in range(m-8+1):
	for row in range(n-8+1):
		count = 0
		check = True
		for r in range(8):
			if check:
				for c in range(8):
					if tile[row+r][col+c] != b[c]:
						count += 1
				check = not check
			else:
				for c in range(8):
					if tile[row+r][col+c] != w[c]:
						count += 1
				check = not check
		result.append(min([count, 64-count]))

print(min(result))