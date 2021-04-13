## Title: 분수찾기
## Level: 8_03
## Number: 1193
## Date: 2021.04.13

num = int(input())

i = 0
check = True

while num > 0:
	i += 1
	num -= i
	check = not check

num += i
i += 1

if check:
	print(f"{num}/{i-num}")
else:
	print(f"{i-num}/{num}")

"""
python 은 ! 대신 not 사용해야 한다..
"""