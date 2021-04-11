## Title: A+B
## Level: 1_05
## Number: 1000
## Date: 2021.04.06

a = input()
a = a.split()

print(int(a[0]) + int(a[1]))

"""
a, b = map(int, input().split())
print(a+b)


map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. 
map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.

"""