## Title: 소수
## Level: 9_02
## Number: 2581
## Date: 2021.04.19

# 내 코드

a, b = int(input()), int(input())

prime_list = []
num_list = list(range(2, b+1))

while len(num_list) > 0:
	pop = num_list.pop(0)
	num_list = [v for v in num_list if v%pop!=0]
	if pop >= a:
		prime_list.append(pop)

if len(prime_list)>0: 
	print(sum(prime_list))
	print(prime_list[0])
else:
	print(-1)


# 백준에서 발견한 어떤 분(cynicaldummy)의 코드

def seive(M, N):
    is_prime = [True] * (N+1)
    is_prime[1] = False

    for n in range(2, int(N**0.5)+1):
        if not is_prime[n]: continue

        for m in range(n*2, N+1, n):
            is_prime[m] = False

    return [i for i in range(M, N+1) if is_prime[i]]

M = int(input())
N = int(input())
primes = seive(M, N)

if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)

"""
N이 소수인지 판단할 때, N**0.5 이하의 숫자들의 배수만 확인하면 된다.
그 이상의 숫자들의 곱으로는 절대 N을 구하지 못한다.
"""
