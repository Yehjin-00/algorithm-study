## Title: 별 찍기 - 2
## Level: 3_10
## Number: 2439
## Date: 2021.04.08

num = int(input())

for i in range(num):
	print(" "*(num-i-1) + "*"*(i+1))


"""
f-formatting align option

f"{x: >{num}}"
-> 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 num자리 공간을 확보
-> 그냥 상수 넣을 때는 {} 필요 없음
"""