# 지그재그 숫자
# T = int(input())
# for tc in range(1, T+1):
#     numbers = int(input())
#     total = 0
#     for n in range(1, numbers+1):
#         if n % 2:
#             total += n
#         else:
#             total -= n
#     print(f'#{tc} {total}')

# 새로운 불면증 치료법
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     copy_N = N
#     numbers = list(range(0, 10))
#     while len(numbers) != 0:
#         for n in str(copy_N):
#             if int(n) in numbers:
#                 numbers.remove(int(n))
#         copy_N += N
#     print(f'#{tc} {copy_N - N}')

# 수도 요금 경쟁
# T = int(input())
# for tc in range(1, T+1):
#     P, Q, R, S, W = map(int, input().split())
#     if W <= R:
#         result = Q
#     else:
#         result = Q + (W-R)*S
#     print(f'#{tc} {min(W * P, result)}')

# 두 개의 숫자열
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     result = []
#     if M > N:
#         N, M = M, N
#         A, B = B, A
#     for i in range(N-M+1):
#         total = 0
#         move = A[i:i+M]
#         for j in range(len(move)):
#             total += move[j]*B[j]
#         result.append(total)
#     print(f'#{tc} {max(result)}')

# 초심자의 회문 검사
# T = int(input())
# for tc in range(1, T+1):
#     word = input()
#     compare = ''
#     for w in range(len(word)-1,-1,-1):
#         compare += word[w]
#     if word == compare:
#         ans = 1
#     else:
#         ans = 0
#     print(f'#{tc} {ans}')

# 이진수
# T = int(input())
# change = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
# for tc in range(1, T+1):
#     N, nums = input().split()
#     ans = ''
#     for n in nums:
#         sub = ''
#         if n.isdigit():
#             x = int(n)
#             for _ in range(4):
#                 sub = str(x % 2) + sub
#                 x = x // 2
#         else:
#             x = change[n]
#             for _ in range(4):
#                 sub = str(x % 2) + sub
#                 x = x // 2
#         ans += sub
#     print(f'#{tc} {ans}')

# 이진수2
# T = int(input())
# for tc in range(1, T+1):
#     N = float(input())
#     ans = ''
#     std = 0.5
#     while N > 0:
#         if len(ans) >= 13:
#             ans = 'overflow'
#             break
#
#         if N >= std:
#             ans += '1'
#             N -= std
#             std /= 2
#         else:
#             ans += '0'
#             std /= 2
#     print(f'#{tc} {ans}')

