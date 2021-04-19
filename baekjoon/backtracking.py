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
def possible(idx):
    for i in range(idx):
        if idx - i == abs(row[idx]-row[i]):
            return True
        else:
            return False

def f(idx):
    global ans
    if idx == N:
        ans += 1
        return

    for i in range(N):
        if used_col[i] == 1:
            continue
        if possible(i):
            continue
        used_col[i] = 1
        row[i] = 1


N = int(input())
row = [0]*N
used_col = [0]*N
ans = 0
f(0)

