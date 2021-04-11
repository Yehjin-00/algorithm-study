## Title: 사분면 고르기
## Level: 2_04
## Number: 14681
## Date: 2021.04.06

x = int(input())
y = int(input())

if x > 0:
	if y > 0:
		print(1)
	else:
		print(4)
elif y > 0:
	print(2)
else:
	print(3)