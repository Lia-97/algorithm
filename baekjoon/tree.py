# 1991번 (트리 순회)
# def preorder(idx):
#     global pre_ans
#     pre_ans += chr(idx+64)
#     if left[idx] != 0:
#         preorder(left[idx])
#     if right[idx] != 0:
#         preorder(right[idx])
#
# def inorder(idx):
#     global in_ans
#     if left[idx] != 0:
#         inorder(left[idx])
#     in_ans += chr(idx + 64)
#     if right[idx] != 0:
#         inorder(right[idx])
#
# def postorder(idx):
#     global post_ans
#     if left[idx] != 0:
#         postorder(left[idx])
#     if right[idx] != 0:
#         postorder(right[idx])
#     post_ans += chr(idx + 64)
#
# N = int(input()) # 노드의 개수
# left, right = [0]*(N+1), [0]*(N+1)
# for _ in range(N):
#     alpha = input().split()
#     pa = ord(alpha[0]) - 64
#     if alpha[1] != '.':
#         ch1 = ord(alpha[1]) - 64
#         left[pa] = ch1
#     if alpha[2] != '.':
#         ch2 = ord(alpha[2]) - 64
#         right[pa] = ch2
#
# pre_ans = ''
# in_ans = ''
# post_ans = ''
#
# preorder(1)
# inorder(1)
# postorder(1)
#
# print(pre_ans)
# print(in_ans)
# print(post_ans)

# 2263번 (트리의 순회)
# n = int(input())
# inorder = list(map(int, input().split()))
# postorder = list(map(int, input().split()))
# tree = [0]*(n+1)
#
# while True:
#     pass

# 11725번 (트리의 부모 찾기) _ dfs 실패
# from collections import defaultdict
# import sys
# sys.setrecursionlimit(1000000)
#
# def dfs(node, parent):
#     ans.append((node, parent))
#     for i in tree[node]:
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(i, node)
#
# T = int(sys.stdin.readline())
# tree = defaultdict(list)
# visited = [0]*(T+1)
# ans = []
# for _ in range(T-1):
#     node1, node2 = map(int, sys.stdin.readline().split()) # 연결된 두 정점
#     tree[node1].append(node2)
#     tree[node2].append(node1)
#
# visited[1] = 1
# dfs(1, 0)
# ans.sort(key=lambda x:x[0])
# for a in ans[1:]:
#     print(a[1])

# 11725번 (트리의 부모 찾기)
# from collections import defaultdict, deque
# import sys
#
# def bfs(q):
#     global answer
#     while q:
#         node, parent = q.popleft()
#         answer.append((node, parent))
#         for i in tree[node]:
#             if visited[i] == 0:
#                 visited[i] = 1
#                 q.append((i, node))
#
# T = int(sys.stdin.readline())
# tree = defaultdict(list)
# visited = [0]*(T+1)
# ans = []
# q = deque()
# answer = []
# for _ in range(T-1):
#     node1, node2 = map(int, sys.stdin.readline().split()) # 연결된 두 정점
#     tree[node1].append(node2)
#     tree[node2].append(node1)
#
# q.append((1, 0))
# visited[1] = 1
# bfs(q)
# answer.sort(key=lambda x:x[0])
# for a in answer[1:]:
#     print(a[1])

# 9372번 (상근이의 여행)
# import sys
# T = int(sys.stdin.readline())
# for _ in range(T):
#     N, M = map(int, sys.stdin.readline().split()) # 국가 수, 비행기 종류
#     for _ in range(M):
#         a, b = map(int, sys.stdin.readline().split())
#     print(N-1)

# 1753번 (최단경로)
# import sys
# import heapq
#
# def f(q):
#     while q:
#         current_weight, current_node = heapq.heappop(q)
#
#         if current_weight > weight[current_node]:
#             continue
#
#         for idx in graph[current_node]:
#             next_node = idx[1]
#             cost = current_weight + idx[0]
#             if cost < weight[next_node]:
#                 weight[next_node] = cost
#                 heapq.heappush(q, (cost, next_node))
#
# INF = float('inf')
# V, E = map(int, sys.stdin.readline().split()) # 정점, 간선
# K = int(sys.stdin.readline()) # 출발지
# graph = [[] for _ in range(V+1)]
# for _ in range(E):
#     u, v, w = map(int, sys.stdin.readline().split())
#     graph[u].append((w, v))
# weight = [INF]*(V+1)
# weight[K] = 0
# q = []
# heapq.heappush(q, (0, K))
# f(q)
#
# for w in weight[1:]:
#     if w == INF:
#         print('INF')
#     else:
#         print(w)

