"""
아무 타일이나 시작해서 n번의 명령에 걸쳐 움직임. 
명령은 x L , x R 형태로 주어짐. 타일 치우기 
타일 색은 덧칠해지면 마지막으로 칠해진 색으로 바뀐다. 타일하나가 흰색과 검은색으로 칠해지면(각 2번씩 이상 w > 2 이고, b > 2 ) 회색으로 바뀜. 흰,검,회 타일 수 출력 

"""

n = int(input())
current = 0 # 현재 위치
section = {} # 범위 : [색 리스트] 형태의 딕셔터리

for _ in range(n):
    distance, direction = tuple(input().split())
    distance = int(distance)

    if direction == 'R': # 검은색
        for i in range(current, current + distance):
            section.setdefault(i,[]).append('b')
        current += distance
    else: # 흰색으로 칠하기
        for i in range(current - distance, current):
            section.setdefault(i,[]).append('w')
        current -= distance

white, black, glay = 0,0,0

for tile, colors in section.items():
    while_block = colors.count('w')
    black_block = colors.count('b')
    
    if while_block >= 2 and black_block >= 2 : 
        glay += 1
    elif colors[-1] == 'w':
        white += 1
    elif colors[-1] == 'b':
        black += 1

print(white, black, glay)