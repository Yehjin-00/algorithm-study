## Title: 파도반 수열
## Level: 15_04
## Number: 9461
## Date: 2022.01.30

# 1 1 1
# 1 1 1 2
# 1 1 1 2 2
# 1 1 2 2 (3)
# 1 2 2 3 (4)
# 2 2 3 4 (5)
# 2 3 4 5 (7) 
# 3 4 5 6 (9)

# 6번째 구할때부터 그 전 5개 중에서 가장 작은 수랑 가장 큰 수 더하기

N = int(input())

P = [0] * 101

P[1] = 1
P[2] = 1
P[3] = 1
P[4] = 2
P[5] = 2

def get_P(n):
	if P[n] == 0:
		P[n] = get_P(n-1) + get_P(n-5)
	return P[n]


for _ in range(N):
	print(get_P(int(input())))