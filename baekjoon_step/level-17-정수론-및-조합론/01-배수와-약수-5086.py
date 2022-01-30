## Title: 배수와 약수
## Level: 17_01
## Number: 5086
## Date: 2022.01.30

while True:
	a, b = map(int, input().split())

	# 종료 조건
	if a+b == 0: 
		break

	# 실행
	if a%b==0:
		print('multiple')
	elif b%a==0:
		print('factor')
	else:
		print('neither')
