## Title: 블랙잭
## Level: 11_01
## Number: 2798
## Date: 2021.04.25

num, target = map(int, input().split())
card = list(map(int, input().split()))

i = 0
result = 0
for first in range(num-2):
	for second in range(first+1, num-1):
		for third in range(second+1, num):
			total = card[first] + card[second] + card[third]
			if total <= target and total > result:
				result = total

print(result)