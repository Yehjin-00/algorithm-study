## Title: N Queen
## Level: 14_05
## Number: 9663
## Date: 2021.06.02


## deep copy를 이용한 풀이

import copy
def check(line, where, chess):
	for i in range(len(chess)):
		for j in range(len(chess)):
			if i == line or j == where or i+j==line+where or i-j==line-where:
				chess[i][j] = -1

def queen(line, l_max, chess, result):   
	if line==l_max:
		if 1 in chess[line]:
			result.append(1)
	else:
		for i in range(len(chess)):
			if chess[line][i] > 0:               
				c = copy.deepcopy(chess)
				check(line, i, c)              
				queen(line+1, l_max, c, result)

n = int(input())

chess = [[1 for i in range(n)] for i in range(n)]
result = []
queen(0, n-1, chess, result)
print(sum(result))


## 원 상태로 돌리기 위한 방안 2 (back function 구현)

def back(chess, threshold):
	for i in range(len(chess)):
		for j in range(len(chess)):
			if chess[i][j] == -threshold:
				chess[i][j] = 1

def check(line, where, chess, num):
	for i in range(len(chess)):
		for j in range(len(chess)):
			if (i == line or j == where or i+j==line+where or i-j==line-where) and chess[i][j]==1:
				chess[i][j] = -num
            

def queen(line, l_max, chess, result):  
	if line==l_max:
		if 1 in chess[line]:
			result.append(chess)
	elif 1 in chess[line]:
		for i in range(len(chess)):
			check_num = l_max * line
			if chess[line][i] > 0:               
				check(line, i, chess, check_num)              
				queen(line+1, l_max, chess, result)
				back(chess, check_num)

n = int(input())
chess = [[1 for i in range(n)] for i in range(n)]
result = []
queen(0, n-1, chess, result)
print(sum(result))


## 구조 자체를 바꾼 시도

def check(x, y, chess):
    for a, b in chess:
        if x == a or b == y or a+b == x+y or a-b == x-y:
            return False
    return True

def queen(line, N, chess, result):
    for i in range(N):
        if check(line, i, chess):
            chess.append([line, i])
            if line==N-1:
                result.append(1)
            else:
                queen(line+1, N, chess, result)
            chess.pop()

n = int(input())
chess = []
result = []
queen(0, n, chess, result)
print(sum(result))


