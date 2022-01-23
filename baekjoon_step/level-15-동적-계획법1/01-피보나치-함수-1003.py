## Title: 피보나치 함수
## Level: 15_01
## Number: 1003
## Date: 2022.01.23

# memoization
N = int(input())
f_dict = {0:(1,0), 1:(0,1)}

def fibonacci(num, zero_lst, one_lst):
	if num in f_dict:
		zero_lst.append(f_dict[num][0])
		one_lst.append(f_dict[num][1])
	else:
		if num-1 in f_dict:
			zero_lst.append(f_dict[num-1][0])
			one_lst.append(f_dict[num-1][1])
		else:
			zero_sum = sum(zero_lst)
			one_sum = sum(one_lst)
			fibonacci(num-1, zero_lst, one_lst)
			f_dict[num-1] = (sum(zero_lst)-zero_sum, sum(one_lst)-one_sum)

		if num-2 in f_dict:
			zero_lst.append(f_dict[num-2][0])
			one_lst.append(f_dict[num-2][1])
		else:
			zero_sum = sum(zero_lst)
			one_sum = sum(one_lst)
			fibonacci(num-2, zero_lst, one_lst)
			f_dict[num-2] = (sum(zero_lst)-zero_sum, sum(one_lst)-one_sum)

for _ in range(N):
	n = int(input())
	zero_lst = []
	one_lst = []
	fibonacci(n, zero_lst, one_lst)
	print(sum(zero_lst), sum(one_lst))

# 시간 초과
N = int(input())

def fibonacci(num, zero_lst, one_lst):
	if num == 0:
		zero_lst.append(1)
	elif num == 1:
		one_lst.append(1)
	else:
		fibonacci(num-2, zero_lst, one_lst)
		fibonacci(num-1, zero_lst, one_lst)

for _ in range(N):
	n = int(input())
	zero_lst = []
	one_lst = []
	fibonacci(n, zero_lst, one_lst)
	print(sum(zero_lst), sum(one_lst))