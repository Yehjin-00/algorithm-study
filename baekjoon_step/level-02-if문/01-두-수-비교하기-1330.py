## Title: 두 수 비교하기
## Level: 2_01
## Number: 1330
## Date: 2021.04.06

a, b = map(int, input().split())

if (a-b) > 0:
	print(">")
elif (a-b) < 0:
	print("<")
else:
	print("==")