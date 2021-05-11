# 9370번 (미확인 도착지)
# import heapq, sys
# from collections import defaultdict
#
# def dijkstra(q):
#     while q:
#         current_weight, current_node = heapq.heappop(q)
#
#         if current_weight > key[current_node]:
#             continue
#
#         for point in graph[current_node]:
#             next_node, weight = point[0], point[1]
#             next_weight = current_weight + weight
#             if next_weight < key[next_node]:
#                 key[next_node] = next_weight
#                 heapq.heappush(q, (next_weight, next_node))
#     return
#
# T = int(input())
# for _ in range(T):
#     answer = []
#     target_list = [] # 도착지 후보군 리스트 초기화
#     graph = defaultdict(list) # 도로 그래프 초기화
#     node, edge, target = map(int, sys.stdin.readline().split()) # 노드, 간선, 목적지후보
#     start, g, h = map(int, input().split()) # 출발지, g & h 사이 도로 지남
#
#     # 도로 그래프에 정보 업데이트 (양방향 그래프)
#     for _ in range(edge):
#         node1, node2, dist = map(int, sys.stdin.readline().split()) # , b 사이에 d의 가중치를 가지는 도로
#         if (node1, node2) == (g, h) or (node1, node2) == (h, g):
#             graph[node1].append((node2, dist-0.1))
#             graph[node2].append((node1, dist-0.1))
#         else:
#             graph[node1].append((node2, dist))
#             graph[node2].append((node1, dist))
#
#     # 도착지 후보군 추가
#     for _ in range(target):
#         target_list.append(int(sys.stdin.readline()))
#
#     INF = float('inf')
#     q = []
#     key = [INF]*(node+1) # 각 노드까지 가는데 걸리는 비용을 무한대로 초기화
#     key[start] = 0 # 이동 비용 리스트의 출발지는 0으로 설정
#     heapq.heappush(q, (0, start))
#     dijkstra(q)
#
#     for target in target_list:
#         if key[target] != INF and type(key[target]) != int:
#             answer.append(target)
#
#     answer.sort()
#     print(*answer)

# 9370번 (미확인 도착지)
import heapq, sys
from collections import defaultdict

def dijkstra(q):
    while q:
        current_weight, current_node, flag = heapq.heappop(q)

        if current_weight > key[current_node][0]:
            continue

        for point in graph[current_node]:
            next_node, weight = point[0], point[1]
            next_weight = current_weight + weight
            if next_weight < key[next_node][0]:
                if (current_node, next_node) == (g, h) or (current_node, next_node) == (h, g):
                    flag = True
                key[next_node][0] = next_weight
                key[next_node][1] = flag
                heapq.heappush(q, (next_weight, next_node, flag))

            elif next_weight == key[next_node][0]:
                if key[next_node][1] == True:
                    flag = True
                if (current_node, next_node) == (g, h) or (current_node, next_node) == (h, g):
                    flag = True
                key[next_node][0] = next_weight
                key[next_node][1] = flag
                heapq.heappush(q, (next_weight, next_node, flag))

    return

T = int(sys.stdin.readline())
for _ in range(T):
    answer = []
    target_list = [] # 도착지 후보군 리스트 초기화
    graph = defaultdict(list) # 도로 그래프 초기화
    node, edge, target = map(int, sys.stdin.readline().split()) # 노드, 간선, 목적지후보
    start, g, h = map(int, input().split()) # 출발지, g & h 사이 도로 지남

    # 도로 그래프에 정보 업데이트 (양방향 그래프)
    for _ in range(edge):
        node1, node2, dist = map(int, sys.stdin.readline().split()) # , b 사이에 d의 가중치를 가지는 도로
        graph[node1].append((node2, dist))
        graph[node2].append((node1, dist))

    # 도착지 후보군 추가
    for _ in range(target):
        target_list.append(int(sys.stdin.readline()))

    INF = float('inf')
    q = []
    key = [[INF, False] for _ in range(node+1)] # 각 노드까지 가는데 걸리는 비용을 무한대로 초기화
    key[start][0] = 0 # 이동 비용 리스트의 출발지는 0으로 설정
    heapq.heappush(q, (0, start, False))
    dijkstra(q)
    for target in target_list:
        if key[target][0] != INF and key[target][1] == True:
            answer.append(target)
    answer.sort()
    print(*answer)
