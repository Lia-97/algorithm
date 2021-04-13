# 다익스트라
# mygraph = {
#     'A': {'B':8, 'C':1, 'D':2},
#     'B' : {},
#     'C': {'B':5, 'D':2},
#     'D': {'E':3, 'F':5},
#     'E': {'F':1},
#     'F': {'A':5}
# }
#
# import heapq
#
#
# def dijkstra(graph, start):
#     # 초기화. 배열을 선언하여 첫 정점에서 각 정점까지의 거리를 저장. 초기에는 첫 정점의 거리는 0, 나머지는 무한대로 저장함
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#     queue = []  # 우선순위 큐
#     heapq.heappush(queue, [distances[start], start])  # 우선순위 큐에 첫 정점 저장
#
#     # 우선순위 큐가 빌 때까지 노드를 꺼낸다.
#     while queue:
#         current_distance, current_node = heapq.heappop(queue)  # 우선순위 큐에서 꺼낸 첫 정점의 거리와 번호
#         if distances[current_node] < current_distance:
#             continue
#
#         # 배열에서 꺼낸 첫 정점거리 + 배열에서 꺼낸 첫 정점부터 연결된 노드까지 거리를 더해서 distance 라는 변수에 저장
#         for adjacent, weight in graph[current_node].items():
#             distance = current_distance + weight
#
#             # 첫 정점에서 인접한 각 노드로 가는 거리와 현재 배열에 저장되어 있는 첫 정점에서 각 정점까지 거리를 비교
#             if distance < distances[adjacent]:
#                 # 현재 배열에 저장되어 있는 첫 정점에서 인접한 노드로 가는 거리가 더 짧으면 배열을 업데이트
#                 distances[adjacent] = distance
#                 # 우선순위 큐에도 추가한다.
#                 heapq.heappush(queue, [distance, adjacent])
#
#     return distances
#
# print(dijkstra(mygraph, 'A'))

# 1753번 (최단경로) _ 시간초과
# from collections import defaultdict
# import heapq, sys
#
# def dijkstra(q):
#     while q:
#         current_node, current_weight = heapq.heappop(q)
#         if weights[current_node] < current_weight:
#             continue
#
#         for point, price in graph[current_node]:
#             weight = current_weight + price
#             if weight < weights[point]:
#                 weights[point] = weight
#                 heapq.heappush(q, (point, weight))
#     return
#
# V, E = map(int, sys.stdin.readline().split()) # 정점의 개수, 간선의 개수
# start = int(sys.stdin.readline())
# graph = defaultdict(list)
# weights = [float('inf')]*(V+1)
# weights[1] = 0 # 시작점은 비용이 0
# q = [] # 우선순위 큐
# heapq.heappush(q, (1, 0))
# for _ in range(E):
#     u, v, w = map(int, sys.stdin.readline().split()) # u에서 v로 가는 가중치 w인 간선
#     graph[u].append((v, w))
# dijkstra(q)
#
# for idx in range(1, len(weights)):
#     if weights[idx] == float('inf'):
#         print('INF')
#     else:
#         print(weights[idx])
