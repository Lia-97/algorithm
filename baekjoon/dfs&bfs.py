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