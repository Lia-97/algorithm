# 여행경로
# def solution(tickets):
#     airport = {}
#
#     for ticket in tickets:
#         if ticket[0] in airport:
#             airport[ticket[0]].append(ticket[1])
#
#         else:
#             airport[ticket[0]] = [ticket[1]]
#
#     # 딕셔너리 안에 있는 value 를 알파벳 순으로 정렬한다
#     for ap in airport:
#         airport[ap].sort()
#
#     def dfs():
#         stack = ['ICN']
#         path = []
#         while stack:
#             top = stack[-1]
#             if top not in airport or len(airport[top]) == 0:
#                 path.append(stack.pop())
#             else:
#                 stack.append(airport[top].pop(0))
#         return path[::-1]
#
#     answer = dfs()
#     return answer

# 섬 연결하기
# def find_root(x):
#     global p
#     while x != p[x]:
#         x = p[x]
#     return x
#
# def solution(n, costs):
#     global p
#     answer = 0
#     costs.sort(key=lambda x: x[2])
#     p = [i for i in range(n)]
#     cnt = 0
#     for start, end, weight in costs:
#         if end > start:
#             start, end = end, start
#         if find_root(start) != find_root(end):
#             cnt += 1
#             answer += weight
#             p[find_root(end)] = find_root(start)
#             if cnt == n-1: # 간선의 개수가 모두 나오면 끝(노드가 n개니까 간선은 n-1개)
#                 break
#     return answer

# 네트워크
# def solution(n, computers):
#     def dfs(node):
#         used[node] = 1
#         for idx in graph[node]:
#             if used[idx] == 0:
#                 dfs(idx)
#
#     answer = 0
#     used = [0]*n
#     graph = [[] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if i != j and computers[i][j] != 0:
#                 graph[i].append(j)
#     for i in range(n):
#         if used[i] == 0:
#             answer += 1
#             dfs(i)
#     return answer

