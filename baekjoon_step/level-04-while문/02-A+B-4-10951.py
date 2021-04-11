## Title: A+B - 4
## Level: 4_02
## Number: 10951
## Date: 2021.04.08

import sys

for line in sys.stdin:
	a, b = map(int, line.split())
	print(a+b)

"""
EOF (end of file) 처리하기

for line in sys.stdin:
	--line--

for line in sys.stdin.readlines():
	--line--
"""