# 11724번 (연결 요소의 개수)
# from collections import defaultdict
# import sys
# sys.setrecursionlimit(10000)
#
# def dfs(node):
#     visited[node] = 1
#     for i in graph[node]:
#         if visited[i] == 0:
#             dfs(i)
#
# N, M = map(int, sys.stdin.readline().split()) # 정점 개수, 간선 개수
# graph = defaultdict(list)
# visited = [0] * (N+1)
# for _ in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# cnt = 0
# for j in range(1,N+1):
#     if visited[j] == 0:
#         dfs(j)
#         cnt += 1
# print(cnt)

# 4963번 (섬의 개수)
# import sys
# sys.setrecursionlimit(10000)
#
# def dfs(x, y):
#     visited[x][y] = 1
#     for d in dir:
#         nx, ny = x + d[0], y + d[1]
#         if 0 <= nx < h and 0 <= ny < w:
#             if MAP[nx][ny] == 1 and visited[nx][ny] == 0:
#                 dfs(nx, ny)
# while True:
#     w, h = map(int, sys.stdin.readline().split()) # 열 개수, 행 개수
#     if w == 0 and h == 0:
#         break
#     MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
#     visited = [[0]*w for _ in range(h)]
#     dir = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,1),(1,-1)] # 상하좌우,대각선
#     cnt = 0 # 섬의 개수
#
#     for i in range(h):
#         for j in range(w):
#             if MAP[i][j] == 1 and visited[i][j] == 0:
#                 dfs(i,j)
#                 cnt += 1 # dfs가 호출될때마다 cnt에 1을 더함
#
#     print(cnt)

# 2468번 (안전 영역) _ 첫번째 제출 코드
# import sys
# sys.setrecursionlimit(100000)
#
# def dfs(a, b):
#     visited[a][b] = 1
#     for d in dir:
#         na, nb = a + d[0], b + d[1]
#         if 0 <= na < N and 0 <= nb < N:
#             if land_copy[na][nb] != 0 and visited[na][nb] == 0:
#                 dfs(na, nb)
#
# N = int(sys.stdin.readline())
# land = []
# max_v = 0
# dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
# for _ in range(N):
#     lis = list(map(int, sys.stdin.readline().split()))
#     land.append(lis)
#     if max(lis) > max_v:
#         max_v = max(lis)
#
# max_cnt = 0
# for i in range(0, max_v):
#     # 루프 돌때마다 침수 영역 표시할 land 초기화
#     land_copy = []
#     for value in land:
#         land_copy.append(value[::])
#     # visited 도 루프 돌때마다 초기화
#     visited = [[0]*N for _ in range(N)]
#     cnt = 0
#
#     # 강수량에 따라 잠기는 지역을 0으로 바꿔준다.
#     for m in range(N):
#         for n in range(N):
#             if land_copy[m][n] <= i:
#                 land_copy[m][n] = 0 # 높이의 조건이 1 이상이기 때문에
#
#     # 안전 영역 개수 세기(0이 아닌 구역의 개수를 센다)
#     for x in range(N):
#         for y in range(N):
#             if land_copy[x][y] != 0 and visited[x][y] == 0:
#                 dfs(x,y)
#                 cnt += 1
#
#     if cnt > max_cnt:
#         max_cnt = cnt
#
# print(max_cnt)

# 2468번 (안전 영역) _ 메모리 줄이기 (벡터연산)
import sys
sys.setrecursionlimit(100000)

def dfs(x, y, z):
    land[x][y] = z
    for d in dir:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < N:
            if land[nx][ny] > z:
                dfs(nx,ny,z)

N = int(sys.stdin.readline())
land = []
max_v = 0
dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
for _ in range(N):
    lis = list(map(int, sys.stdin.readline().split()))
    land.append(lis)
    if max(lis) > max_v:
        max_v = max(lis)

ans = 0
for k in range(max_v-1, -1, -1):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if land[i][j] > k:
                cnt += 1
                dfs(i, j, k)
    if cnt > ans:
        ans = cnt

print(ans)

# 2468번 (안전 영역) _ 메모리 줄이기 (손코딩)
import sys
sys.setrecursionlimit(100000)

def dfs(x, y, z):
    land[x][y] = z
    if land[x-1][y] > z:
        dfs(x-1, y, z)
    if land[x+1][y] > z:
        dfs(x+1,y,z)
    if land[x][y-1] > z:
        dfs(x, y-1,z)
    if land[x][y+1] > z:
        dfs(x, y+1,z)


N = int(sys.stdin.readline())
land = [[0]*(N+2)]
max_v = 0

for _ in range(N):
    lis = [0]+list(map(int, sys.stdin.readline().split()))+[0]
    land.append(lis)
    if max(lis) > max_v:
        max_v = max(lis)
land.append([0]*(N+2))

ans = 0
for k in range(max_v-1, -1, -1):
    cnt = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if land[i][j] > k:
                cnt += 1
                dfs(i, j, k)
    if cnt > ans:
        ans = cnt

print(ans)