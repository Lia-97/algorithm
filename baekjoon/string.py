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

# 1764번 (듣보잡)
# N, M = map(int, input().split()) # 듣지못한 사람, 보지 못한 사람
# unlisten = []
# unsee = []
# for _ in range(N):
#     unlisten.append(input())
# for _ in range(M):
#     unsee.append((input()))
#
# ans = list(set(unlisten) & set(unsee))
# ans.sort()
#
# print(len(ans))
# for i in ans:
#     print(i)

# 4949번 (균형잡힌 세상)
# tc = []
# while True:
#     test = list(input())
#     if test == ['.']:
#         break
#     tc.append(test)
#
#
# for sentence in tc:
#     check = ['(', ')', '[', ']']
#     stack = ['*']
#     while sentence:
#         string = sentence.pop()
#         if string in check:
#             if string == '(' and stack[-1] == ')':
#                 stack.pop()
#             elif string == '[' and stack [-1] == ']':
#                 stack.pop()
#             else:
#                 stack.append(string)
#     if len(stack) == 1:
#         ans = 'yes'
#     else:
#         ans = 'no'
#
#     print(ans)

# 1874번 (스택 수열) _ 미완
# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(int(input()))
# real_nums = nums[::-1]
# print(real_nums)
#
# stack = []
# while len(stack) != n:
#     while

# OX 퀴즈
# T = int(input())
# for _ in range(T):
#     result = input()
#     add = 1
#     total = 0
#     for i in range(len(result)):
#         if result[i] == 'O':
#             total += add
#             add += 1
#         elif result[i] == 'X':
#             add = 1
#     print(total)

# 그대로 출력하기
# while True:
#     try:
#         sentence = input()
#     except:
#         break
#     print(sentence)

#