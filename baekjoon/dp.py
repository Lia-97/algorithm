# 9461번 (파도반 수열)
# T = int(input())
# for tc in range(T):
#     dp = [1, 1, 1]
#     N = int(input())
#     for i in range(3, N):
#         dp.append(dp[i-3] + dp[i-2])
#     print(dp[N-1])

# 1932번 (정수 삼각형)
# n = int(input())
# tri = [list(map(int, input().split())) for _ in range(n)]
#
# for i in range(1, len(tri)):
#     for j in range(len(tri[i])):
#         if j == 0:
#             tri[i][0] = tri[i][0] + tri[i-1][0]
#         elif j == len(tri[i])-1:
#             tri[i][len(tri[i])-1] = tri[i][len(tri[i])-1] + tri[i-1][len(tri[i-1])-1]
#         else:
#             tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]
#
# print(max(tri[len(tri)-1]))

# 2579번 (계단 오르기) _ 정답 코드
# n = int(input())
# stairs = [0] * 301
# dp = [0] * 301
# for i in range(n):
#     stair = int(input())
#     stairs[i+1] = stair
#
# dp[1] = stairs[1]
# dp[2] = stairs[1]+stairs[2]
# dp[3] = max(stairs[1], stairs[2]) + stairs[3]
# for i in range(4, n+1):
#     dp[i] = max(dp[i-2]+stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
#
# print(dp[n])

# 2579번 (계단 오르기) _ 원래 쓴 코드
n = int(input())
stairs = [0]
dp = [0] * 301
for _ in range(n):
    stair = int(input())
    stairs.append(stair)
dp[1] = stairs[1]
dp[2] = stairs[1]+stairs[2]
dp[3] = max(stairs[1], stairs[2]) + stairs[3]
for i in range(4, n+1):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[n])

# 11053번 (가장 긴 증가하는 부분 수열)
# N = int(input())
# A = list(map(int, input().split()))
# dp = [0] * N

# 1912번 (연속합) _ 시간초과...
# n = int(input())
# nums = list(map(int, input().split()))
# N = len(nums)
# max_total = -100000000
# for i in range(N):
#     for j in range(i+1, N):
#         total = 0
#         for l in range(i, j):
#             total += nums[l]
#         if total > max_total:
#             max_total = total
# print(max_total)

# 1912번 (연속합) _ 정답
# n = int(input())
# nums = list(map(int, input().split()))
# N = len(nums)
# dp = [0] * N
# dp[0] = nums[0]
# for i in range(1, N):
#     dp[i] = max(dp[i-1] + nums[i], nums[i])
# print(max(dp))