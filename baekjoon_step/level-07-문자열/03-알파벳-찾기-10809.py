## Title: 알파벳 찾
## Level: 7_03
## Number: 10809
## Date: 2021.04.12

word = input()

for i in range(26):
	print(word.find(chr(i+97)), end=' ')