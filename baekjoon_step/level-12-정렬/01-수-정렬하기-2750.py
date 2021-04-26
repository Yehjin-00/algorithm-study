## Title: 수 정렬하기
## Level: 12_01
## Number: 2750
## Date: 2021.04.26

# 파이썬 개꿀
import sys

num = sys.stdin.readline()
num = []
for line in sys.stdin.readlines():
	num.append(int(line))

num.sort()
for i in num:
	print(i)

# 삽입 정렬
# https://gmlwjd9405.github.io/2018/05/06/algorithm-insertion-sort.html
import sys

num = sys.stdin.readline()
num = []
for line in sys.stdin.readlines():
	num.append(int(line))

for i in range(1, len(num)):
	for n in range(i):
		if num[n] > num[i]:
			temp = num[i]
			for idx in range(i-n):
				num[i-idx] = num[i-idx-1]
			num[n] = temp
			break

for i in num:
	print(i)
		
# 거품 정렬
# https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html
import sys

num = sys.stdin.readline()
num = []
for line in sys.stdin.readlines():
	num.append(int(line))

def swap(lst, a, b):
	temp = lst[a]
	lst[a] = lst[b]
	lst[b] = temp
	return lst

for i in range(len(num)-1):
	for n in range(len(num)-1-i):
		if num[n] > num[n+1]:
			num = swap(num, n, n+1)

for i in num:
	print(i)


"""
python list sort
- sorted(list) -> sort한 리스트값 반환. 원래의 list는 변하지 않음.
- list.sort() -> list sort하고 아무것도 반환 안함. 원래의 list 변함.

정렬
- 삽입 정렬
- 거품 정렬
정리
"""