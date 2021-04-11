## Title: 평균은 넘겠지
## Level: 5_07
## Number: 4344
## Date: 2021.04.10

import sys

num = int(input())

for line in sys.stdin:
	line = list(map(int, line.split()))

	line = line[1:]

	av = sum(line)/len(line)
	ratio = len([v for v in line if v > av])/len(line)*100

	print(f"{ratio:.3f}%")