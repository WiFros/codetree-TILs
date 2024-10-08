"""
길이가 N인 1차원 배열
Ai ~ Bi 영역에 값을 1씩 증가시키는 명령이 K 번 주어진다. 
쌓인 블럭의 수 중 최댓값을 출력하는 프로그램
"""

N, K = map(int, input().split(' '))
block = [0 for _ in range(N)]
answer = 0

for i in range(K):
    A, B = map(int, input().split(' '))
    block[A-1:B] = [x + 1 for x in block[A-1:B]]


print(max(block))