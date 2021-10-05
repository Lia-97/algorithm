# 2164번 (카드2)
# from collections import deque
# card = int(input())
# q = deque()
# for i in range(card):
#     q.append(i+1)
#
# while len(q) > 1:
#     a = q.popleft()
#     b = q.popleft()
#     q.append(b)
# print(q.pop())

# 10773번 (제로)
# K = int(input())
# num = []
# for _ in range(K):
#     i = int(input())
#     if i != 0:
#         num.append(i)
#     else:
#         num.pop()
# print(sum(num))

# 9012번 (괄호)
# T = int(input())
# for _ in range(T):
#     sentence = list(input())
#     sum = 0
#     for i in sentence:
#         if i == '(':
#             sum += 1
#         elif i == ')':
#             sum -= 1
#         if sum < 0:
#             print('NO')
#             break
#     if sum > 0:
#         print('NO')
#     elif sum == 0:
#         print('YES')

# 1874번 (스택 수열)
# import sys
# from collections import deque
# N = int(sys.stdin.readline())
# sequence = deque()
# stack = []
# ans = []
# for num in range(N):
#     sequence.append(int(sys.stdin.readline()))
# for i in range(1, N+1):
#     stack.append(i) # 1부터 스택에 push 하고
#     ans.append('+') # push 표시
#     while stack and stack[-1] == sequence[0]: # 스택의 가장 마지막 값이 수열의 첫번째 값과 같다면
#         stack.pop() # 스택의 가장 마지막 값 제거
#         sequence.popleft() # 수열의 첫번째 값 제거
#         ans.append('-') # pop 표시
#     if i == N and stack and stack[-1] != sequence[0]:
#         ans = ["NO"]
#         break
# for a in ans:
#     print(a)
