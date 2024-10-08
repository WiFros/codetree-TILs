n = int(input())
cnt_b = {}
cnt_w = {}
positions = set()
last_color = {}
cur = 0

for _ in range(n):
    x_str, c = input().split()
    x = int(x_str)

    if c == 'L':
        while x > 0:
            positions.add(cur)
            cnt_w[cur] = cnt_w.get(cur, 0) + 1
            last_color[cur] = 1  # 1은 흰색을 나타냅니다.
            x -=1
            if x > 0:
                cur -=1
    else:
        while x > 0:
            positions.add(cur)
            cnt_b[cur] = cnt_b.get(cur, 0) + 1
            last_color[cur] = 2  # 2는 검은색을 나타냅니다.
            x -=1
            if x > 0:
                cur +=1

w, b, g = 0, 0, 0

for pos in positions:
    bw = cnt_b.get(pos, 0)
    ww = cnt_w.get(pos, 0)
    if bw >= 2 and ww >= 2:
        g += 1
    elif last_color[pos] == 1:
        w += 1
    elif last_color[pos] == 2:
        b += 1

print(w, b, g)