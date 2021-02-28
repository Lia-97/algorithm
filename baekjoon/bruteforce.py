# 2798번 (블랙잭) _ 부분집합으로 풀었더니 시간초과 뜸
# import sys
# N, M = map(int,sys.stdin.readline().rstrip().split())
# lis = list(map(int,sys.stdin.readline().rsplit()))
# card = []
# for i in range(1 << N):
#     sub = []
#     for j in range(N):
#         if i & (1<<j):
#             sub.append(lis[j])
#     if len(sub) == 3:
#         card.append(sub)
#
# max_sum = 0
# for c in card:
#     if sum(c) <= M and sum(c) > max_sum:
#        max_sum = sum(c)
#
# print(max_sum)

# 2798번 (블랙잭)
# N, M = map(int, input().split())
# lis = list(map(int, input().split()))
# max_sum = 0
# for i in range(N):
#     for j in range(i+1, N):
#         for l in range(j+1, N):
#             if lis[i]+lis[j]+lis[l] <= M and lis[i]+lis[j]+lis[l] > max_sum:
#                 max_sum = lis[i]+lis[j]+lis[l]
# print(max_sum)

#