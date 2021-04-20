## Title: 소인수분해
## Level: 9_03
## Number: 11653
## Date: 2021.04.19

# 사용자로부터 input 받기
num = int(input())

# 소수 리스트 구하기
is_prime = [True] * (num+1)
is_prime[1] = False

for n in range(2, int(num**0.5)+1):
    if not is_prime[n]: continue
    for m in range(n*2, num+1, n):
        is_prime[m] = False

prime_list = [i for i in range(2, num+1) if is_prime[i]]

# 가장 작은 소수로 나누기 (recursion)
def divide(lst, n):
	if n in prime_list:
		lst.append(n)
	else:
		for prime in prime_list:          
			if n%prime==0:
				lst.append(prime)
				divide(lst, n//prime)
				break

result = []
divide(result, num)

for prime in sorted(result):
	print(prime)