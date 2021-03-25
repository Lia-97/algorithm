# 2606번 (바이러스)
# def dfs(node):
#     global cnt
#     visited[node] = 1
#     cnt += 1
#     for next_node in computers[node]:
#         if visited[next_node] != 1:
#             dfs(next_node)
#
# from collections import defaultdict
# N = int(input()) # 컴퓨터의 수
# com = int(input()) # 연결되어 있는 컴퓨터 쌍의 수
# computers = defaultdict(list)
# for c in range(com):
#     a, b = map(int, input().split())
#     computers[a].append(b)
#     computers[b].append(a)
# visited = [0] * (N+1)
# visited[0] = 1
# cnt = 0
# dfs(1)
#
# print(cnt-1)

# 2667번 (단지번호 붙이기)
# def dfs(i, j):
#     global num
#     num += 1
#     visited[i][j] = 1
#     for d in dir:
#         ni, nj = i + d[0], j + d[1]
#         if 0 <= ni < N and 0 <= nj < N:
#             if visited[ni][nj] == 0 and arr[ni][nj] == '1':
#                 dfs(ni, nj)
#
# N = int(input())
# arr = [list(input()) for _ in range(N)]
# cnt = 0 # 총 단지수
# nums = [] # 단지 내 집의 수
# dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# visited = [[0] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == '1' and visited[i][j] == 0:
#             num = 0
#             cnt += 1
#             dfs(i, j)
#             nums.append(num)
#
# nums.sort() # 오름차순으로 정렬
#
# print(cnt)
# for i in nums:
#     print(i)

# 1012번 (유기농 배추)
# import sys
# sys.setrecursionlimit(100000)
#
# def dfs(x, y):
#     visited[x][y] = 1
#     for k in range(4):
#         nx, ny = x + dir[k][0], y + dir[k][1]
#         if 0 <= nx < N and 0 <= ny < M:
#             if arr[nx][ny] == 1 and visited[nx][ny] == 0:
#                 dfs(nx, ny)
#
# T = int(input())
# for _ in range(T):
#     M, N, K = map(int, input().split()) # 가로, 세로, 배추위치
#     arr = [[0]*M for _ in range(N)]
#     for _ in range(K):
#         X, Y = map(int, input().split())
#         i, j = Y, X
#         arr[i][j] = 1
#
#     visited = [[0]*M for _ in range(N)]
#     dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
#
#     cnt = 0
#
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 1 and visited[i][j] == 0:
#                 dfs(i,j)
#                 cnt += 1
#     print(cnt)

# 7576번 (토마토)
# from collections import deque
# M, N = map(int, input().split()) # 열개수, 행개수
# tomato = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
#
# dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
# q = deque()
# cnt = 0
#
# for i in range(N):
#     for j in range(M):
#         if tomato[i][j] == 1:
#             q.append((i,j))
#             visited[i][j] = 1
#
# while q:
#     cnt += 1
#     for _ in range(len(q)):
#         x, y = q.popleft()
#         for k in range(4):
#             nx, ny = x + dir[k][0], y + dir[k][1]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if tomato[nx][ny] == 0 and visited[nx][ny] == 0:
#                     tomato[nx][ny] = 1
#                     visited[nx][ny] = 1
#                     q.append((nx, ny))
# ans = -1
#
# def answer():
#     global ans
#     for i in range(len(tomato)):
#         for j in tomato[i]:
#             if tomato[i][j] == 0:
#                 return
#     ans = cnt-1
#
# answer()
#
# print(ans)

# 1697번 (숨바꼭질)
# from collections import deque
#
# N, K = map(int, input().split())  # 수빈 위치, 동생 위치
# q = deque()
# q.append((N, 0))
# visited = [0]*100001
#
# while True:
#     node, time = q.popleft()
#     dir = [node*2, node-1, node+1]
#     if node != K:
#         for d in dir:
#             if 0 <= d <= 100000 and visited[d] == 0:
#                 q.append((d, time+1))
#                 visited[d] = 1
#         time += 1
#     else:
#         ans = time
#         break
#
# print(ans)

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
# import sys
# sys.setrecursionlimit(100000)
#
# def dfs(x, y, z):
#     land[x][y] = z
#     for d in dir:
#         nx, ny = x + d[0], y + d[1]
#         if 0 <= nx < N and 0 <= ny < N:
#             if land[nx][ny] > z:
#                 dfs(nx,ny,z)
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
# ans = 0
# for k in range(max_v-1, -1, -1):
#     cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if land[i][j] > k:
#                 cnt += 1
#                 dfs(i, j, k)
#     if cnt > ans:
#         ans = cnt
#
# print(ans)

# 2468번 (안전 영역) _ 메모리 줄이기 (손코딩)
# import sys
# sys.setrecursionlimit(100000)
#
# def dfs(x, y, z):
#     land[x][y] = z
#     if land[x-1][y] > z:
#         dfs(x-1, y, z)
#     if land[x+1][y] > z:
#         dfs(x+1,y,z)
#     if land[x][y-1] > z:
#         dfs(x, y-1,z)
#     if land[x][y+1] > z:
#         dfs(x, y+1,z)
#
#
# N = int(sys.stdin.readline())
# land = [[0]*(N+2)]
# max_v = 0
#
# for _ in range(N):
#     lis = [0]+list(map(int, sys.stdin.readline().split()))+[0]
#     land.append(lis)
#     if max(lis) > max_v:
#         max_v = max(lis)
# land.append([0]*(N+2))
#
# ans = 0
# for k in range(max_v-1, -1, -1):
#     cnt = 0
#     for i in range(1,N+1):
#         for j in range(1,N+1):
#             if land[i][j] > k:
#                 cnt += 1
#                 dfs(i, j, k)
#     if cnt > ans:
#         ans = cnt
#
# print(ans)

# 2178번 (미로 탐색)
# from collections import deque
# N, M = map(int, input().split()) # 행개수, 열개수
# arr = [input() for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
# visited[0][0] = 1
# dir = [(-1,0),(1,0),(0,-1),(0,1)]
# q = deque()
# q.append((0,0,1))
# answer = 0
#
# while q:
#     x, y, cnt = q.pop()
#     if x == N-1 and y == M-1:
#         answer = cnt
#         break
#     for d in dir:
#         nx, ny = x + d[0], y + d[1]
#         if 0 <= nx < N and 0 <= ny < M:
#             if arr[nx][ny] == '1' and visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 q.appendleft((nx,ny,cnt+1))
# print(answer)

# 14502번 (연구소) _ 미완
# from itertools import combinations
# from collections import deque
#
# N, M = map(int, input().split()) # 행 개수, 열 개수
# arr = [] # 연구소 지도
# check = [] # combinations 할 목록
# for _ in range(N):
#     arr.append(list(map(int, input().split())))
# # 0 인 idx 추가하기
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             check.append((i,j))
#
# q = deque()
# dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
#
# max_safe = 0
# for walls in combinations(check, 3):
#     copy_arr = []
#     visited = [[0] * M for _ in range(N)]
#     for a in arr:
#         copy_arr.append(a[::])
#     for wall in walls:
#         copy_arr[wall[0]][wall[1]] = 1
#         for i in range(N):
#             for j in range(M):
#                 if copy_arr[i][j] == 2:
#                     q.appendleft((i,j))
#                     visited[i][j] = 1
#         while q:
#             x, y = q.pop()
#             for d in dir:
#                 nx, ny = x + d[0], y + d[1]
#                 if 0 <= nx < N and 0 <= ny < M:
#                     if arr[nx][ny] == 0 and visited[nx][ny] == 0:
#                         q.appendleft((nx, ny))
#                         copy_arr[nx][ny] = 1
#                         visited[nx][ny] = 1
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 0:
#                 cnt += 1
#
#     if cnt > max_safe:
#         max_safe = cnt
#
# print(max_safe)

# 2583번 (영역 구하기) _ dfs
# import sys
# sys.setrecursionlimit(10000)
#
# def dfs(x, y):
#     global sub
#     visited[x][y] = 1
#     for d in dir:
#         nx, ny = x + d[0], y + d[1]
#         if 0 <= nx < M and 0 <= ny < N:
#             if paper[nx][ny] == 0 and visited[nx][ny] == 0:
#                 sub += 1
#                 dfs(nx, ny)
#     return sub
#
# M, N, K = map(int, input().split()) # 행 개수, 열 개수, 사각형의 개수
# paper = [[0]*N for _ in range(M)] # 빈 모눈종이
# visited = [[0]*N for _ in range(M)]
# dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
# cnt = 0
# size = []
#
# for _ in range(K):
#     x1, y1, x2, y2 = map(int, input().split())
#     for x in range(y1, y2):
#         for y in range(x1, x2):
#             paper[x][y] = 1
#
# for i in range(M):
#     for j in range(N):
#         if paper[i][j] == 0 and visited[i][j] == 0:
#             sub = 1
#             size.append(dfs(i,j))
#             cnt += 1
#
# size.sort()
# size = list(map(str, size))
# ans = ' '.join(size)
# print(cnt)
# print(ans)

# 2583번 (영역 구하기) _ bfs
# from collections import deque
#
# def bfs(x,y):
#     global sub
#     q = deque()
#     q.appendleft((x,y))
#     visited[x][y] = 1
#
#     while q:
#         x, y = q.pop()
#         for d in dir:
#             nx, ny = x + d[0], y + d[1]
#             if 0 <= nx < M and 0 <= ny < N:
#                 if paper[nx][ny] == 0 and visited[nx][ny] == 0:
#                     sub += 1
#                     visited[nx][ny] = 1
#                     q.appendleft((nx, ny))
#
#     return sub
#
# M, N, K = map(int, input().split()) # 행 개수, 열 개수, 사각형의 개수
# paper = [[0]*N for _ in range(M)] # 빈 모눈종이
# visited = [[0]*N for _ in range(M)]
# dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
# cnt = 0
# size = []
# for _ in range(K):
#     x1, y1, x2, y2 = map(int, input().split())
#     for x in range(y1, y2):
#         for y in range(x1, x2):
#             paper[x][y] = 1
#
# for i in range(M):
#     for j in range(N):
#         if paper[i][j] == 0 and visited[i][j] == 0:
#             sub = 1
#             size.append(bfs(i,j))
#             cnt += 1
#
# size.sort()
# size = list(map(str, size))
# ans = ' '.join(size)
# print(cnt)
# print(ans)

# 1987번 (알파벳)
# R, C = map(int, input().split()) # 행개수, 열개수
# board = [input() for _ in range(R)]
# q = set([(0,0,board[0][0])])
# dir = [(-1,0),(1,0),(0,-1),(0,1)]
# answer = 1
#
# while q:
#     x, y, alpha = q.pop()
#     answer = max(answer, len(alpha))
#     for d in dir:
#         nx, ny = x + d[0], y +d[1]
#         if 0 <= nx < R and 0 <= ny < C:
#             if board[nx][ny] not in alpha:
#                 q.add((nx, ny, alpha+board[nx][ny]))
#
# print(answer)

