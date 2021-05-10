# 9370번 (미확인 도착지)
import heapq
from collections import defaultdict

def dijkstra():
    pass

T = int(input())
for _ in range(T):
    target_list = [] # 도착지 후보군 리스트 초기화
    graph = defaultdict(list) # 도로 그래프 초기화
    node, edge, target = map(int, input().split()) # 노드, 간선, 목적지후보
    start, g, h = map(int, input().split()) # 출발지, g & h 사이 도로 지남

    # 도로 그래프에 정보 업데이트 (양방향 그래프)
    for _ in range(edge):
        node1, node2, dist = map(int, input().split()) # , b 사이에 d의 가중치를 가지는 도로
        graph[node1].append((node2, dist))
        graph[node2].append((node1, dist))

    # 도착지 후보군 추가
    for _ in range(target):
        target_list.append(int(input()))

    INF = float('inf')
    q = []
    key = [INF]*(n+1) # 각 노드까지 가는데 걸리는 비용을 무한대로 초기화
    key[s] = 0 # 이동 비용 리스트의 출발지는 0으로 설정
    heapq.heappush(q, ())
