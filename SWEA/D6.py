# 1795. 인수의 생일 파티
def f(q):
    while q:
        current_node, current_weight = heapq.heappop(q)

        if current_weight > cost[current_node]:
            continue

        for next_node, weight in graph[current_node]:
            price = weight + current_weight
            if price < cost[next_node]:
                cost[next_node] = price
                heapq.heappush(q, (next_node, cost[next_node]))

    return


from collections import defaultdict
import heapq
T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split()) # N개 집, M개의 간선, 도착지점 X
    graph = defaultdict(list)
    graph_back = defaultdict(list)
    INF = 1000000

    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((y, c))
        graph_back[y].append(x, c)

    for i in range(1, N+1):
        cost = [INF] * (N + 1)
        cost[i] = 0
        q = []
        heapq.heappush(q, (i, 0))
        f(q)
        print(q)
    print(cost)