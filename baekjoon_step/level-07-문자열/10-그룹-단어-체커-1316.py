## Title: 그룹 단어 체커
## Level: 7_10
## Number: 1316
## Date: 2021.04.13

num = int(input())
result = 0

for iteration in range(num):
	word = input()
	check = True
	i = 0
	while i < len(word)-1:
		if word[i] != word[i+1] and word[i+1:].count(word[i]) > 0:
			check = False
			i = len(word)-1
		i += 1
	if check:
		result += 1

print(result)

"""
!!! 좋은 코드 !!!
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)
"""