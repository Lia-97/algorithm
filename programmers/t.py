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

####### 올리브영 경력직 (21.08.15) ##########
# 1
# def solution(x, y, r, v):
#     answer = 0
#     rec_info = [100000,0,100000,0] # 직사각형의 꼭짓점 (x1, x2, y1, y2)
#
#     for i in range(len(x)):
#         if x[i]-r[i] <= rec_info[0]:
#             rec_info[0] = x[i]-r[i]
#         if x[i]+r[i] >= rec_info[1]:
#             rec_info[1] = x[i]+r[i]
#         if y[i]-r[i] <= rec_info[0]:
#             rec_info[2] = y[i]-r[i]
#         if y[i]+r[i] >= rec_info[0]:
#             rec_info[3] = y[i]+r[i]
#
#     ran_points = [] # 난수를 점으로 생성한 좌표
#
#     # v 리스트의 숫자
#     for i in range(len(v) // 2):
#         a = rec_info[0] + (2*i)%(rec_info[1]-rec_info[0])
#         b = rec_info[2]+ (2*i + 1)%(rec_info[3]-rec_info[2])
#         ran_points.append((a,b))
#
#     in_round_cnt = 0 # 원 안에 있는 점의 개수
#
#     # 원 내부에 있는지 판별
#     for m in ran_points:
#         for n in range(len(x)):
#             if r[n] ** 2 >= (x[n]- m[0]) ** 2 + (y[n] - m[1]) ** 2:
#                 in_round_cnt += 1
#                 print(m[0], m[1])
#                 break
#
#     # 원의 면적 계산
#     answer = (in_round_cnt / len(ran_points)) * (rec_info[1]-rec_info[0]) * (rec_info[3] - rec_info[2])
#
#     return answer
#
# print(solution([5], [5], [5], [92, 83, 14, 45, 66, 37, 28, 9, 10, 81])) # 80
# print(solution([3, 4], [3, 5], [2, 3], [12, 83, 54, 35, 686, 337, 258, 95, 170, 831, 8, 15])) # 28

# 2
# def solution(subway, start, end):
#     answer = 0
#     line = 0
#     N = len(subway)
#     SUBWAY = []
#
#     # subway를 int 타입으로 변환
#     for sub in subway:
#         SUBWAY.append(list(map(int, sub.split())))
#
#     # 출발지가 몇호선에 있는지 확인
#     for n in range(len(SUBWAY)):
#         if start in SUBWAY[n]:
#             line = n
#
#     ans_list = []
#     def f(end, line, cnt, visited_line, visited_station):
#         for i in SUBWAY[line]:
#             if i == end:
#                 ans_list.append(cnt)
#                 return
#             elif i != end and visited_station[i] == 0:
#                 for j in range(len(visited_line)):
#                     if visited_line[j] == 0:
#                         if i in SUBWAY[j]:
#                             visited_line[j] = 1
#                             visited_station[i] = 1
#                             f(end, j, cnt+1, visited_line, visited_station)
#                         visited_line[j] = 0
#                         visited_station[i] = 0
#
#     # dfs 호출
#     visited_line = [0] * N  # 방문한 노선
#     visited_station = [0] * 200001 # 방문한 역
#     visited_line[line] = 1 # 출발지가 있는 노선은 방문 처리
#     visited_station[start] = 1 # 출발역은 방문처리
#     f(end, line, 0, visited_line, visited_station)
#
#     answer = min(ans_list)
#
#     return answer
#
# solution(["1 2 3 4 5 6 7 8","2 11","0 11 10","3 17 19 12 13 9 14 15 10","20 2 21"], 1, 9) # 1
# solution(["1 2 3 4 5 6 7 8 9 10","2 8"], 1, 10) # 0
# solution(["0 1 2 3 4","1 12 13 14"], 2, 12) # 1



#########  그렙 인턴 ###########
# 1
# def solution(arr):
#     new_arr = sorted(list(set(arr)))
#     if len(new_arr) == 1:
#         answer = 0
#     else:
#         answer = new_arr[(len(new_arr) // 2)-1] + 1
#         print(new_arr)
#
#     return answer
#
# print(solution([1, 1, 1, 1, 1, 5, 7, 10, 10]))

# 2
# def solution(card_numbers):
#     answer = []
#
#     for l in card_numbers:
#         if len(l) != 19 and len(l) != 16:
#             answer.append(0)
#         else:
#             lis = l.split('-')
#             for card in lis:
#                 if len(card) != 4:
#                     answer.append(0)
#                     break
#             nums = ''.join(lis)
#             N = len(nums)
#             number = nums[::-1]
#             first_ans = 0
#             second_ans = 0
#             for i in range(N):
#                 print(i, number[i])
#                 if i%2: # 홀수일때, 여기서는 짝수자리수를 의미
#                     check = int(number[i])*2
#                     if check >= 10:
#                         first_ans += (check // 10) + (check %10)
#                     else:
#                         first_ans += check
#                     print('(1)', first_ans)
#                 else:
#                     second_ans += int(number[i])
#                     print('(2)', second_ans)
#             print('__________________')
#             if (first_ans + second_ans) % 10 == 0:
#                 answer.append(1)
#             else:
#                 answer.append(0)
#
#     return answer
#
# print(solution(["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453", "328537649934245", "3285376499342459", "3285-3764-9934-2452"]))



######## 월코챌 시즌3 (9월) ##########
# 1
# def solution(numbers):
#     answer = sum(range(0, 10))-sum(numbers)
#     return answer

# 2
# def f(grid, x, y, l, cnt):
#     global arr_answer, cnt_answer, visited
#
#     moving = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
#     if x + moving[l][0] >= 0 and y + moving[l][1] >= 0:
#         next_x, next_y = (x + moving[l][0])%len(grid), (y + moving[l][1])%len(grid[0])
#     elif x + moving[l][0] >= 0 and y + moving[l][1] < 0:
#         next_x, next_y = (x + moving[l][0]) % len(grid), len(grid[0])-1
#     elif x + moving[l][0] < 0 and y + moving[l][1] >= 0:
#         next_x, next_y = len(grid)-1, (y + moving[l][1])%len(grid[0])
#     else:
#         next_x, next_y = len(grid) - 1, len(grid[0])-1
#
#     dir = grid[next_x][next_y]
#
#     # 앞으로 갈 방향 설정
#     if (l == 0 and dir == "L") or (l == 1 and dir == "R"):
#         l = 2
#     elif (l == 0 and dir == "R") or (l == 1 and dir == "L"):
#         l = 3
#     elif (l == 2 and dir == "L") or (l == 3 and dir == "R"):
#         l = 1
#     elif (l == 2 and dir == "R") or (l == 3 and dir == "L"):
#         l = 0
#     else:
#         pass
#
#     if visited[next_x][next_y][l] == 0:
#         visited[next_x][next_y][l] = 1
#         f(grid, next_x, next_y, l, cnt+1)
#     else:
#         print("???", visited, arr_answer)
#         if visited not in arr_answer:
#             arr_answer.append(visited)
#             cnt_answer.append(cnt)
#
# arr_answer = []
# cnt_answer = []
#
# def solution(grid):
#     global arr_answer, cnt_answer, visited
#
#     N = len(grid)
#     M = len(grid[0])
#     visited = []
#     for _ in range(N):
#         visited.append([[0, 0, 0, 0] for _ in range(M)])
#
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             for l in range(4): # 시작하는 방향(상하좌우)
#                 visited[i][j][l] = 1
#                 f(grid, i, j, l, 1)
#
#     cnt_answer.sort()
#     return cnt_answer
#
# print(solution(["S"]))



######## 라인 코테 #########
# 1
# def solution(student, k):
#     answer = 0
#     N = len(student)
#     for i in range(N):
#         for j in range(i+k, N+1):
#             if student[i:j].count(1) == k:
#                 answer += 1
#     return answer
#
# print(solution([0,1,0,0], 1))

# 2
# def solution(research, n, k):
#     answer = ''
#     all_keywords = ""
#
#     # 검색 기간 동안 등장한 모든 키워드 파악
#     for r in research:
#         all_keywords += r
#
#     unique_keywords = sorted(list(set(all_keywords)))
#
#     # 검색어 추출 기간
#     N = len(research)
#
#     # 검색어 현황 파악할 수 있는 테이블 생성
#     table = []
#     for _ in range(len(unique_keywords)):
#         table.append([0]*N)
#
#     # 검색어가 등장한 수만큼 일자별로 테이블에 추가
#     for i in range(len(unique_keywords)):
#         for j in range(N):
#             table[i][j] += research[j].count(unique_keywords[i])
#
#     # 이슈 검색어가 된 날의 수
#     issue_day = [0]*len(unique_keywords)
#
#     # 기준에 만족하는 검색어 조사
#     for t in range(len(unique_keywords)):
#         for x in range(N-n+1):
#             period = table[t][x:x+n]
#             flag = False
#             if sum(period) >= 2*n*k:
#                 for p in period:
#                     if p >= k:
#                         flag = True
#                     else:
#                         flag = False
#                         break
#             if flag:
#                 issue_day[t] += 1
#
#     print(table)
#     print(issue_day)
#
#     # 결과
#     max_value = 0
#     for cnt in range(len(issue_day)):
#         if issue_day[cnt] > max_value:
#             answer = unique_keywords[cnt]
#             max_value = issue_day[cnt]
#
#     if answer == '':
#         answer = "None"
#
#
#     return answer
#
# print(solution(["abaaaa","aaa","abaaaaaa","fzfffffffa"], 2, 2))
# print(solution(["yxxy","xxyyy"], 2, 1))
# print(solution(["yxxy","xxyyy","yz"], 2, 1))
# print(solution(["xy","xy"], 1, 1))

# 3
# def solution(jobs):
#     copied_jobs = []
#
#     for job in jobs:
#         copied_jobs.append(job)
#
#     answer = []
#     answer.append(jobs[0][2])
#     time = jobs[0][0] + jobs[0][1] # 현재 시각
#     part = jobs[0][2]
#
#     # answer 목록에 들어갔으면 jobs 에서 삭제
#     jobs.remove(jobs[0])
#
#     next_list = []  # 앞선 작업을 처리하는 동안 쌓인 작업 목록
#     for job in copied_jobs:
#         if job[0] <= time and job in jobs:
#             next_list.append(job)  # 쌓인 작업 목록에 넣고
#             jobs.remove(job)  # 기존의 작업목록에서 삭제
#
#     while jobs or next_list:
#         if jobs and not next_list:  # 일은 남았지만 쌓인 작업이 없으면
#             next_list.append(jobs[0])
#         for job in copied_jobs:
#             if job[0] <= time and job in jobs:
#                 next_list.append(job) # 쌓인 작업 목록에 넣고
#                 jobs.remove(job) # 기존의 작업목록에서 삭제
#
#         importance = [0]*102 # 각 분류번호 별 중요도
#
#         flag = True
#
#         for next in next_list:
#             if next[2] == part:
#                 time += next[1]
#                 next_list.remove(next) # 쌓인 작업 목록에서 삭제
#                 flag = False
#                 break
#             else:
#                 importance[next[2]] += next[3] # 각 분류번호에 중요도를 더함
#         if flag:
#             max_importance = 0
#             next_part = 0
#             for im in range(len(importance)):
#                 if importance[im] > max_importance:
#                     max_importance = importance[im]
#                     next_part = im
#             part = next_part
#             answer.append(part)
#             for next in next_list:
#                 if next[2] == part:
#                     time += next[1]
#                     next_list.remove(next)
#
#     return answer
#
# print(solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))
# print(solution([[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]]))

# 5
