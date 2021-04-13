# 수 찾기
# N = int(input())
# A = list(map(int, input().split()))
# A.sort()
# M = int(input())
# nums = list(map(int, input().split()))
# for n in nums:
#     ans = 0
#     start = 0
#     end = len(A) - 1
#     while start <= end:
#         mid = (end + start) // 2
#         if A[mid] == n:
#             ans = 1
#             break
#         elif A[mid] < n:
#             start = mid+1
#         elif A[mid] > n:
#             end = mid-1
#     print(ans)

# 2805번 (나무 자르기)
# import sys
# N, M = map(int, sys.stdin.readline().split()) # 나무의 수, 나무의 길이
# trees = list(map(int, sys.stdin.readline().split()))
# start = 1
# end = max(trees)
# while start <= end:
#     total = 0
#     mid = (start + end) // 2
#     # 시간초과
#     # for tree in trees:
#     #     if tree - mid > 0:
#     #         total += tree - mid
#     # 이렇게 하면 시간초과 X --> comprehension 이 더 빠르다.
#     total = sum(tree - mid if tree > mid else 0 for tree in trees)
#
#     if total >= M:
#         start = mid+1
#     elif total < M:
#         end = mid-1
#
# print(end)
