## Title: 직사각형에서 탈출
## Level: 9_07
## Number: 1085
## Date: 2021.04.21

x, y, w, h = map(int, input().split())

print(min([w-x, x, h-y, y]))