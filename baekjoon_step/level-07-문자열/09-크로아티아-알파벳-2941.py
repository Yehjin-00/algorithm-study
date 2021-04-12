## Title: 크로아티아 알파벳
## Level: 7_09
## Number: 2941
## Date: 2021.04.13

alphabet = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

result = 0
word = input()
n = len(word)

for letter in alphabet:
	count = word.count(letter)
	result += count
	n -= len(letter) * count

result += n
result -= word.count('dz=')

print(result)

"""
- dz= & z= 처리하기
- 포함되지 않는 문자 처리하기
"""