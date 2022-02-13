## Title: 나머지
## Level: 1_12
## Number: 10430
## Date: 2021.04.06

A, B, C = map(int, input().split())
print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C)