# 방향: 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [ 0, 1, 0,-1]

N, M, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
units = {}
init_k = [0]*(M+1)
final_k = [0]*(M+1)

for m in range(1, M+1):
    si, sj, h, w, k = map(int, input().split())
    units[m] = [si-1, sj-1, h, w, k]
    init_k[m] = k
    final_k[m] = k  # 초기 체력 저장

def push_unit(start, dr):
    q = []
    pset = set()
    damage = [0] * (M+1)
    intended_positions = {}

    q.append(start)
    pset.add(start)

    while q:
        cur = q.pop(0)
        ci, cj, h, w, k = units[cur]
        ni, nj = ci + di[dr], cj + dj[dr]

        # 범위 체크
        if not (0 <= ni <= N - h and 0 <= nj <= N - w):
            return  # 이동 취소

        # 이동할 위치에 벽(2) 또는 함정(1)이 있는지 확인
        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if arr[i][j] == 2:
                    return  # 이동 취소
                if arr[i][j] == 1:
                    damage[cur] += 1

        intended_positions[cur] = (ni, nj)

        # 다른 유닛과 겹치는지 확인
        for idx in units:
            if idx in pset:
                continue
            ti, tj, th, tw, tk = units[idx]
            if ni <= ti + th - 1 and ni + h -1 >= ti and nj <= tj + tw -1 and nj + w -1 >= tj:
                q.append(idx)
                pset.add(idx)

    # 명령받은 기사는 데미지 없음
    damage[start] = 0

    # 유닛 이동 및 데미지 처리
    for idx in pset:
        si, sj, h, w, k = units[idx]
        if k <= damage[idx]:
            units.pop(idx)
            final_k[idx] = 0
        else:
            ni, nj = intended_positions[idx]
            units[idx] = [ni, nj, h, w, k - damage[idx]]
            final_k[idx] = k - damage[idx]

for _ in range(Q):
    idx, dr = map(int, input().split())
    if idx in units:
        push_unit(idx, dr)

ans = 0
for idx in range(1, M+1):
    ans += init_k[idx] - final_k[idx]
print(ans-1)