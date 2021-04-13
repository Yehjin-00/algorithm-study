## Title: 손익분기점
## Level: 8_01
## Number: 1712
## Date: 2021.04.13

import math

a, b, c = map(int, input().split())

# c * 판매량 - (a + b * 판매량) > 0
# 판매량 > a / (c-b)
# 판매량 < a / (b-c)

if c - b > 0:
	print(math.floor((a/(c-b)+1)))
else:
	print(-1)