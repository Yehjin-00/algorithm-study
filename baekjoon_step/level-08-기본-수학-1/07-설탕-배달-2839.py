## Title: 설탕 배달
## Level: 8_07
## Number: 2839
## Date: 2021.04.18

num = int(input())

small = 0
while num%5!=0 and num>0:
	num -= 3
	small += 1

if num<0:
	print(-1)
else:
	print(small + (num//5))
	