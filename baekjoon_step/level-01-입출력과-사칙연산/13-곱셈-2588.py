## Title: 곱셈
## Level: 1_13
## Number: 2588
## Date: 2021.04.06

a = int(input())
b = int(input())

c = a*(b%10)
d = a*((b//10)%10)
e = a*(b//100)
f = a * b

print(c, d, e, f)