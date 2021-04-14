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

# 보급로 _ 다익스트라로 풀기
# import heapq
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     roads = [list(map(int, input())) for _ in range(N)]
#     times = [[float('inf')]*N for _ in range(N)]
#     times[0][0] = 0
#     dir = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우
#     queue = []
#     heapq.heappush(queue, (0, 0, times[0][0])) # x좌표, y좌표, 복구에 걸리는 시간
#
#     while queue:
#         x, y, time = heapq.heappop(queue)
#         if times[x][y] < time:
#             continue
#
#         for d in dir:
#             nx, ny = x + d[0], y + d[1]
#             setting = time
#             if 0 <= nx < N and 0 <= ny < N:
#                 setting += roads[nx][ny]
#
#                 if setting < times[nx][ny]:
#                     times[nx][ny] = setting
#                     heapq.heappush(queue, (nx, ny, setting))
#
#     print(f'#{tc} {times[N-1][N-1]}')

# 보급로 _ dfs로 풀기 (실행시간 빠른 코드 참고)
# from collections import deque
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# def dfs(x, y):
#     q = deque()
#     q.append((x, y))
#     d[x][y] = 0
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx, ny = x + dx[k], y + dy[k]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if d[nx][ny] == -1:
#                     d[nx][ny] = d[x][y] + a[nx][ny]
#                     q.append((nx, ny))
#                 else:
#                     if d[nx][ny] > d[x][y] + a[nx][ny]:
#                         d[nx][ny] = d[x][y] + a[nx][ny]
#                         q.append((nx, ny))
#                     else:
#                         continue
#
# for t in range(int(input())):
#     n = int(input())
#     a = [list(map(int, list(input()))) for _ in range(n)]
#     d = [[-1] * (n) for _ in range(n)]
#     dfs(0, 0)
#     print('#{} {}'.format(t + 1, d[n - 1][n - 1]))

# Ladder1 _ ???
# from collections import deque
# for tc in range(1, 11):
#     num = input()
#     x = 0
#     y = 0 # 2의 위치
#     visited = [[0]*102 for _ in range(102)]
#
#     # 0을 테두리로 가진 이차원 배열 만들기
#     ladder = [[0]*102]
#     for i in range(100):
#         lad = list(map(int, input().split()))
#         ladder.append([0]+lad+[0])
#         ladder.append([0]*102)
#         # 2의 위치 찾기
#         if 2 in lad:
#             x = i+1
#             y = lad.index(2)
#
#     q = deque()
#     q.append((x,y))
#
#     while q:
#         x, y = q.popleft()
#
#         if x == 1:
#             break
#
#         if ladder[x][y-1] == 1 and visited[x][y-1] == 0:
#             nx, ny = x, y-1
#         elif ladder[x][y+1] == 1 and visited[x][y+1] == 0:
#             nx, ny = x, y+1
#         else:
#             nx, ny = x-1, y
#
#         visited[nx][ny] = 1
#         q.append((nx, ny))
#
#     print(y-1)

# 괄호 짝짓기
# table = {'(':1, ')':-1, '<':2, '>':-2, '[':3, ']':-3, '{':4, '}':-4}
# for tc in range(1, 11):
#     all = int(input())
#     bracket = list(input())
#     stack = []
#     stack.append(bracket.pop())
#     while bracket:
#         last = bracket.pop()
#         if len(stack) == 0 and table[last]>0:
#             break
#         elif len(stack) == 0 and table[last]<0:
#             stack.append(last)
#         else:
#             if table[last]+table[stack[-1]] == 0:
#                 stack.pop()
#             else:
#                 stack.append(last)
#
#     if stack:
#         ans = 0
#     else:
#         ans = 1
#     print(f'#{tc} {ans}')

# 길찾기
# from collections import deque
#
# def bfs(q):
#     global ans
#     while q:
#         node = q.popleft()
#         if node == 99:
#             ans = 1
#             break
#         if road1[node] != 0:
#             q.append(road1[node])
#         if road2[node] != 0:
#             q.append(road2[node])
#
#
# for tc in range(1, 11):
#     tc, N = map(int, input().split()) # 테케 번호, 길의 총 개수
#     road1 = [0]*100
#     road2 = [0]*100
#     pairs = list(map(int, input().split())) # 순서쌍
#     ans = 0
#     for i in range(N):
#         idx = pairs[2*i]
#         val = pairs[2*i+1]
#         if road1[idx] == 0:
#             road1[idx] = val
#         else:
#             road2[idx] = val
#     q = deque()
#     q.append(1)
#     bfs(q)
#
#     print(f'#{tc} {ans}')

# 미로2
# from collections import deque
#
# def bfs(q):
#     global ans
#
#     while q:
#         x, y = q.popleft()
#         for d in dir:
#             nx, ny = x+d[0], y+d[1]
#             if 0 <= nx < 100 and 0 <= ny <100:
#                 if maze[nx][ny] != '1' and visited[nx][ny] == 0:
#                     if maze[nx][ny] == '3':
#                         ans = 1
#                         return
#                     visited[nx][ny] = 1
#                     q.append((nx, ny))
#
#
# for tc in range(1, 11):
#     input()
#     maze = [input() for _ in range(100)]
#     visited = [[0] * 100 for _ in range(100)]
#     dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
#     start = (0,0)
#     ans = '0'
#     for i in range(100):
#         for j in range(100):
#             if maze[i][j] == '2':
#                 start = (i, j)
#                 visited[i][j] = 1
#                 break
#
#     q = deque()
#     q.append(start)
#     bfs(q)
#     print(f'#{tc} {ans}')



