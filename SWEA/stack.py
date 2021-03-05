# 파스칼의 삼각형
# T= int(input())
# for tc in range(1, T+1):
#     # 첫번째 줄과 두번째 줄은 주어져 있음
#     pascal = [[1], [1, 1]]
#     N = int(input())
#     for i in range(2, N):
#         # pascal 에 append 할 arr 리스트를 생성한다. arr 리스트의 첫번째 원소는 1.
#         arr= [1]
#         for j in range(i-1):
#             # 구하고자 하는 원소(리스트)의 하나 전 리스트의 원소들의 합이 새로 추가하는 리스트의 원소가 된다.
#             arr.append(pascal[i-1][j] + pascal[i-1][j+1])
#         arr.append(1) # arr 리스트의 마지막 원소도 1.
#         pascal.append(arr) # pascal 리스트에 arr 을 더한다.
#
#     # N 이 1이면 pascal 의 첫번째 원소만 출력할 수 있게 조정해준다.
#     if N == 1:
#         pascal = pascal[:N]
#
#     print('#{}'.format(tc))
#     for p in pascal:
#         p = map(str, p)
#         p = ' '.join(p)
#         print(p)

# 부분집합 재귀로 풀어보기 _ 원재한테 물어보기
# def recur(n, k):
#     if n == k:
#         print(bit) # 전체 부분집합 출력
#         for i in range(k):
#             if bit[i]:
#                 print(A[i], end = ' ')
#         print()
#         return
#     else:
#         bit[n] = 0
#         recur(n+1, k)
#         bit[n] = 1
#         recur(n+1, k)
#
# A = [10, 20, 30]
# N = len(A)
# bit = [0] * N
# recur(0, N) # 0번 원소부터 복사, 원소의 수 N개

# 음료수 얼려 먹기 _ 미완
# N, M = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(N)]
# print(arr)
#
# def ice(x, y):
#     if x < 0 or x >= M or y < 0 or y >= N:
#         return False
#     if arr[x][y] == 0:
#         pass

# 반복문자 지우기
# T = int(input())
# for tc in range(1, T+1):
#     lis = list(map(str, input()))
#     stack = [-1] # 인덱스 에러를 방지하기 위해 임의의 원소 -1 넣어줌.
#
#     # lis 의 길이가 0이 아닌동안
#     while len(lis)!= 0:
#         # lis 의 가장 마지막 값이 stack 의 가장 마지막 값과 같은지 비교햔다.
#         last = lis.pop()
#         # 같으면 stack 에서도 해당 값을 빼주고
#         if last == stack[-1]:
#             stack.pop()
#         # 다르면 더해준다.
#         else:
#             stack.append(last)
#
#     # stack 생성 시, 임의로 넣었던 값 -1 은 제외해 줘야 하므로 len(stack)-1
#     ans = len(stack)-1
#     print('#{} {}'.format(tc, ans))

# 괄호검사
# T = int(input())
# for tc in range(1, T+1):
#     lis = list(map(str, input()))
#     # 각 괄호에 해당하는 숫자를 지정한다. 짝이 되는 괄호의 합이 0 이 되도록.
#     dic = {'(': 1, ')': -1, '{': 2, '}': -2, '*': 0}
#     # 맨 처음 들어올 값과 비교하기 위해 임의의 값을 넣어놓는다.
#     stack = ['*']
#     while len(lis) > 0:
#         last = lis.pop()
#         # lis 의 마지막 원소가 괄호 4종에 해당한다면
#         if last in ['(',')','{','}']:
#             # 딕셔너리에서 해당 괄호의 숫자를 가져와서 stack 의 원소가 해당하는 숫자와 합이 0인지 확인한다.
#             if dic.get(stack[-1]) + dic.get(last) == 0:
#                 # 합이 0이면 짝을 이룬다는 뜻이므로 stack 에서 pop
#                 stack.pop()
#             # 합이 0이 되지 않는다면 append
#             else:
#                 stack.append(last)
#     # 모든 괄호가 짝을 이루었다면 stack 에서 전부 pop 되었을테니까, stack 의 길이는 초기값의 길이인 1이 되어야 함.
#     if len(stack) == 1:
#         ans = 1
#     else:
#         ans = 0
#
#     print('#{} {}'.format(tc,ans))

# 종이 붙이기_???????
# def Paper(N):
#     dp = []
#     N = N // 10
#     dp.append(1)
#     dp.append(3)
#     for i in range(2, N):
#         # (i-1) 왼쪽 끝이 2 x 1 막대, (i-2) 왼쪽 끝이 2 x 2 막대(가로로 2x1 2개 또는 2x2 1개 이므로 * 2)
#         dp.append(dp[i - 1] + dp[i - 2] * 2)
#     return dp[-1]
#
#
# T = int(input())
# for test in range(1, T + 1):
#     N = int(input())
#     print(f'#{test}', Paper(N))

# 그래프 경로
# def f(s, g, v): # s에서 g에 도착할 수 있는지 확인하는 함수
#     # 중복없이 빠짐없이 탐색하는 dfs
#     stack = [] # stack 생성
#     visited = [0]*(v+1) # visited 생성
#     stack.append(s) # push(s) 갈림길 목록에 시작점 추가
#     visited[s] = 1 # visited[s] <= 1 방문예약 표시(중복된 push 방지)
#     while stack: # 스택이 비어있지 않으면(방문할 곳이 남아있으면)
#         n = stack.pop() # 방문할 목록에서 마지막에 기록된 노드를 꺼내
#         if n == g: # 방문할 노드가 목적지 g인지 확인
#             return 1 # 경로가 존재하기 때문
#         for i in range(1, V+1): # 모든 노드에 대해, 현재노드에서 방문할 수 있는 곳인지 검토
#             if adj[n][i] == 1 and visited[i] == 0: # 인접하고 미방문인 노드 i 를 찾으면
#                 stack.append(i) # push(i)
#                 visited[i] = 1
#
#     return 0 # 목적지에 도달하지 못하고, 탐색할 노드가 더 이상 없는 경우
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     adj = [[0] * (V+1) for _ in range(V+1)] # 인접행렬 생성, 초기화
#     for _ in range(E):
#         n1, n2 = map(int, input().split())
#         adj[n1][n2] = 1 # 연결되어있으면 1로 바꿔줌
#         # adj[n2][n1] = 1 # 방향성이 없기 때문
#     S, G = map(int, input().split()) # 출발점, 목적지
#     print('#{} {}'.format(tc, f(S, G, V)))

# 길 찾기 _ 시간 초과 뜸
# def find():
#     stack = []
#     visited = [0]*100
#     stack.append(1)
#     visited[1] = 1
#     while stack:
#         n = stack.pop()
#         if n == 99:
#             return 1
#         for i in range(0, 100):
#             if arr[n][i] == 1 and visited[i] == 0:
#                 stack.append(i)
#                 visited[i] = 1
#     return 0
#
# for tc in range(11):
#     tc, N = map(int, input().split())
#     node = list(map(int, input().split()))
#     arr = [[0] * 100 for _ in range(100)]
#
#     for i in range(N):
#         arr[node[i * 2]][node[i * 2 + 1]] = 1
#
#
#     print('#{} {}'.format(tc, find()))

# 길 찾기 _ 런타임 에러를 없애보자.
# def dfs(node):
#     global ans
#     if node == 99:
#         ans = 1
#         return
#     else:
#         visited[node] = 1
#         if node in arr:
#             for i in arr[node]:
#                 if visited[i] != 1:
#                     dfs(i)
#     return
#
# for tc in range(11):
#     tc, N = map(int, input().split())
#     arr = {}
#     nums = list(map(int, input().split()))
#     visited = [0] * 100
#     ans = 0
#     for i in range(N):
#         if nums[i*2] in arr:
#             arr[nums[i * 2]].append(nums[(i*2)+1])
#         else:
#             arr[nums[i * 2]] = [nums[(i*2)+1]]
#     dfs(0)
#     print(f'#{tc} {ans}')

# 길찾기 _ 스택으로 풀어보기
# for tc in range(11):
#     tc, N = map(int, input().split())
#     arr = {}
#     nums = list(map(int, input().split()))
#     visited = [0] * 100
#     ans = 0
#     for i in range(N):
#         if nums[i*2] in arr:
#             arr[nums[i * 2]].append(nums[(i*2)+1])
#         else:
#             arr[nums[i * 2]] = [nums[(i*2)+1]]
#     print(f'#{tc} {ans}')

# 그래프 경로 _ 혼자서 풀어보기
# def graph(s, g, v):
#     stack = []
#     visited = [0] * (v+1)
#     stack.append(s)
#     visited[s] = 1
#     while stack:
#         l = stack.pop()
#         if l == g:
#             return 1
#         for i in range(1, v+1):
#             if arr[l][i] == 1 and visited[i] == 0:
#                 stack.append(i)
#                 visited[i] = 1
#     return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     v, e = map(int, input().split())
#     arr = [[0]*(v+1) for _ in range(v+1)]
#
#     for _ in range(e):
#         n, m = map(int, input().split())
#         arr[n][m] = 1
#
#     s, g = map(int, input().split())
#
#     ans = graph(s, g, v)
#
#     print('#{} {}'.format(tc, ans))

# 재귀로 부분집합 풀기
# def recur(n, k):
#     if n == k:
#         print(bit) # 전체 부분집합 출력
#         for i in range(k):
#             if bit[i]:
#                 print(A[i], end = ' ')
#         print()
#         return
#     else:
#         bit[n] = 0
#         recur(n+1, k)
#         bit[n] = 1
#         recur(n+1, k)
#
# A = [10, 20, 30]
# N = len(A)
# bit = [0] * N
# recur(0, N) # 0번 원소부터 복사, 원소의 수 N개

# 백트래킹으로 부분집합 풀기
# N = 3
# arr = [1, 2, 3]  # 우리가 활용할 데이터
# sel = [0] * N  # arr의 각 자리의 해당 원소를 뽑았는지 체크하는 리스트(부분집합을 의미함)
#
# def powerset(idx):
#     if idx == N:
#         print(sel, ':', end='')
#         for i in range(N):
#             if sel[i]:
#                 print(arr[i], end='')
#         print()
#
#         return
#
#     # idx 자리의 원소를 뽑고 간다.
#     sel[idx] = 1
#     powerset(idx + 1)
#     # idx 자리를 안뽑고 간다.
#     sel[idx] = 0
#     powerset(idx + 1)
#
# powerset(0)

# 연습문제1
# lis = list(map(str, input()))
# stack = []
# result = []
# while lis:
#     for l in lis:
#         if l in ['+', '-', '*', '/']:
#             stack.append(lis.pop())
#         else:
#             result.append(lis.pop())
# while result:
#     a = result.pop()
#     lis.append(a)
#
# lis.extend(stack)
#
# lis = ' '.join(lis)
#
# print(lis)

# 연습문제1 - 두번째 방법
# lis = list(map(str, input()))
# stack = []
# result = []
# while lis:
#     for l in lis:
#         if l in ['+', '-', '*', '/']:
#             stack.append(lis.pop())
#         else:
#             result.append(lis.pop())
#
# result = result[::-1]
# result.extend(stack)
#
# result = ' '.join(result)
# print(result)

# 연습문제1 - 세번째 방법
# lis = list(map(str, input()))
# stack = []
# ans = []
# for l in lis:
#     if l in ['+', '-', '*', '/']:
#         stack.append(l)
#     else:
#         ans.append(l)
# while stack:
#     ans.append(stack.pop())
# ans = ' '.join(ans)
# print(ans)

# powerset 재귀
# N = 3
# arr = [1, 2, 3]  # 우리가 활용할 데이터
# sel = [0] * N  # arr의 각 자리의 해당 원소를 뽑았는지 체크하는 리스트(부분집합을 의미함)
#
# def powerset(idx):
#     if idx == N:
#         print(sel, ':', end='')
#         for i in range(N):
#             if sel[i]:
#                 print(arr[i], end='')
#         print()
#
#         return
#
#     # idx 자리의 원소를 뽑고 간다.
#     sel[idx] = 1
#     powerset(idx + 1)
#     # idx 자리를 안뽑고 간다.
#     sel[idx] = 0
#     powerset(idx + 1)
#
# powerset(0)

# 그래프 경로 (재귀로 풀기)
# def dfs(node):
#     global ans
#     visited[node]=1
#     if node == G:
#         ans = 1
#         return
#
#     for next_node in graph[node]:
#         if visited[next_node] ==0:
#             dfs(next_node)
#         if ans == 1:
#             return
#
# from collections import defaultdict
# T=int(input())
# for tc in range(1,T+1):
#     graph=defaultdict(list)
#     V,E=map(int,input().split())
#     visited=[0]*(V+1)
#     ans=0
#
#     for _ in range(E):
#         a,b=map(int,input().split())
#         graph[a].append(b)
#     S,G=map(int,input().split())
#     dfs(S)
#
#     print(f'#{tc} {ans}')

# Forth
# def check(a, b, i):
#     if i == '+':
#         return b + a
#     elif i == '-':
#         return b - a
#     elif i == '*':
#         return b* a
#     elif i == '/':
#         return b //a
#
# def forth(lis):
#     global ans
#     operator = ['+', '-', '*', '/']
#     stack = []
#     for l in lis:
#         if l not in operator and l != '.':
#             stack.append(int(l))
#         elif l in operator:
#             if len(stack) > 1:
#                 stack.append(check(stack.pop(), stack.pop(), l))
#             else:
#                 ans = 'error'
#                 return
#         elif l == '.':
#             if len(stack) != 1:
#                 ans = 'error'
#                 return
#             else:
#                 ans = stack.pop()
#                 return
#
# T = int(input())
# for tc in range(1, T+1):
#     lis = input().split()
#     ans = 0
#     forth(lis)
#     print(f'#{tc} {ans}')

# 미로
# def dfs(x, y):
#     global ans
#     if arr[x][y] == 3:
#         ans = 1
#         return
#     arr[x][y] = 1
#     for i in range(4):
#         nx = x + dir[i][0]
#         ny = y + dir[i][1]
#         if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1:
#             dfs(nx, ny)
#
#     return
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     stack = []
#     ans = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:
#                 dfs(i,j)
#     print('#{} {}'.format(tc, ans))

# 배열 최소 합
# def dfs(idx, sub):
#     global min_sum
#     if idx == N:
#         if sub <= min_sum:
#             min_sum = sub
#             return
#
#     if sub >= min_sum:
#         return
#
#     for i in range(N):
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(idx+1, sub + arr[idx][i])
#             visited[i] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [0] * N
#     min_sum = float('inf')
#     dfs(0,0)
#     print(f'#{tc} {min_sum}')

# 토너먼트 카드게임 _ 버려
# def rsp(A,B):
#     # (번호, 가위,바위,보)
#     if A[1] > B[1]:
#         A,B=B,A
#     # 비기면
#     if A[1] == B[1]:
#         return A if A[0] < B[0] else B
#     elif A[1] < B[1]:
#         #  A가 가위, B가 보로 커진건 B가 진것
#         if A[1] == 1 and B[1] == 3:
#             return A
#         return B
#
# def check(N, cards):
#     global ans
#     lis = []
#     if N < 1:
#         return
#     if N%2:
#         for i in range(N//2):
#             lis.append(rsp(cards[i*2], cards[i*2 + 1]))
#         lis.append(cards[-1])
#         if len(lis) == 1:
#             ans = lis.pop()[0]
#             return
#         check(N//2 + 1, lis)
#     else:
#         for i in range(N//2):
#             lis.append(rsp(cards[i*2], cards[i*2 + 1]))
#         if len(lis) == 1:
#             ans = lis.pop()[0]
#             return
#         check(N//2, lis)
#     return
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cards = list(map(int, input().split()))
#     cards = list(enumerate(cards, start=1))
#     ans = 0
#     check(N, cards)
#     print(f'#{tc} {ans}')
#
# # lis = [1, 1, 3, 4]
# # lis = list(enumerate(lis))
# #
# # print(lis[0][1] == lis[1][1])
# # print(type(lis[0][1]))

# queue
# Q_SIZE = 10
# q = [0] * Q_SIZE
# front = -1
# rear = -1
#
# rear += 1
# q[rear] = 10
# rear += 1
# q[rear] = 20
# rear += 1
# q[rear] = 30
# while front != rear:
#     front += 1
#     tmp = q[front]
#     print(tmp)

# queue
# from queue import Queue
#
# q = Queue()
# q.put(10)
# q.put(20)
# q.put(30)
# while not q.empty():
#     print(q.get())

# 연습문제2 _ 마이쮸
# N = 20 # 마이쮸의 개수
#
# queue = [(1,0)] # 초기화
# # (0,0) [0] : 사람 번호, [1] : 직전까지 받았던 마이쮸의 개수
#
# new_people = 1
# last_people = 0
#
# while N > 0:
#     num, cnt = queue.pop(0)
#
#     last_people = num # 마지막으로 받으러 온 사람
#     cnt += 1 # 저번 보다 하나 더 챙기기
#
#     N -= cnt # num 이라는 친구가 cnt 개수만큼 가져감
#     new_people += 1
#
#     queue.append((num, cnt)) # 맨 뒤로 가서 다시 줄을 섬
#     queue.append((new_people, 0)) # 새로운 사람도 줄섬
# print(last_people)

# bfs 연습문제3 (교재)
# # 7 8
# # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
#
# # 리스트 사용
# def bfs(s, V):           # 너비우선 탐색
#     q = []               # 큐 생성
#     visited = [0]*(V+1)  # visited 생성
#     q.append(s)          # 시작점 인큐
#     visited[s] = 1       # 시작점 처리 표시
#     while q:             # 대기중인 번호가 있으면
#         n = q.pop(0)     # 빠른 순으로 꺼내서
#         print(n)         # do(n)
#         for i in range(1, V+1):  # 바로 뒤에 연결된 번호가 있으면 (인접 노드 중 표시안된 노드 i가 있으면)
#             if adj[n][i] and visited[i] == 0:  # 아직 대기중이 아니면
#                 q.append(i)
#                 visited[i] = 1
#
# # 행렬 사용
# def bfs2(s, V):           # 너비우선 탐색
#     q = []               # 큐 생성
#     visited = [0]*(V+1)  # visited 생성
#     q.append(s)          # 시작점 인큐
#     visited[s] = 1       # 시작점 처리 표시
#     while q:             # 대기중인 번호가 있으면
#         n = q.pop(0)     # 빠른 순으로 꺼내서
#         print(n)         # do(n)
#         for i in adjlist[n]:  # 바로 뒤에 연결된 번호가 있으면 (인접 노드 중 표시안된 노드 i가 있으면)
#             if visited[i] == 0:  # 아직 대기중이 아니면
#                 q.append(i)
#                 visited[i] = 1
#
# V, E = map(int, input().split())
# edge = list(map(int, input().split()))
#
# adj = [[0]*(V+1) for _ in range(V+1)] # 인접행렬
# for i in range(E):
#     adj[edge[i*2]][edge[i*2+1]] = 1
#     adj[edge[i*2+1]][edge[i*2]] = 1 # 무향 그래프
#
# adjlist = [[] for _ in range(V+1)] # 인접리스트인 경우
# for i in range(0, E*2, 2):
#     adjlist[edge[i]].append(edge[i+1])
#     adjlist[edge[i+1]].append(edge[i]) # 무향 그래프
#
# bfs(1, V)

# 암호생성기
# for tc in range(1, 11):
#     tc = int(input())
#     nums = list(map(int, (input().split())))
#     while nums[-1] > 0:
#         for i in range(1, 6):
#             pw = nums.pop(0)
#             if pw - i > 0:
#                 nums.append(pw-i)
#             else:
#                 nums.append(0)
#                 break
#     nums = ' '.join(map(str, nums))
#     print('#{} {}'.format(tc, nums))

# 미로의 거리
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     maze = [input() for _ in range(N)]
#     visited = [[0]*N for _ in range(N)] # 방문여부 확인. 방문했으면 1로 바꿀 예정
#     dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 이동 방향 (상, 하, 좌, 우)
#     q = [] # 큐 생성
#     ans = 0
#
#     # 시작노드와 도착 노드를 구한다.
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == '2':
#                 q.append((i,j,0)) # 시작노드를 q에 더하고
#                 visited[i][j] = 1 # 해당 노드의 visited 도 1로 바꿔준다.
#             if maze[i][j] == '3':
#                 end = (i, j)
#
#     while q:
#         x, y, move = q.pop(0)
#
#         # 도착하면 움직인 거리 move 에 1 을 빼서 ans에 저장한다.
#         if x == end[0] and y == end[1]:
#             ans = move - 1
#             break
#
#         # 위에서 pop 한 maze[x][y] 가 갈 수 있는 칸을 찾는다.
#         for k in range(4):
#             nx = x + dir[k][0]
#             ny = y + dir[k][1]
#             # 상하좌우 중에 이동 가능한 칸을 q 에 더하고, 방문 처리한다.
#             if 0 <= nx < N and 0 <= ny < N:
#                 if maze[nx][ny] != '1' and visited[nx][ny] == 0:
#                     q.append((nx, ny, move+1))
#                     visited[nx][ny] = 1
#
#     print(f'#{tc} {ans}')

# 회전
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     nums = list(input().split())
#     while M > 0:
#         first = nums.pop(0)
#         nums.append(first)
#         M -= 1
#
#     print(f'#{tc} {nums[0]}')

# 노드의 거리
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     graph = {}
#     # 방향이 없는 그래프를 만든다.
#     for _ in range(E):
#         start, end = map(int, input().split())
#         if start in graph:
#             graph[start].append(end)
#             if end in graph:
#                 graph[end].append(start)
#             else:
#                 graph[end] = [start]
#         else:
#             graph[start] = [end]
#             graph[end] = [start]
#
#     S, G = map(int, input().split()) # 출발, 도착
#
#     visited = [0] * (V+1) # 방문 여부 체크
#     q = []
#     q.append((S, 0)) # 시작하는 노드를 일단 q에 넣는다.
#     visited[S] = 1 # 시작하는 노드 방문 처리
#     ans = 0
#
#     flag = False
#     while q:
#         node, move = q.pop(0)
#         if node in graph:
#             for i in graph[node]:
#                 if i == G:
#                     ans = move + 1
#                     flag = True
#                     break
#                 if visited[i] == 0:
#                     q.append((i, move+1))
#                     visited[i] = 1
#             if flag: break
#     print(f'#{tc} {ans}')

# 피자 굽기 _ 미완
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # 화덕 크기, 피자 개수
#     cheese = list(map(int, input().split()))
#     q = []
#     ans = 0
#     for i in range(N):
#         q.append(cheese[i])
#     cheese = cheese[N:]
#     cheese = cheese[::-1]
#
#     while cheese:
#         while q:
#             print(q)
#             check = q.pop(0)
#             if check <= 1:
#                 print('지금')
#                 break
#             else:
#                 if check//2 > 0:
#                     q.append(check//2)
#                     print(q)
#                     if len(q) == 1:
#                         ans = q.pop()
#
#         q.append(cheese.pop())
#
#     print(ans)

# 미로1
# for tc in range(1, 11):
#     tc = int(input())
#     maze = [input() for _ in range(16)]
#     visited = [[0] * 16 for _ in range(16)]
#     q = []
#     dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     ans = 0
#     for i in range(16):
#         for j in range(16):
#             if maze[i][j] == '2':
#                 start = (i, j)
#                 visited[i][j] = 1
#                 q.append((i, j))
#
#     while q:
#         i, j = q.pop(0)
#         if maze[i][j] == '3':
#             ans = 1
#
#         for k in range(4):
#             ni, nj = i + dir[k][0], j + dir[k][1]
#             if 0 <= ni < 16 and 0 <= nj < 16:
#                 if maze[ni][nj] != '1' and visited[ni][nj] == 0:
#                     q.append((ni, nj))
#                     visited[ni][nj] = 1
#
#     print(f'#{tc} {ans}')

# 러시아 국기 같은 깃발
# from itertools import combinations
# T=int(input())
# for tc in range(1,T+1):
#     N,M=map(int,input().split())
#     flag=[]
#     ans=2500
#     # 각 행에 해당 색으로 칠할 때 비용계산
#     for _ in range(N):
#         W,B,R=0,0,0
#         for s in input():
#             if s == 'W':
#                 W+=1
#             elif s == 'B':
#                 B+=1
#             else:
#                 R+=1
#         flag.append({'W':M-W,'B':M-B,'R':M-R})
#
#     # 모든 경우의 수 check
#     for start,end in combinations(range(1,N),2):
#         result=0
#         # W, B, R 순서로 채워지는 것이므로
#         for i in range(N):
#             if i < start:
#                 result += flag[i]['W']
#             elif  i >= end:
#                 result += flag[i]['R']
#             else:
#                 result += flag[i]['B']
#         ans=min(ans,result)
#
#     print(f'#{tc} {ans}')

# 햄버거 다이어트
T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    burger = [list(map(int, input().split())) for _ in range(N)]
    part = []

    for i in range(1 << N):
        sub = []
        for j in range(N):
            if i & (1 << j):
                sub.append(burger[j])
        sub_sum = 0
        for s in sub:
            sub_sum += s[1]
        if sub_sum <= L:
            part.append(sub)

    ans = 0

    for sub_part in part:
        taste = 0
        for sub in sub_part:
            taste += sub[0]
        if taste > ans:
            ans = taste

    print(f'#{tc} {taste}')
