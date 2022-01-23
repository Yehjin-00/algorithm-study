## Title: 신나는 함수 실행
## Level: 15_02
## Number: 9184
## Date: 2022.01.23

# description
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)


# 통과
def w(n1, n2, n3):

	tuple3 = (n1, n2, n3)

	if n1 <= 0 or n2 <= 0 or n3 <= 0:
		return 1

	elif tuple3 in w_dict:
		return w_dict[tuple3]

	elif n1 > 20 or n2 > 20 or n3 > 20:
		return w(20, 20, 20)

	elif n1 < n2 and n2 < n3:
		result = w(n1, n2, n3-1) + w(n1, n2-1, n3-1) - w(n1, n2-1, n3)
		w_dict[tuple3] = result
		return result

	else:
		result = w(n1-1, n2, n3) + w(n1-1, n2-1, n3) + w(n1-1, n2, n3-1) - w(n1-1, n2-1, n3-1)
		w_dict[tuple3] = result
		return result

n1, n2, n3 = map(int, input().split())
w_dict = {}
while n1 != -1 or n2 != -1 or n3 != -1:
	result_lst = []
	print(f"w({n1}, {n2}, {n3}) = {w(n1, n2, n3)}")
	n1, n2, n3 = map(int, input().split())

