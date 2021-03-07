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
