n = int(input())
visited = {}  # 좌표에 대한 방문 횟수
current = 0

for _ in range(n):
    # 명령어를 받아와서 분리
    distance, inst = input().split()
    distance = int(distance)
    
    if inst == 'R':  # 오른쪽 이동
        for _ in range(distance):
            current += 1
            visited[current] = visited.get(current, 0) + 1
    elif inst == 'L':  # 왼쪽 이동
        for _ in range(distance):
            current -= 1
            visited[current] = visited.get(current, 0) + 1

# 2번 이상 방문한 좌표 개수를 세기
count = sum(1 for v in visited.values() if v >= 2)
print(count)