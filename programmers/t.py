# 숫자놀이
# def solution(s):
#     nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     sentence = s
#     for idx, n in enumerate(nums):
#         if n in s:
#             sentence = sentence.replace(n, str(idx))
#     return int(sentence)
#
# print(solution("one4seveneight"))


# 면접
# def solution(places):
#     dir = [(-1,0),(0,-1),(0,1),(1,0)]
#     dir_two = [(-2,0,-1,0),(2,0,1,0),(0,-2,0,-1),(0,2,0,1)]
#     dir_three = [(-1,-1,-1,0,0,-1),(-1,1,-1,0,0,1),(1,-1,0,-1,1,0),(1,1,0,1,1,0)]
#     def check(place):
#         for i in range(len(place)):
#             for j in range(len(place[i])):
#                 if place[i][j] == 'P':
#                     for d in dir:
#                         ni, nj = i+d[0], j+d[1]
#                         if 0 <= ni < len(place) and 0 <= nj < len(place[i]):
#                             if place[ni][nj] == 'P':
#                                 return 0
#                     for d2 in dir_two:
#                         ni, nj = i+d2[0], j+d2[1]
#                         nx, ny = i+d2[2], j+d2[3]
#                         if 0 <= ni < len(place) and 0 <= nj < len(place[i]):
#                             if place[ni][nj] == 'P' and place[nx][ny] != 'X':
#                                 print('2',i, j, ni, nj, nx, ny)
#                                 return 0
#                     for d3 in dir_three:
#                         ni, nj = i + d3[0], j + d3[1]
#                         nx, ny = i + d3[2], j + d3[3]
#                         na, nb = i + d3[4], j + d3[5]
#                         if 0 <= ni < len(place) and 0 <= nj < len(place[i]):
#                             if place[ni][nj] == 'P':
#                                 if place[nx][ny] != 'X' or place[na][nb] != 'X':
#                                     return 0
#         return 1
#
#
#
#     answer = []
#     for place in places:
#         answer.append(check(place))
#
#     return answer
# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

# 소트프웨어 개발
# def solution(n, k, cmd):
#     answer = ''
#     origin = list(range(n))
#     delete = []
#     selected = k
#     for change in cmd:
#         if change[0] == 'D':
#             selected += int(change[2])
#         elif change[0] == 'U':
#             selected -= int(change[2])
#         elif change[0] == 'C':
#             if selected != len(origin)-1:
#                 delete.append((selected, origin[selected])) # 삭제된 값과 그 값의 인덱스를 delete 리스트에 저장
#                 origin.pop(selected) # 그 다음 origin에서 값을 삭제
#             else:
#                 delete.append((selected, origin[selected]))
#                 origin.pop(selected)
#         elif change[0] == 'Z':
#             idx, val = delete.pop()
#             origin.insert(idx, val)
#
#     for idx in list(range(n)):
#         if idx in origin:
#             answer += 'O'
#         else:
#             answer += 'X'
#     return answer
#
# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

# 미로 탈출
# from collections import deque
# def solution(n, start, end, roads, traps):
#     def reverse_graph(lis):
#         for l in lis:
#             print(l)
#             if l in traps:
#                 for road in roads:  # 방향을 바꿔준다.
#                     if road[0] == l[0] or road[1] == l[0]:
#                         road[0], road[1] = road[1], road[0]
#                         return roads
#             else:
#                 return roads
#
#     answer = 0
#     q = deque()
#     sub_lis = [start, 0]
#     q.append(sub_lis)
#     print(q)
#     while q:
#         for lis in q:
#             print('l', lis)
#             reverse_graph(lis)
#             node, weight = lis.popleft()
#
#             if node == end:
#                 answer = weight
#                 break
#
#         for road in roads:
#             sub = []
#             print('cnt', node)
#             if road[0] == node:
#                 sub.append((road[1], weight+road[2]))
#                 print(q)
#         q.append(sub)
#
#     return answer
#
# print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))


# def solution(n, start, end, roads, traps):
#     def backtracking(node, weight):
#         if node == end:
#             return weight
#         flag = 0
#         if node in traps:  # 함정 노드라면
#             flag = 1
#             for road in roads:  # 방향을 바꿔준다.
#                 if road[0] == node or road[1] == node:
#                     road[0], road[1] = road[1], road[0]
#
#         for road in roads:
#             if road[0] == node:
#                 backtracking(road[1], weight + road[2])
#
#         if flag == 1:
#             for road in roads:  # 방향을 다시 바꿔준다.
#                 if road[0] == node or road[1] == node:
#                     road[0], road[1] = road[1], road[0]
#     answer = 0
#     backtracking(start, 0)
#
#     return answer
#
# print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))



















# 미로 탈출
# def solution(n, start, end, roads, traps):
#     def backtracking(node, weight, graphs):
#         if node == end:
#             return weight
#
#         for graph in graphs:
#             if graph[0] == node:
#                 next_node = graph[1]
#                 next_weight = graph[2]
#                 if next_node in traps:
#                     for graph in graphs:  # 방향을 바꿔준다.
#                         if graph[0] == next_node or graph[1] == next_node:
#                             graph[0], graph[1] = graph[1], graph[0]
#                 backtracking(next_node, weight+next_weight, graphs)
#                 if next_node in traps:
#                     for graph in graphs:  # 다시 방향을 바꿔준다.
#                         if graph[0] == next_node or graph[1] == next_node:
#                             graph[0], graph[1] = graph[1], graph[0]
#
#     answer = 0
#     print(backtracking(start, 0, roads))
#
#     return answer
#
# solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])






# from collections import deque
# def solution(n, start, end, roads, traps):
#     answer = 0
#     q = deque()
#     q.append((start, 0, roads))
#     while q:
#         print(q)
#         node, weight, graphs = q.popleft()
#         if node == end:
#             answer = weight
#             break
#
#         for graph in graphs:
#             if graph[0] == node:
#                 next_node = graph[1]
#                 next_weight = graph[2]
#                 if next_node in traps:
#                     for graph in graphs:
#                         if graph[0] == next_node or graph[1] == next_node:
#                             graph[0], graph[1] = graph[1], graph[0]
#                     copy_graph = []
#                     for graph in graphs:
#                         copy_graph.append(graph[::])
#                     q.append((next_node, weight + next_weight, copy_graph))
#                     for graph in graphs:
#                         if graph[0] == next_node or graph[1] == next_node:
#                             graph[0], graph[1] = graph[1], graph[0]
#     return answer
#
# print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))






















# 주식
# def solution(code, day, data):
#     answer = []
#     result = []
#     for d in data:
#         info = d.split()
#         if info[1][5:] == code:
#             if info[2][5:13] == day:
#                 price = int(info[0][6:])
#                 hour = int(info[2][13:])
#                 result.append((hour, price))
#     result.sort()
#     for r in result:
#         answer.append(r[1])
#     return answer

# solution("012345", "20190620", ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"])


# 스키장
def solution(t, r):
    answer = []
    # 탑승시각, 손님의 번호, 티켓등급을 같이 나타내는 리스트 만들기
    pair_t = []

    for val in t:
        pair_t.append([val])
    for idx, level in enumerate(r):
        pair_t[idx].extend([level, idx])

    # 같은 시각에 온 손님이 없을 때
    if len(t) == len(set(t)):
        pair_t.sort()
        for p in pair_t:
            answer.append(p[2])

    else:
        while True:
            pair_t.sort(key=lambda x:(x[0],x[1]))
            order = pair_t.pop(0)
            answer.append(order[2])
            for lis in pair_t:
                if lis[0] == order[0]:
                    lis[0] += 1
            if not pair_t:
                break

    return answer

print(solution([0,1,3,0], [0,1,2,3]))

# print(solution([7,6,8,1], [0,1,2,3]))



#




