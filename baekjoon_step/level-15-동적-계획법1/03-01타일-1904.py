## Title: 01타일
## Level: 15_03
## Number: 1904
## Date: 2022.01.23

# 놉
N = int(input())
tile_dict = {}

def tile(i, N):
	if i == N-1:
		return 1
	elif i == N-2:
		return 2
	elif (i, N) in tile_dict:
		return tile_dict[(i, N)]
	else:
		result = tile(i+1, N) + tile(i+2, N)
		tile_dict[(i, N)] = result
		return result

print(tile(0, N))


# 통과
N = int(input())

tile_lst = [0] * 1000000
tile_lst[0] = 1
tile_lst[1] = 2

for i in range(2, N):
    tile_lst[i] = (tile_lst[i-2]+tile_lst[i-1])%15746

print(tile_lst[N-1])