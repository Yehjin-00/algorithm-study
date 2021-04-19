## Title: 소수 찾기
## Level: 9_01
## Number: 1978
## Date: 2021.04.19

input_list = input()
input_list = sorted(list(map(int, input().split())))

prime_list = []
num_list = list(range(2, max(input_list)+1))

while len(num_list) > 0:
	pop = num_list.pop(0)
	num_list = [v for v in num_list if v%pop!=0]
	prime_list.append(pop)

print(len(set(prime_list)&set(input_list)))

"""
set 교집합: & 기호
"""
