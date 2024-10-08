n = int(input())
visited = {}  # 좌표에 대한 방문 횟수
current = 0

for _ in range(n):
    # 명령어를 받아와서 분리
    distance, inst = input().split()
    distance = int(distance)
    
    if inst == 'R':  # 오른쪽 이동
        for i in range(1, distance + 1):
            visited[current + i] = visited.get(current + i, 0) + 1
        current += distance
    elif inst == 'L':  # 왼쪽 이동
        for i in range(1, distance + 1):
            visited[current - i] = visited.get(current - i, 0) + 1
        current -= distance

# 2번 이상 방문한 좌표 개수를 세기
count = sum(1 for v in visited.values() if v >= 2)
print(count)