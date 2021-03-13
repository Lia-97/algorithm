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

# 큰 수 만들기
