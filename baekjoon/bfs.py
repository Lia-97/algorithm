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

# 14502번 (연구소)
from itertools import combinations
from collections import deque

N, M = map(int, input().split()) # 행 개수, 열 개수
arr = [] # 연구소 지도
check = [] # combinations 할 목록
for _ in range(N):
    arr.append(list(map(int, input().split())))
# 0 인 idx 추가하기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            check.append((i,j))

q = deque()
visited = [[0] * M for _ in range(N)]
dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우

max_safe = 0
for walls in combinations(check, 3):
    # 이전에 0 을 1 로 바꿔줬던 것들을 다시 0으로 바꿔줘야 할듯
    for wall in walls:
        arr[wall[0]][wall[1]] = 1
        print(arr)
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2:
                    q.appendleft((i,j))
                    visited[i][j] = 1
        while q:
            x, y = q.pop()
            for d in dir:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                        q.appendleft((nx, ny))
                        arr[nx][ny] = 1
                        visited[nx][ny] = 1
    # print(arr)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1

    if cnt > max_safe:
        max_safe = cnt

print(max_safe)


