# 11724번 (연결 요소의 개수)
# from collections import defaultdict
# import sys
# sys.setrecursionlimit(10000)
#
# def dfs(node):
#     visited[node] = 1
#     for i in graph[node]:
#         if visited[i] == 0:
#             dfs(i)
#
# N, M = map(int, sys.stdin.readline().split()) # 정점 개수, 간선 개수
# graph = defaultdict(list)
# visited = [0] * (N+1)
# for _ in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# cnt = 0
# for j in range(1,N+1):
#     if visited[j] == 0:
#         dfs(j)
#         cnt += 1
# print(cnt)