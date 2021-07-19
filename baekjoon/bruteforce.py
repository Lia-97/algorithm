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

# 7568번 (덩치) _ 실패
# import sys
# N = int(sys.stdin.readline())
# points = [0]*N
# weights = []
# heights = []
# for i in range(N):
#     weight, height = map(int, sys.stdin.readline().split())
#     weights.append((i, weight))
#     heights.append((i, height))
# weights.sort(key=lambda x:-x[1])
# heights.sort(key=lambda x:-x[1])
# for i in range(N):
#     points[weights[i][0]] += i
#     points[heights[i][0]] += i
#     print(weights)
#     print(heights)
#     print(points)
# ranks = list(enumerate(points))
# ranks.sort(key=lambda x:x[1])
# curr_rank = 1
# next_rank = 2
# result = [0]*N
# result[ranks[0][0]] = 1
# for n in range(1, N):
#     if ranks[n][1] != ranks[n-1][1]:
#         curr_rank = next_rank
#     next_rank += 1
#     result[ranks[n][0]] = curr_rank
#
# print(*result)

# 7568번 (덩치) _ 위에랑 뭐가 다른지 모르겠음
# N = int(input())
# info = []
# result = []
# for _ in range(N):
#     W, H = map(int, input().split())
#     info.append((W, H))
# for i in range(N):
#     count = 0
#     for j in range(N):
#         if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
#             count += 1
#     result.append(count+1)
# print(*result)

