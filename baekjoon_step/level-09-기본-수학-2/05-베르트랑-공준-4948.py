## Title: 베르트랑 공준
## Level: 9_05
## Number: 4948
## Date: 2021.04.19


import sys

for line in sys.stdin.readlines():
	a = int(line)
	b = 2*a

	if a > 0:
	    check_list = [1] * (b+1)
	    
	    for i in range(2, int(b**0.5)+1):
	        if check_list[i] == 0: continue
	        for v in range(i*2, b+1, i):
	            check_list[v] = 0

	    for i in range(a+1):
	        check_list[i] = 0

	    print(sum(check_list))