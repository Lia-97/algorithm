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
# def solution(t, r):
#     answer = []
#     # 탑승시각, 손님의 번호, 티켓등급을 같이 나타내는 리스트 만들기
#     pair_t = []
#
#     for val in t:
#         pair_t.append([val])
#     for idx, level in enumerate(r):
#         pair_t[idx].extend([level, idx])
#
#     # 같은 시각에 온 손님이 없을 때
#     if len(t) == len(set(t)):
#         pair_t.sort()
#         for p in pair_t:
#             answer.append(p[2])
#
#     else:
#         while True:
#             pair_t.sort(key=lambda x:(x[0],x[1]))
#             order = pair_t.pop(0)
#             answer.append(order[2])
#             for lis in pair_t:
#                 if lis[0] == order[0]:
#                     lis[0] += 1
#             if not pair_t:
#                 break
#
#     return answer
#
# print(solution([0,1,3,0], [0,1,2,3]))

# print(solution([7,6,8,1], [0,1,2,3]))


# 월간코드챌린지(5월)

# 1
# def solution(left, right):
#     answer = 0
#     for num in range(left, right+1):
#         cnt = 0
#         for i in range(1, num+1):
#             if num % i == 0:
#                 cnt += 1
#         if cnt % 2 == 0:
#             answer += num
#         else:
#             answer -= num
#     return answer
#
# print(solution(13, 17))

# 2 _ 실패
# def solution(numbers):
#     answer = []
#
#     def make_bit(x):
#         ans = ''
#         while True:
#             if x == 1:
#                 ans = '1' + ans
#                 break
#             ans = str(x % 2) + ans
#             x = x // 2
#
#         if len(ans) < 16:
#             ans = '0' * (16 - len(ans)) + ans
#
#         return ans
#
#     def check_diff(num):
#         origin = make_bit(num)
#         start = num+1
#         while True:
#             total = 0
#             changed_start = make_bit(start)
#             for i in range(16):
#                 if changed_start[i] != origin[i]:
#                     total += 1
#             if total <= 2:
#                 return start
#             start += 1
#
#     for num in numbers:
#         answer.append(check_diff(num))
#
#     return answer

# 2 _ 실패
# def solution(numbers):
#     answer = []
#
#     def make_binary(val):
#         ans = []
#         while True:
#             if val == 1:
#                 ans.append(1)
#                 break
#             ans.append(val % 2)
#             val //= 2
#         return ans
#
#     def find_ans(num):
#         bit = make_binary(num)
#         for idx in range(len(bit)):
#             if bit[idx] == 0:
#                 for i in range(idx-1, -1, -1):
#                     if bit[i] == 1:
#                         bit[i] = 0
#                         bit[idx] = 1
#                         return bit
#                 bit[idx] = 1
#                 return bit
#         bit[-1] = 0
#         bit.append(1)
#         return bit
#
#     for num in numbers:
#         sub_ans = 0
#         lis = find_ans(num)
#         for i in range(len(lis)):
#             sub_ans += lis[i]*(2**i)
#         answer.append(sub_ans)
#     return answer
#
# print(solution([2,7]))

# 2
# def solution(numbers):
#     answer = []
#     def binary(num):
#         ans = ''
#         for _ in range(15):
#             if num == 1:
#                 ans = '1' + ans
#                 num = 0
#             elif num == 0:
#                 ans = '0' + ans
#             else:
#                 ans = str(num % 2) + ans
#                 num //= 2
#         return ans
#
#     def get_ans(num):
#         origin = binary(num)
#         for n in range(num+1, num+11):
#             total = 0
#             for i in range(15):
#                 if origin[i] != binary(n)[i]:
#                     total += 1
#             if total <= 2:
#                 answer.append(n)
#                 return
#
#     for num in numbers:
#         get_ans(num)
#
#     return answer
#
# print(solution([2,7]))

# 인터파크 1
# def solution(grade):
#     N = len(grade)
#     answer = [0]*N # answer을 0으로 초기화한다.
#
#     # 중복되는 점수를 제거하고, 역순으로 정렬한다. (가장 큰 점수부터 순서대로)
#     grade_set = sorted(list(set(grade)))
#
#     cnt = 0 # 자신보다 높은 점수의 학생 수
#     for idx in range(len(grade_set)-1,-1,-1): # 가장 높은 점수 부터 차례대로 확인해보자
#         changed_cnt = 0 # 해당 점수를 가진 학생의 수를 changed_cnt 라는 변수에 저장한다.
#         for i in range(N): # grade를 순회하면서
#             if grade[i] == grade_set[idx]: # grade_set의 각 원소와 값이 같다면
#                 answer[i] = cnt+1 # answer 리스트의 i 인덱스 자리에 자신보다 높은 점수의 학생 수+1을 대입한다.
#                 changed_cnt += 1 # 해당 점수를 가진 학생의 수를 추가한 후,
#         cnt += changed_cnt # 현재까지의 학생 수에 change_cnt 를 대입한다.
#
#     return answer
#
# solution([2, 2, 1])

# 인터파크 1
# from collections import Counter, defaultdict
# def solution(grade):
#     answer = []
#     # 각 점수에 해당하는 사람들이 몇명인지 구하고, 점수가 큰 순으로 정렬한다
#     grade_dict = Counter(grade)
#     grade_dict = sorted(grade_dict.items(), key=lambda x: -x[0] )
#
#     # 사람 수의 누적합을 구해, 각 점수에 해당한다면 몇 등인지 구한다
#     grade_chart = defaultdict(int)
#     rank = 1
#     for grades in grade_dict:
#         grade_chart[grades[0]] = rank
#         rank += grades[1]
#
#     # grade를 순회하면서 해당 점수가 key일때, value 값을 answer에 더한다.
#     for g in grade:
#         answer.append(grade_chart[g])
#
#     return answer
# #
# # print(solution([2, 2, 1]))

# 인터파크 2
# from collections import defaultdict, deque
# def solution(N, relation):
#     def bfs(q):
#         ans = 0 # 본인은 친구의 수에 포함되지 않으므로 ans를 0으로 초기화
#         while q:
#             node, cnt = q.popleft()
#             if cnt == 2: # 이미 2단계를 거쳐서 친구인지 확인했다면 break
#                 break
#             for idx in graph[node]:
#                 if used[idx] == 0: # 방문 안한 노드라면
#                     used[idx] = 1 # 방문 처리를 해주고
#                     q.append((idx, cnt+1)) # 다음 노드 idx, 한 단계를 거쳤으므로 cnt+1
#                     ans += 1 # 친구 수에 +1
#         return ans
#
#     answer = []
#
#     # 딕셔너리 형태의 그래프를 만든다.
#     graph = defaultdict(list)
#     for rel in relation:
#         graph[rel[0]].append(rel[1])
#         graph[rel[1]].append(rel[0])
#
#     # 1번 부터 N번까지 노드를 순회하면서, 친구의 수를 센다.
#     for n in range(1, N+1):
#         q = deque()
#         used = [0]*(N+1)
#         q.append((n, 0)) # 시작노드, 몇 단계 걸쳐 친구인지 나타내는 숫자 0
#         used[n] = 1
#         answer.append(bfs(q))
#
#     return answer
#
# print(solution(5, [[1,2],[4,2],[3,1],[4,5]]))



























# 1
# N, k = map(int, input().split())
# foods = list(map(int, input().split()))
# ans = []
# while True:
#     for i in range(k-1, N+k-1):
#         if foods[i%N] != 0:
#             foods[i%N] -= 1
#             if foods[i%N] == 0:
#                 if (i%N + 1) not in ans:
#                     ans.append(i%N + 1)
#
#     if sum(foods) == 0:
#         break
#
# print(' '.join(list(map(str, ans))))

# 2
# from collections import deque
#
# def bfs(q):
#     while q:
#         x, y, i, j, cnt = q.popleft()
#         for d in dir:
#             nx, ny, ni, nj = x+d[0], y+d[0], i+d[0], j+d[0]
#             if (0 <= nx < N and 0 <= ny < N) or (0 <= ni < N and 0 <= nj < N):
#
#
# N = int(input())
# board = [input() for _ in range(N)]
# x1, y1, x2, y2 = map(int, input().split())
# visited = [[0]*N for _ in range(N)]
# dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
# q = deque()
# visited[x1][y1] = 1
# q.append((x1, y1, x2, y2, 0))
# bfs(q)

















