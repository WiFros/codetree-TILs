from collections import deque

MAX_L = 70

R, C, K = 0, 0, 0 # 행, 열, 골렘의 개수를 의미합니다
A = [[0] * MAX_L for _ in range(MAX_L + 3)] # 실제 숲을 [3~R+2][0~C-1]로 사용하기위해 행은 3만큼의 크기를 더 갖습니다
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
isExit = [[False] * MAX_L for _ in range(MAX_L + 3)] # 해당 칸이 골렘의 출구인지 저장합니다
answer = 0 # 각 정령들이 도달할 수 있는 최하단 행의 총합을 저장합니다

# (y, x)가 숲의 범위 안에 있는지 확인하는 함수입니다
def inRange(x, y):
    return 3 <= x < R + 3 and 0 <= y < C

# 숲에 있는 골렘들이 모두 빠져나갑니다
def resetMap():
    for i in range(R + 3):
        for j in range(C):
            A[i][j] = 0
            isExit[i][j] = False

# 골렘의 중심이 y, x에 위치할 수 있는지 확인합니다.
# 북쪽에서 남쪽으로 내려와야하므로 중심이 (y, x)에 위치할때의 범위와 (y-1, x)에 위치할떄의 범위 모두 확인합니다
def canGo(x, y):
    flag = 0 <= y - 1 and y + 1 < C and x + 1 < R + 3
    flag = flag and (A[x - 1][y - 1] == 0)
    flag = flag and (A[x - 1][y] == 0)
    flag = flag and (A[x - 1][y + 1] == 0)
    flag = flag and (A[x][y - 1] == 0)
    flag = flag and (A[x][y] == 0)
    flag = flag and (A[x][y + 1] == 0)
    flag = flag and (A[x + 1][y] == 0)
    return flag

# 정령이 움직일 수 있는 모든 범위를 확인하고 도달할 수 있는 최하단 행을 반환합니다
def bfs(x, y):
    result = x
    q = deque([(x, y)])
    visit = [[False] * C for _ in range(R + 3)]
    visit[x][y] = True
    while q:
        cur_x, cur_y = q.popleft()
        for k in range(4):
            nx, ny = cur_x + dx[k], cur_y + dy[k]
            # 정령의 움직임은 골렘 내부이거나
            # 골렘의 탈출구에 위치하고 있다면 다른 골렘으로 옮겨 갈 수 있습니다
            if inRange(nx, ny) and not visit[nx][ny] and (A[nx][ny] == A[cur_x][cur_y] or (A[nx][ny] != 0 and isExit[cur_x][cur_y])):
                q.append((nx, ny))
                visit[nx][ny] = True
                result = max(result, nx)
    return result

# 골렘id가 중심 (y, x), 출구의 방향이 d일때 규칙에 따라 움직임을 취하는 함수입니다
# 1. 남쪽으로 한 칸 내려갑니다.
# 2. (1)의 방법으로 이동할 수 없으면 서쪽 방향으로 회전하면서 내려갑니다.
# 3. (1)과 (2)의 방법으로 이동할 수 없으면 동쪽 방향으로 회전하면서 내려갑니다.
def down(x, y, d, id):
    if canGo(x + 1, y):
        # 아래로 내려갈 수 있는 경우입니다
        down(x + 1, y, d, id)
    elif canGo(x + 1, y - 1):
        # 왼쪽 아래로 내려갈 수 있는 경우입니다
        down(x + 1, y - 1, (d + 3) % 4, id)
    elif canGo(x + 1, y + 1):
        # 오른쪽 아래로 내려갈 수 있는 경우입니다
        down(x + 1, y + 1, (d + 1) % 4, id)
    else:
        # 1, 2, 3의 움직임을 모두 취할 수 없을떄 입니다.
        if not inRange(x-1, y-1) or not inRange(x+1, y+1):
            # 숲을 벗어나는 경우 모든 골렘이 숲을 빠져나갑니다
            resetMap()
        else:
            # 골렘이 숲 안에 정착합니다
            A[x][y] = id
            for k in range(4):
                A[x + dx[k]][y + dy[k]] = id
            # 골렘의 출구를 기록하고
            isExit[x + dx[d]][y + dy[d]] = True
            global answer
            # bfs를 통해 정령이 최대로 내려갈 수 있는 행를 계산하여 누적합니다
            answer += bfs(x, y) - 3 + 1

def main():
    global R, C, K
    R, C, K = map(int, input().split())
    for id in range(1, K + 1): # 골렘 번호 id
        x, d = map(int, input().split()) # 골렘의 출발 x좌표, 방향 d를 입력받습니다
        down(0, x - 1, d, id)
    print(answer)

if __name__ == "__main__":
    main()