# 프린터
# from collections import deque
# def solution(priorities, location):
#     answer = 0
#     cnt = 0
#     q = deque()
#     # 찾는 인덱스를 알기 위해 enumerate
#     for idx,num in enumerate(priorities):
#         q.append((num,idx))
#     while True:
#         max_v = max(q)[0]
#         turn = q.popleft()
#         if turn[0] == max_v and turn[1] != location:
#             cnt += 1
#         elif turn[0] == max_v and turn[1] == location:
#             cnt += 1
#             answer = cnt
#             break
#         else:
#             q.append(turn)
#     return answer

# 기능개발
# from collections import deque
# def solution(progresses, speeds):
#     answer = []
#     spare = deque()
#     # 일을 모두 끝내려면 남은 기간을 spare 에 추가
#     for i in range(len(progresses)):
#         todo = 100 - progresses[i]
#         speed = speeds[i]
#         if todo % speed == 0:
#             spare.append(todo // speed)
#         else:
#             spare.append((todo // speed) +1)
#
#     max_work = 0 # max_work 초기화
#     while spare:
#         work = spare.popleft()
#         if work > max_work:
#             answer.append(1)
#             max_work = work
#         else:
#             answer[-1] += 1
#
#     return answer

# 큰 수 만들기 _ recursive 에러.. 스택으로 풀기!
# def large_num(lis, start, end):
#     global answer
#     max_v = 0
#     idx = start
#     for i in range(start, end):
#         if lis[i] > max_v:
#             max_v = lis[i]
#             idx = i + 1
#     answer.append(max_v)
#     if end + 1 <= len(lis):
#         large_num(lis, idx, end + 1)
#
# def solution(number, k):
#     global answer
#     answer = []
#     number = list(map(int, number))
#
#     large_num(number, 0, k+1)
#     answer = list(map(str, answer))
#     answer = ''.join(answer)
#     return answer

# 큰 수 만들기 _ 스택으로 풀어보기

# 가장 큰 수
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     print(numbers)
#     answer = ''.join(numbers)
#     return answer
#
# print(solution([3, 30, 34, 5, 9]))

# 대여 시간
# N= int(input()) # 인원 수
# times = [input() for _ in range(N)] # 01/34 ~ 89/1112
# start = []
# end = []
# for time in times:
#     start.append(int(time[0:2])*60 + int(time[3:5]))
#     end.append(int(time[8:10])*60 + int(time[11:13]))
#
# s = max(start)
# e = min(end)
# if s > e:
#     print(-1)
# else:
#     print(f'{s//60:#02d}:{s%60:#02d} ~ {e//60:#02d}:{e%60:#02d}')

# 배송 전략
# N = int(input()) # 경로의 길이
# load = input() # 경로
# dp=[0]*50
# dp[0] = 1
#
# if load[1] == '1':
#     dp[1] = 1
# else:
#     dp[1] = 0
#
# for i in range(2,N):
#     if load[i] == '0':
#         dp[i] = 0
#     else:
#         dp[i] = dp[i-2] + dp[i-1]
#
# print(dp[N-1])

# 배치
# def find_product(i,j,size):
#     for x in range(i,i+size):
#         for y in range(j,j+size):
#             if place[x][y] == '0':
#                 return False
#     return True
#
# N=int(input())
# place=[input() for _ in range(N)]
# product=[0]*(N+1)
# for size in range(1,N+1):
#     for i in range(0,N+1-size):
#         for j in range(0,N+1-size):
#             if find_product(i,j,size):
#                 product[size]+=1
#
# print('total: {0}'.format(sum(product)))
# for i in range(1,len(product)):
#     if product[i] !=0:
#         print('size[{0}]: {1}'.format(i,product[i]))

# 콘텐츠
# A, B, C, D, E = map(float, input().split())
# grade = {'A': A,
#          'B': B,
#          'C': C,
#          'D': D,
#          'E': E} # 등급별 점수
#
# N, M = map(int, input().split()) # 행 개수, 열 개수
# watched = [input() for _ in range(N)]
# point = [input() for _ in range(N)]
#
# result = []
#
# for i in range(N-1,-1,-1):
#     for j in range(M-1,-1,-1):
#         if watched[i][j] != 'W':
#             result.append((watched[i][j], point[i][j], grade[point[i][j]], i,j)) # 알파벳, 평점, x좌표, y좌표
#
# result.sort(key=lambda x:(-ord(x[0]), -x[2], x[3], x[4]))
#
# for r in result:
#     print(' '.join(map(str,r[1:])))

# 시선
# from collections import deque
#
# def bfs():
#     while q:
#         x, y, cnt = q.pop()
#         if arr[x+1][y] == '.' and visited[x+1][y] == 0:
#             q.appendleft((x+1,y, cnt))
#             visited[x+1][y] = 1
#             if x+1 == M-1:
#                 return cnt
#         else:
#             for d in dir:
#                 nx, ny = x + d[0], y + d[1]
#                 if 0 <= nx < M and 0 <= ny < N:
#                     if arr[nx][ny] == '.' and visited[nx][ny] == 0:
#                         q.appendleft((nx,ny,cnt+1))
#                         visited[nx][ny] = 1
#     return -1
#
# N, M = map(int, input().split()) # 열 개수, 행 개수
# arr = [input() for _ in range(M)]
# q = deque()
# dir = [(0,-1),(0,1)] # 좌, 우
# visited = [[0]*N for _ in range(M)]
#
# for i in range(N):
#     if arr[0][i] == 'c':
#         q.appendleft((0,i,0)) # x좌표, y좌표, 좌우로 이동한 횟수
#         visited[0][i] = 1
#
# print(bfs())

# 스킬트리 _ 시간초과
# def solution(skill, skill_trees):
#     checks = []
#     cnt = 0
#     for sk in skill_trees:
#         sub = ''
#         for s in sk:
#             if s in skill:
#                 sub += s
#         checks.append(sub)
#     print(checks)
#
#     for check in checks:
#         for i in range(len(skill)):
#             if skill[i] == check[0]:
#                 if skill[i:i+len(check)+1] == check:
#                     cnt += 1
#     return cnt
#
# print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]))

# 스킬트리_ 실패
# def solution(skill, skill_trees):
#     cnt = len(skill_trees)
#     for skills in skill_trees:
#         if skill[0] not in skills:
#             cnt -= 1
#             continue
#         sub = ''
#         for s in skills:
#             if s in skill:
#                 sub += s
#             if sub not in skill:
#                 cnt -= 1
#                 break
#     return cnt
#
# print(solution('D', ["GQWR"]))

#
def three(k):
    double = k
    total = 0
    while double >= 1:
        total += 3 ** double
        double -= 1
    return total

def solution(n):
    for N in range(1, 1000):
        if three(N-1) < n <= three(N):
            break
    # N의 자리 숫자임


print(solution(10))


