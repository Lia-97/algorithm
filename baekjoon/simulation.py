# 1100번 (하얀 칸)
# arr = [] # 0흰, 1검
# for i in range(8):
#     if i%2:
#         arr.append([1,0,1,0,1,0,1,0])
#     else:
#         arr.append([0,1,0,1,0,1,0,1])
#
# chess = [list(input()) for _ in range(8)]
# cnt = 0
#
# for i in range(8):
#     for j in range(8):
#         if arr[i][j] == 0 and chess[i][j] == 'F':
#             cnt += 1
# print(cnt)

# 1966번 (프린터 큐)
# from collections import deque
# T = int(input()) # 테스트케이스 수
# for tc in range(T):
#     N, M = map(int, input().split()) # 문서 개수, 문서 위치
#     papers = list(map(int,input().split())) # 문서의 중요도
#     q = deque()
#     cnt = 0
#     for i, paper in enumerate(papers):
#         q.append((paper,i))
#
#     while True:
#         max_v = max(q)[0]
#         num, idx = q.popleft()
#         if num == max_v and idx == M:
#             cnt += 1
#             break
#         elif num == max_v and idx != M:
#             cnt += 1
#         else:
#             q.append((num,idx))
#
#     print(cnt)

# 1966번 (프린터 큐) _ 시간 줄여보기
# from collections import deque
# T = int(input()) # 테스트케이스 수
# for tc in range(T):
#     N, M = map(int, input().split()) # 문서 개수, 문서 위치
#     papers = list(map(int,input().split())) # 문서의 중요도
#     q = deque()
#     cnt = 0
#     for i, paper in enumerate(papers):
#         q.append((paper,i))
#
#     max_list = sorted(papers)
#
#     while True:
#         num, idx = q.popleft()
#         if num == max_list[-1] and idx == M:
#             cnt += 1
#             break
#         elif num == max_list[-1] and idx != M:
#             cnt += 1
#             max_list.pop()
#         else:
#             q.append((num,idx))
#     print(cnt)

# 14503번 (로봇 청소기)