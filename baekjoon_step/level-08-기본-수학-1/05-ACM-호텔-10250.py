## Title: ACM 호텔
## Level: 8_05
## Number: 10250
## Date: 2021.04.17

import sys 

num = int(input())

for line in sys.stdin:
	h, w, n = map(int, line.split())
	room = (n-1)//h + 1
	floor = (n-1)%h + 1
	print(floor*100+room)
	