# 물놀이를 가자
# from collections import deque
# T = int(input())
# dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
# for tc in range(1, T+1):
#     N, M  = map(int, input().split()) # 행개수, 열개수
#     arr = [input() for _ in range(N)]
#     q = deque()
#     visited = [[0]*M for _ in range(N)]
#
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 'W':
#                 q.append((i, j))
#
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx, ny = x + dir[k][0], y + dir[k][1]
#             if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[nx][ny] == 'L':
#                 q.append((nx, ny))
#                 visited[nx][ny] = visited[x][y] + 1
#
#     total = 0
#     for v in visited:
#         total += sum(v)
#
#     print(f'#{tc} {total}')

# 물놀이를 가자
# from collections import deque
# T = int(input())
# for tc in range(1, T+1):
#     N, M  = map(int, input().split()) # 행개수, 열개수
#     arr = [input() for _ in range(N)]
#     dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
#     q = deque()
#     visited = [[0]*M for _ in range(N)]
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 'W':
#                 q.append((i, j, cnt))
#                 visited[i][j] = 1
#
#     total = 0
#
#     while q:
#         i, j, cnt = q.popleft()
#         for k in range(4):
#             ni, nj = i + dir[k][0], j + dir[k][1]
#             if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 'L':
#                 q.append((ni, nj, cnt+1))
#                 total += cnt + 1
#                 visited[ni][nj] = 1
#
#     print(f'#{tc} {total}')

# 탈주범 검거
from collections import deque
T = int(input())
dir = [[],[(-1,0),(1,0),(0,-1),(0,1)],[(-1,0),(1,0)],[(0,-1),(0,1)],[(-1,0),(0,1)],[(1,0),(0,1)],[(0,-1),(1,0)],[(0,-1),(-1,0)]]
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split()) # 세로, 가로, 맨홀위치x, 맨홀위치y, 탈출 후 소요시간
    hole = [list(map(int, input().split())) for _ in range(N)]
    q = deque()
    visited = [[0]*M for _ in range(N)]
    q.appendleft((R,C))
    visited[R][C] = 1
    cnt = 0

    while cnt != L-1:
        cnt += 1
        for _ in range(len(q)):
            x, y = q.pop()
            num = hole[x][y]
            for d in dir[num]:
                nx, ny = x + d[0], y+d[1]
                if 0 <= nx < N and 0 <= ny < M:
                    for l in dir[hole[x][y]]:
                        if (-l[0], -l[1]) in dir[hole[nx][ny]]:
                            if visited[nx][ny] == 0 and hole[nx][ny] != 0:
                                q.appendleft((nx, ny))
                                visited[nx][ny] = 1

        if cnt == L-1:
            break

    answer = 0

    for v in visited:
        answer += sum(v)

    print(f'#{tc} {answer}')