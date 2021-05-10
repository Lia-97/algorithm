# 2798번 (블랙잭) _ 부분집합으로 풀었더니 시간초과 뜸
# import sys
# N, M = map(int,sys.stdin.readline().rstrip().split())
# lis = list(map(int,sys.stdin.readline().rsplit()))
# card = []
# for i in range(1 << N):
#     sub = []
#     for j in range(N):
#         if i & (1<<j):
#             sub.append(lis[j])
#     if len(sub) == 3:
#         card.append(sub)
#
# max_sum = 0
# for c in card:
#     if sum(c) <= M and sum(c) > max_sum:
#        max_sum = sum(c)
#
# print(max_sum)

# 2798번 (블랙잭)
# N, M = map(int, input().split())
# lis = list(map(int, input().split()))
# max_sum = 0
# for i in range(N):
#     for j in range(i+1, N):
#         for l in range(j+1, N):
#             if lis[i]+lis[j]+lis[l] <= M and lis[i]+lis[j]+lis[l] > max_sum:
#                 max_sum = lis[i]+lis[j]+lis[l]
# print(max_sum)

# 2589번 (보물섬) _ 문제를 잘못 이해함
# from collections import deque
# import sys
#
# def bfs(q):
#     cnt = 0
#     while q:
#         x, y = q.popleft()
#         print(x,y)
#         for d in dir:
#             nx, ny = x+d[0], y+d[1]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if gift[nx][ny] == 'L' and visited[nx][ny] == 0:
#                     visited[nx][ny] = 1
#                     cnt += 1
#                     q.append((nx, ny))
#     return cnt
#
# N, M = list(map(int, sys.stdin.readline().split())) # 세로, 가로
# gift = [sys.stdin.readline() for _ in range(N)]
# q = deque()
# dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
# visited = [[0]*M for _ in range(N)] # 방문여부
# min = float('inf')
# for i in range(N):
#     for j in range(M):
#         if gift[i][j] == 'L' and visited[i][j] == 0:
#             visited[i][j] = 1
#             q.append((i, j))
#             ans = bfs(q)
#             if ans < min:
#                 min = ans
# print(min)

# 2589번 (보물섬)
lis=[5,2,7,4]
lis.pop(1)
print(lis)