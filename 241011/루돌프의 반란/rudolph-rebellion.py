def is_vaild(x,y,N):
    return 0<=x<N and 0<=y<N
def get_distance(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

# 상우하좌 / 11,1,7,5 방향
direction = [[-1,0],[0,1],[1,0],[0,-1],
            [-1,-1],[-1,1],[1,-1],[1,1]]

class Santa:
    power = 0
    is_stun = False
    priority = [0,1,2,3]

    def __init__(self,idx,x,y):
        self.idx = idx
        self.x = x
        self.y = y
    def add_force(self,target,power):


    def move(self, target):
        # 상 우 하 좌 순서의 이동 우선순위
        current_distance = get_distance(self.x, self.y, target.x, target.y)
        possible_direction = []

        for i in priority:
            nx = self.x + direction[i][0]
            ny = self.y + direction[i][1]
            
            # 유효한 좌표인지와 그리드가 비어있는지 확인
            if is_valid(nx, ny) and grid[nx][ny] == 0:
                distance = get_distance(nx, ny, target.x, target.y)
                if distance < current_distance:
                    possible_direction.append((distance, (nx, ny)))
        
        if possible_direction:
            # 거리가 가까운 순으로 정렬하고 가장 가까운 방향 선택
            possible_direction.sort(key=lambda x: x[0])
            return possible_direction[0][1]  # 가장 가까운 위치로 이동
        else:
            # 가까워질 수 없으면 현재 위치 유지
            return (self.x, self.y)

    def update(self):

    def find_target(self): # bfs
        



class Rudolph:
    power = 0
    target = {}# (좌표 : 인덱스)

    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self,target):
        if global grid[x][y] == 0 # 갈 수 있는 경우