## Title: 큰 수 A+B
## Level: 8_08
## Number: 10757
## Date: 2021.04.13


# 파이썬 짱짱
a, b = map(int, input().split())
print(a+b)


# C/C++로 생각해봐야함-!
# 일단은 파이썬으로 자리수별로 계산하는거!

a, b = map(str, input().split())

zero_num = len(a)-len(b)

if zero_num > 0:
	b = "0"*zero_num + b
else:
	a = "0"*((-1)*zero_num) + a

total = ""
carry = 0
for i in range(len(a)):
	idx = len(a)-1-i
	result = int(a[idx])+int(b[idx])+carry
	if result > 9:
		total = str(result-10) + total
		carry = 1
	else:
		total = str(result) + total
		carry = 0

if carry == 1:
	print("1"+total)
else:
	print(total)