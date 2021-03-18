# 그룹 단어 체커
# N = int(input())
# total = N
# for _ in range(N):
#     word = list(map(str, input()))
#     result = []
#     while len(word) != 0:
#         last = word.pop()
#         if last not in result:
#             result.append(last)
#         else:
#             if last != result[-1]:
#                 total -= 1
#                 break
# print(total)

# 근묵자흑
# N, K = map(int, input().split()) # 수열 길이, 연속적으로 골라야 하는 수
# lis = list(map(int, input().split()))
#
# minimal = 100000
# idx = 0
# for i in range(N):
#     if lis[i] < minimal:
#         minimal = lis[i]
#         idx = i
# if i <= K-1:
#     ans = N // (K-1)
# else:
#     pass

# 사은품 교환하기
# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     ans = 0
#     if N >= 5:
#         drink = N // 5
#         if M // drink >= 7:
#             ans = N // 5
#         else:
#             ans = (N+M) // 12
#
#     print(ans)