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