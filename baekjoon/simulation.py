# 1100번 (하얀 칸)
# arr = [] # 0흰, 1검
# for i in range(8):
#     if i%2:
#         arr.append([1,0,1,0,1,0,1,0])
#     else:
#         arr.append([0,1,0,1,0,1,0,1])
#
# chess = [list(input()) for _ in range(8)]
# cnt = 0
#
# for i in range(8):
#     for j in range(8):
#         if arr[i][j] == 0 and chess[i][j] == 'F':
#             cnt += 1
# print(cnt)

# 1966번 (프린터 큐)
# from collections import deque
# T = int(input()) # 테스트케이스 수
# for tc in range(T):
#     N, M = map(int, input().split()) # 문서 개수, 문서 위치
#     papers = list(map(int,input().split())) # 문서의 중요도
#     q = deque()
#     cnt = 0
#     for i, paper in enumerate(papers):
#         q.append((paper,i))
#
#     while True:
#         max_v = max(q)[0]
#         num, idx = q.popleft()
#         if num == max_v and idx == M:
#             cnt += 1
#             break
#         elif num == max_v and idx != M:
#             cnt += 1
#         else:
#             q.append((num,idx))
#
#     print(cnt)

# 1966번 (프린터 큐) _ 시간 줄여보기
# from collections import deque
# T = int(input()) # 테스트케이스 수
# for tc in range(T):
#     N, M = map(int, input().split()) # 문서 개수, 문서 위치
#     papers = list(map(int,input().split())) # 문서의 중요도
#     q = deque()
#     cnt = 0
#     for i, paper in enumerate(papers):
#         q.append((paper,i))
#
#     max_list = sorted(papers)
#
#     while True:
#         num, idx = q.popleft()
#         if num == max_list[-1] and idx == M:
#             cnt += 1
#             break
#         elif num == max_list[-1] and idx != M:
#             cnt += 1
#             max_list.pop()
#         else:
#             q.append((num,idx))
#     print(cnt)

# 14503번 (로봇 청소기) _ 미완
# N, M = map(int, input().split()) # 행 개수, 열 개수
# r, c, d = map(int, input().split()) # x좌표, y좌표, 방향
# clean = [list(map(int,input().split())) for _ in range(N)]
# stack = []
# visited = [[0]*M for _ in range(N)]
# dir = [(-1,0),(0,1),(1,0),(0,-1)] # d의 방향(0부터 순서대로)
# stack.append((r,c,d))
# visited[r][c] = 1
#
# while True:
#     x, y, d = stack.pop()
#     nx, ny = x+dir[d][0], y+dir[d][1]
#     if 0 <= nx < N and 0 <= ny < M:
#         if clean[nx][ny] == 0:
#             stack.append((nx, ny))
#             visited[nx][ny] = 1
#         else:
#             if d == 0:
#                 d = 3
#             else:
#                 d = d-1

# 10172번 (개)
# dog = '''|\_/|
# |q p|   /}
# ( 0 )"""\\
# |"^"`    |
# ||_/=\\\\__|
# '''
#
# print(dog)

# 5567번 (결혼식)
# from collections import defaultdict, deque
#
# def bfs(q):
#     invite = 0
#     while q:
#         current_node, step = q.popleft()
#         if step == 2:
#             return invite
#         for next_node in graph[current_node]:
#             if used[next_node] == 0:
#                 used[next_node] = 1
#                 invite += 1
#                 q.append((next_node, step+1))
#     return invite
#
#
# n = int(input()) # 친구의 수
# m = int(input()) # 리스트의 길이
# graph = defaultdict(list)
# for _ in range(m):
#     node1, node2 = map(int, input().split())
#     graph[node1].append(node2)
#     graph[node2].append(node1)
# q = deque()
# used = [0]*(n+1)
# q.append((1, 0)) # 상근이의 노드번호, 몇단계 연결인지
# used[1] = 1
# print(bfs(q))

# 10818번 (최소, 최대)
# import sys
# N = sys.stdin.readline()
# nums = list(map(int, sys.stdin.readline().split()))
# answer = [min(nums), max(nums)]
#
# print(*answer)


# import sys
# N = int(sys.stdin.readline())
# nums = list(map(int, sys.stdin.readline().split()))
# nums.sort()
# answer = [nums[0], nums[N-1]]
#
# print(*answer)


