# 1931번 (회의실 배정)
# import sys
# N = int(sys.stdin.readline())
# schedule = []
# for _ in range(N):
#     start, end = map(int, sys.stdin.readline().split())
#     schedule.append((start, end))
# schedule.sort(key=lambda x:(x[1],x[0]))
# std = 0
# cnt = 0
# for i in schedule:
#     if i[0] >= std:
#         cnt += 1
#         std = i[1]
# print(cnt)

# 13305번 (주유소)
# import sys
#
# N = int(sys.stdin.readline())
# dist = list(map(int, sys.stdin.readline().split())) # 도시를 연결하는 도로의 길이
# node = list(map(int, sys.stdin.readline().split())) # 주유소의 리터당 기격
#
# i = 0
# cost = 0
# while True:
#     if i >= N-1:
#         break
#
#     cnt = 1
#     for j in range(i+1, N-1):
#         if node[i] > node[j]:
#             break
#         cnt += 1
#     for idx in range(i, cnt+i):
#         cost += dist[idx]*node[i]
#
#     i += cnt
#
# print(cost)
