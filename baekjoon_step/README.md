# 백준 단계별로 풀기 정리

## 1. sys

### sys.stdin.readline() # 3_04

- input()과 동일하게 사용가능!
- 사용하는 이유? 시간적으로 input()보다 좋다!
- 한 줄을 받을때 주의!
	: line 별로 읽어서 \n 이 포함되어 있으니 마지막에 .rstrip() 혹은 .strip() 사용하기!

### EOF (end of file) 처리하기 # 4_02

	for line in sys.stdin:
		--line--

	for line in sys.stdin.readlines():
		--line--


## 2. map

### map function # 1_05

	a, b = map(int, input().split())
	print(a+b)

- map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. 
- map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.


### lambda 사용한 map # 5_05

	num = list(map(int, input().split()))
	num = list(map(lambda x: x/max(num)*100, num))

## 3. set

### set 자료형 # 6_02
- 그냥 집합임
- 차집합 구하기: set(list) - set(list)
- 교집합 구하기: set(list) & set(list)

## 4. string

### string 거꾸로 하기 # 7_07

	a = 'string'
	print(a[::-1])

### str count 함수 # 5_03

	string.count(text)

- string 안에 들어있는 text 개수를 세어준다.

## 5. 소수

### 소수 구하기 알고리즘 # 9_01 # 9_02

- [소수(Prime Number) 구하기 효율적 알고리즘 :: 코드자몽](https://myjamong.tistory.com/139)
- N이 소수인지 판단할 때, N**0.5 이하의 숫자들의 배수만 확인하면 된다.
- 그 이상의 숫자들의 곱으로는 절대 N을 구하지 못한다.

## 0. 기타 python 문법

### f-formatting align option # 3_10

	f"{x: >{num}}"

- 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 num자리 공간을 확보
- 그냥 상수 넣을 때는 {} 필요 없음

# 다시 풀어보면 좋을 문제

- 7_10 그룹 단어 체커 (1316)
- 8_02 벌집 (2292)
- 8_06 부녀회장이 될테야 (2775)
- 8_08 큰 수 A+B (10757) : 나중에 C++로 풀어보기
- 12_02 수 정렬하기 - 2 (2751) : 기본적인 sort
- 12_09 나이 순 정렬 (10814) : stable sort 개념 정리