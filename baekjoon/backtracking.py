# 15649번 (N과 M(1)) _ permutations
# from itertools import permutations
# N, M = map(int, input().split())
# for comb in permutations(list(range(1, N+1)), M):
#     print(*comb)

# 15649번 (N과 M(1)) _ 백트래킹으로 풀기
# def dfs(sub):
#     if len(sub) == M:
#         print(*sub)
#         return
#
#     for i in range(N):
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(sub+[arr[i]])
#             visited[i] = 0
#
# N, M = map(int, input().split())
# arr = list(range(1, N + 1))
# visited = [0]*N
# dfs([])

# 15650번 (N과 N(2))
# N, M = map(int, input().split())
# arr = list(range(1, N+1))
# def f(idx, sub):
#     if len(sub) == M:
#         print(*sub)
#         return
#
#     for i in range(idx, N):
#         f(i+1, sub+[arr[i]])
#
# f(0, [])

# 15651번 (N과 M(3))
# def f(sub):
#     if len(sub) == M:
#         print(*sub)
#         return
#
#     for i in range(N):
#         f(sub+[arr[i]])
#
# N, M = map(int, input().split())
# arr = list(range(1, N+1))
# f([])

# 15652번 (N과 M(4))
# def f(idx, sub):
#     if len(sub) == M:
#         print(*sub)
#         return
#
#     for i in range(idx, N):
#         f(i, sub+[arr[i]])
#
# N, M = map(int, input().split())
# arr = list(range(1, N+1))
# f(0, [])

# 9663번 (N-Queen)
# 대각선 체크 함수
# def possible(idx, i): # (idx=행인덱스, i=해당행에서 queen을 놓을 컬럼인덱스)
#     for j in range(idx):
#         # 행 인덱스의 차이가 queen이 놓인 컬럼 인덱스의 차이와 같다면 possible하지 않으므로 False
#         if idx - j == abs(col[j]-i) or col[j] == i:
#             return False
#     return True
#
# def f(idx):
#     global ans
#     # N번째 행까지 갔으면 ans +1
#     if idx == N:
#         ans += 1
#         return
#
#     for i in range(N): # 컬럼을 순회하는데,
#         if used[i] == 0: # queen이 놓여있지 않은 컬럼이라면
#             if possible(idx, i): # 대각선으로도 안 겹치는지 확인 (idx=행인덱스, i=해당행에서 queen을 놓을 컬럼인덱스)
#                 # True 일 때 아래 코드가 실행됨
#                 col[idx] = i # idx 행에서 i를 컬럼 인덱스로 가지는 위치에 queen을 놓았음을 의미
#                 used[i] = 1 # queen을 놓은 i 컬럼을 1로 바꿔서, 다음행에서 사용불가능하도록 설정
#                 f(idx+1) # 다음행에서 함수 호출
#                 col[idx] = 0 # 되돌아가기 위해 0으로 다시 리셋
#                 used[i] = 0
#
# N = int(input())
# col = [0]*N # 퀸을 놓은 컬럼 index
# used = [0]*N # 퀸을 놓은 컬럼을 1로 바꿔줌
#
# ans = 0
# f(0)
# print(ans)

# 9663번 (N-Queen) _ 원재의 솔루션
# def check(row,col):
#     if used_col[col]==1:
#         return False
#     if used_dig[row+col]==1:
#         return False
#     if used_rdig[row-col+N-1] == 1:
#         return False
#     return True
#
# def back_tracking(row):
#     if row == N:
#         return 1
#
#     result=0
#     for col in range(N):
#         if check(row,col):
#             used_col[col] = used_dig[row + col] = used_rdig[row - col + N - 1] = 1
#             result+=back_tracking(row+1)
#             used_col[col] = used_dig[row + col] = used_rdig[row - col + N - 1] = 0
#     return result
#
# N=int(input())
# used_col=[0]*N
# used_dig=[0]*(2*N-1)
# used_rdig=[0]*(2*N-1)
# print(back_tracking(0))

# 14889번 (스타트와 링크) _ 실패
# def make_team(idx, team):
#     global used, min_diff
#
#     if len(team) == N//2:
#         print(team)
#         used = [0]*N
#
#         else_team = []
#         for i in range(N):
#             if i not in team:
#                 else_team.append(i)
#
#         total = calc_power(team, 0, [])
#         else_total = calc_power(else_team, 0, [])
#         print(total, else_total)
#
#         print('total',total)
#         if abs(total - else_total) < min_diff:
#             min_diff = abs(total - else_total)
#
#     for i in range(idx, N):
#         if visited[i] == 0:
#             visited[i] = 1
#             make_team(i+1, team+[i])
#             visited[i] = 0
#
# def calc_power(team, idx, sub):
#     global used
#     total = 0
#     if len(sub) == 2:
#         x, y = sub[0], sub[1]
#         total += powers[x][y] + powers[y][x]
#         print('total2',total)
#
#     for i in range(idx, N//2):
#         if used[i] == 0:
#             used[i] = 1
#             calc_power(team, i+1, sub+[i])
#
#     return total
#
#
# N = int(input())
# powers = [list(map(int, input().split())) for _ in range(N)]
# sum_powers = 0
# for i in range(N):
#     sum_powers += sum(powers[i])
# visited = [0]*N
# min_diff = float('inf')
# make_team(0, [])
# print(min_diff)

# 6603번 (로또)
# import sys
#
# def k_set(idx, sub):
#     result = []
#     if len(sub) == k:
#         return [sub]
#     for i in range(idx, len(nums)):
#         if used_nums[i] == 0:
#             used_nums[i] = 1
#             result.extend(k_set(i+1, sub+[nums[i]]))
#             used_nums[i]= 0
#     return result
#
# def result_set(idx, sub):
#     result = []
#     if len(sub) == 6:
#         return [sub]
#     for i in range(idx, k):
#         if used_c[i] == 0:
#             used_c[i] = 1
#             result.extend(result_set(i+1, sub+[c[i]]))
#             used_c[i] = 0
#     return result
#
# while True:
#     data = sys.stdin.readline().strip()
#     if data == '0':
#         break
#     lis = list(map(int, data.split()))
#     k = lis[0]
#     nums = lis[1:]
#     used_nums = [0]*len(nums)
#     candidate = k_set(0, [])
#     answer = []
#     for c in candidate:
#         used_c = [0]*len(c)
#         answer.extend(result_set(0, []))
#
#     for a in answer:
#         print(' '.join(map(str, a)))
#     print('')

# 10819번 (차이를 최대로)
# def getSum(lis):
#     total = 0
#     for i in range(1, len(lis)):
#         total += abs(lis[i-1] - lis[i])
#     return total
#
# def getArr(sub):
#     if len(sub) == N:
#         return getSum(sub)
#
#     ans = float('-inf')
#
#     for i in range(N):
#         if used[i] == 0:
#             used[i] = 1
#             ans = max(ans, getArr(sub+[arr[i]]))
#             used[i] = 0
#
#     return ans
#
# N = int(input()) # 배열의 길이
# arr = list(map(int, input().split()))
# used = [0]*N
# print(getArr([]))
