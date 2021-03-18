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

