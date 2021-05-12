## Title: N Queen
## Level: 14_05
## Number: 9663
## Date: 2021.05.12


def check(line, where, chess):
	for i in range(len(chess)):
		for j in range(len(chess)):
			if i == line or j == where or i+j==line+where or i-j==line-where:
				chess[i][j] = -1	

def queen(line, l_max, chess, result):
	if line==l_max:
		if 1 in chess[line]:
			result += 1
	else:
		for i in range(len(chess)):
			if chess[line][i] > 0:
				c = chess.copy()
				check(line, i, c)
				queen(line+1, l_max, c, result)

n = int(input())

# 1 안전, -1 위험
chess = [[1 for i in range(n)] for i in range(n)]
result = 0
queen(0, n-1, chess, result)
print(result)




### 이거 테스트중

def check(line, where, chess):
	for i in range(len(chess)):
		for j in range(len(chess)):
			if i == line or j == where or i+j==line+where or i-j==line-where:
				chess[i][j] = -1

def queen(line, l_max, chess, result):
	display('line', line)    
	if line==l_max:
		display('if')
		display(chess)
		if 1 in chess[line]:
			result.append(1)
	else:
		for i in range(len(chess)):
			display('else', i)
			display(chess)
			if chess[line][i] > 0:
				c = chess.copy()
				check(line, i, c)
				queen(line+1, l_max, c, result)

n = int(input())

# 1 안전, -1 위험
chess = [[1 for i in range(n)] for i in range(n)]
result = []
queen(0, n-1, chess, result)
print(sum(result))