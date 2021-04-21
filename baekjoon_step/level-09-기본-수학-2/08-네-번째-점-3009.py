## Title: 네 번째 점
## Level: 9_08
## Number: 3009
## Date: 2021.04.21

x = []
y = []

for i in range(3):
	a, b = map(int, input().split())
	if a not in x:
		x.append(a)
	else:
		x.remove(a)

	if b not in y:
		y.append(b)
	else:
		y.remove(b)

print(x[0], y[0])