OFF_SET = 100
n = int(input())
positions = {}

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = [val + OFF_SET for val in [x1, y1, x2, y2]]

    for x in range(x1, x2):
        for y in range(y1, y2):
            positions[(x,y)] = positions.get((x,y),0) + 1
print(len(positions))