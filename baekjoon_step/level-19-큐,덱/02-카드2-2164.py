## Title: 카드2
## Number: 2164
## Date: 2021.09.22

from collections import deque

N = int(input())
deq = deque(range(1, N+1))

while len(deq) > 1:
	deq.popleft()
	deq.rotate(-1)

print(deq.pop())