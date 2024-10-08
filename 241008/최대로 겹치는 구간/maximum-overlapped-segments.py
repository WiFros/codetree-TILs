n = int(input())  # 선분의 개수
events = []

# 선분의 시작점과 끝점을 이벤트로 저장
for _ in range(n):
    x1, x2 = map(int, input().split())
    events.append((x1, 'start'))
    events.append((x2, 'end'))

# 이벤트를 정렬 (위치가 같을 경우 'end'가 먼저 오도록 처리)
events.sort(key=lambda x: (x[0], x[1] == 'start'))

# 선분이 겹치는 최대 개수를 찾는 변수
current_overlapping = 0
max_overlapping = 0

# 이벤트를 순회하면서 겹치는 선분 개수를 추적
for event in events:
    if event[1] == 'start':
        current_overlapping += 1
        max_overlapping = max(max_overlapping, current_overlapping)
    else:
        current_overlapping -= 1

print(max_overlapping)