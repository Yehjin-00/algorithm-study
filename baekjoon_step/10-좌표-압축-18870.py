## Title: 좌표 압축
## Level: 12_10
## Number: 18870
## Date: 2021.05.04


# 시간 초과
num = input()
num = list(map(int, input().split()))

for i in range(len(num)):
	num[i] = [num[i], i]

num.sort()

index = 0
before = 0
for i in range(len(num)):
	if i==0 or num[i][0]!=before:
		index = i
	before = num[i][0]
	num[i] = [num[i][1], index]

num.sort()

for value in num:
	print(value[1], end=' ')


# 재도전
n = int(input())
num = list(map(int, input().split()))
ranking = sorted(list(set(num)))
rank_dict = {ranking[i] : i for i in range(len(ranking))}

for i in num:
	print(rank_dict[i], end=' ')