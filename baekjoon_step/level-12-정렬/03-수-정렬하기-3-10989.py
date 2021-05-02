## Title: 수 정렬하기 3
## Level: 12_03
## Number: 10989
## Date: 2021.05.02

# 카운팅 정렬
import sys

input = sys.stdin.readline
n = int(input())
count = [0] * 10000

for i in range(n):
    count[int(input())-1] += 1

for i in range(10000):
    for j in range(count[i]):
        print(i+1)