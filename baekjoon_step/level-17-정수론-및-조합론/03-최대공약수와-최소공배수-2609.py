## Title: 최대공약수와 최소공배수
## Level: 17_03
## Number: 2609
## Date: 2022.01.30

a, b = map(int, input().split())

if a%b==0:
	print(b)
	print(a)

elif b%a==0:
	print(a)
	print(b)

else:
	a, b = min(a, b), max(a, b)
	for i in range(2, a+1):
		if a%i==0 and b%(a//i)==0:
			m = a//i
			print(m)
			print((a*b)//m)
			break