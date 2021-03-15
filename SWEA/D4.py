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
# from collections import deque
# T = int(input())
# dir = [[],[(-1,0),(1,0),(0,-1),(0,1)],[(-1,0),(1,0)],[(0,-1),(0,1)],[(-1,0),(0,1)],[(1,0),(0,1)],[(0,-1),(1,0)],[(0,-1),(-1,0)]]
# for tc in range(1, T+1):
#     N, M, R, C, L = map(int, input().split()) # 세로, 가로, 맨홀위치x, 맨홀위치y, 탈출 후 소요시간
#     hole = [list(map(int, input().split())) for _ in range(N)]
#     q = deque()
#     visited = [[0]*M for _ in range(N)]
#     q.appendleft((R,C))
#     visited[R][C] = 1
#     cnt = 0
#
#     while cnt != L-1:
#         cnt += 1
#         for _ in range(len(q)):
#             x, y = q.pop()
#             num = hole[x][y]
#             for d in dir[num]:
#                 nx, ny = x + d[0], y+d[1]
#                 if 0 <= nx < N and 0 <= ny < M:
#                     if (-d[0], -d[1]) in dir[hole[nx][ny]]:
#                         if visited[nx][ny] == 0 and hole[nx][ny] != 0:
#                             q.appendleft((nx, ny))
#                             visited[nx][ny] = 1
#
#         if cnt == L-1:
#             break
#
#     answer = 0
#
#     for v in visited:
#         answer += sum(v)
#
#     print(f'#{tc} {answer}')

# 탈주범 검거 _ 원재의 솔루션
# from collections import deque
# dir={1:[(1,0),(-1,0),(0,1),(0,-1)],
#      2:[(1,0),(-1,0)],
#      3:[(0,1),(0,-1)],
#      4:[(-1,0),(0,1)],
#      5:[(0,1),(1,0)],
#      6:[(1,0),(0,-1)],
#      7:[(-1,0),(0,-1)]}
#
# def connect(pipe1,pipe2):
#     r_pipe=(-pipe1[0],-pipe1[1])
#     if r_pipe in pipe2:
#         return True
#     return False
#
# def bfs(i,j,L):
#     ans=1
#     q=deque()
#     q.appendleft((i,j,tunnel[i][j]))  # (x,y,kind)
#     visited[i][j]=1
#     while q:
#         if L == 1:
#             break
#         L-=1
#         for _ in range(len(q)):
#             x,y,kind=q.pop()
#             for d in dir[kind]:
#                 nx,ny=x+d[0],y+d[1]
#                 if 0<= nx < N and 0<= ny < M:                          # map안에 존재
#                     if visited[nx][ny] == 0 and tunnel[nx][ny] !=0:    # 방문 x, 파이프가 있는 경우
#                         if connect(d,dir[tunnel[nx][ny]]):            # 다음 위치와 파이프가 연결 되는지
#                             visited[nx][ny]=1
#                             q.appendleft((nx,ny,tunnel[nx][ny]))
#                             ans+=1
#     return ans
#
# T=int(input())
# for tc in range(1,T+1):
#     N,M,R,C,L=map(int,input().split())
#     visited=[[0]*M for _ in range(N)]
#     tunnel=[]
#     for _ in range(N):
#         tunnel.append(list(map(int,input().split())))
#     print(f'#{tc} {bfs(R,C,L)}')

# 요리사
