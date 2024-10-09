"""
왼쪽으로 뒤집으면 흰색, 오른쪽은 검은색

아무타일 : 0번째에서 시작, n번의 명령

흰색과 검은색의 타일 수
"""

n = int(input())
sections = {}
current = 0

for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)
    if direction == 'R': #1 -> 검은색 
        while distance > 0:
            sections[current] = sections.get(current,0)
            sections[current] = 1
            distance -= 1
            if distance > 0:
                current += 1
    else: # -1 -> 흰색
        while distance > 0:
            sections[current] = sections.get(current,0)
            sections[current] = -1
            distance -= 1
            if distance > 0:
                current -= 1

white, black = 0,0
for color in sections.values():
    if color == 1:
        black += 1
    else:
        white += 1

print(white, black)