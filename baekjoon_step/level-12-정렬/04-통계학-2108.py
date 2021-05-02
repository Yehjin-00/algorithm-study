## Title: 통계학
## Level: 12_04
## Number: 2108
## Date: 2021.05.02

import sys

input = sys.stdin.readline
n = int(input())
count = [0] * 8001

for i in range(n):
    count[int(input())+4000] += 1

maxi = 0
num = []
check = True
for i in range(8001):
	if count[i] > count[maxi]:
		maxi = i
		check = True
	elif count[i] == count[maxi] and check and i != maxi:
		maxi = i
		check = False
	for j in range(count[i]):
		num.append(i-4000)

print(round(sum(num)/len(num)))
print(num[len(num)//2])
print(maxi-4000)
print(num[-1]-num[0])
