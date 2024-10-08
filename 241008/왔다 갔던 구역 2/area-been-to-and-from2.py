OFFSET = 1000
MAX_R = 2000

n = int(input())
visited = []

current = 0

for _ in range(n):
    distance, direction = tuple(input().split())
    distance = int(distance)

    if direction == 'L':
        left_section = current - distance
        right_section = current
        current -= distance
    else:
        left_section = current
        right_section = current + distance
        current += distance
    
    visited.append([left_section,right_section])

checked = [0] * (MAX_R + 1)

for x1, x2 in visited:
    x1,x2 = x1 + OFFSET, x2 + OFFSET

    for i in range(x1,x2):
        checked[i] += 1
count = 0
for element in checked:
    if element >= 2:
        count += 1

print(count)