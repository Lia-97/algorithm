# 준환이의 운동관리
# T = int(input())
# result = 0
# for tc in range(1, T+1):
#     L, U, X = map(int, input().split())
#     if X > U:
#         result = -1
#     else:
#         if X < L:
#             result = L - X
#         else:
#             result = 0
#     print(f'#{tc} {result}')

# [S/W 문제해결 기본] 4일차 - 거듭 제곱
# for tc in range(1, 11):
#     int(input())
#     N, M = map(int, input().split())
#     ans = N ** M
#     print(f'#{tc} {ans}')

# 모음이 보이지 않는 사람
# T = int(input())
# vowel = ['a', 'e', 'i', 'o', 'u']
# for tc in range(1, T+1):
#     words = input()
#     for v in vowel:
#         if v in words:
#             words = words.replace(v, '')
#     print(f'#{tc} {words}')

# [S/W 문제해결 기본] 3일차 - 회문1
# for tc in range(1, 11):
#     long = int(input())
#     square = []
#     result = []
#     for i in range(8):
#         abc = list(input())
#         square.append(abc)
#         for j in range(8-long+1):
#             origin = abc[j:j+long]
#             reverse = origin[::-1]
#             if origin == reverse:
#                 result.append(origin)
#
#     for m in range(8):
#         vertical = []
#         for l in square:
#             vertical.append(l[m])
#         for n in range(8-long+1):
#             vertical_origin = vertical[n:n+long]
#             vertical_reverse = vertical_origin[::-1]
#             if vertical_origin == vertical_reverse:
#                 result.append(vertical_origin)
#
#     print(f'#{tc} {len(result)}')

# [S/W 문제해결 기본] 3일차 - 회문1 (함수 만들어서 풀어보기)

# def test(long, abc, result):
#     for i in range(8-long+1):
#         origin = abc[i:i+long]
#         reverse = origin [::-1]
#         if origin == reverse:
#             result.append(origin)
#
# for tc in range(1, 11):
#     long = int(input())
#     square = []
#     result = []
#     for i in range(8):
#         abc = list(input())
#         square.append(abc)
#         test(long, abc, result)
#
#     for m in range(8):
#         vertical = []
#         for l in square:
#             vertical.append(l[m])
#         test(long, vertical, result)
#
#     print(f'#{tc} {len(result)}')

# [S/W 문제해결 기본] 3일차 - 회문1 (전치 행렬)
# def check(word):
#     global ans
#     for i in range(8-length+1):
#         origin=word[i:i+length]
#         reverse=origin[::-1]
#         if origin == reverse:
#             ans+=1
#
# T=10
# for tc in range(1,T+1):
#     length=int(input())
#     board=[]
#     ans=0
#
#     for _ in range(8):
#         board.append(input())
#     # 전치 행렬
#     T_board=list(zip(*board))
#
#     for i in range(8):
#         check(board[i])
#         check(T_board[i])
#
#     print(f'#{tc} {ans}')

# 원재의 메모리 복구하기
# T = int(input())
# for tc in range(1, T+1):
#     memory = input()
#     cnt = 0
#     if memory[0] == '1':
#         cnt += 1
#     for i in range(1, len(memory)):
#         if memory[i] != memory[i-1]:
#             cnt += 1
#     print(f'#{tc} {cnt}')

# 원재의 메모리 복구하기 _ 원재의 솔루션
#
# T=int(input())
# for tc in range(1,T+1):
#     # 맨 앞자리 수를 판별하기 위해 if 문을 쓸 필요가 없어짐
#     bit='0'+input()
#     cnt=0
#     for i in range(1,len(bit)):
#         if bit[i] != bit[i-1]:
#             cnt+=1
#     print(f'#{tc} {cnt}')

# [S/W 문제해결 기본] 7일차 - 암호생성기
# for tc in range(1, 11):
#     input()
#     numbers = list(map(int, input().split()))
#     while numbers[-1] > 0:
#         for i in range(1, 6):
#             move = numbers.pop(0)
#             if move - i > 0:
#                 numbers.append(move-i)
#             else:
#                 numbers.append(0)
#                 break
#     result = ' '.join(map(str,numbers))
#     print(f'#{tc} {result}')

# 소득 불균형
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     total = 0
#     long = 0
#     for number in numbers:
#         total += number
#         long += 1
#     avg = total / long
#     cnt = 0
#     for number in numbers:
#         if number <= avg:
#             cnt += 1
#     print('#{} {}'.format(tc, cnt))

# [Professional] 쥬스 나누기
# T= int(input())
# for tc in range(1, T+1):
#     N = input()
#     print(f'#{tc}', end=' ')
#     print(('1/'+N+' ') * int(N))

# [S/W 문제해결 기본] 3일차 - String
# for tc in range(1, 11):
#     input()
#     search = input()
#     sentence = input()
#     cnt = 0
#     for i in range(len(sentence)-len(search)+1):
#         if sentence[i:i+len(search)] == search:
#             cnt += 1
#     print(f'#{tc} {cnt}')

# 제곱 팰린드롬 수
# T = int(input())
# for tc in range(1, T+1):
#     A, B = map(int, input().split())
#     cnt = 0
#     for num in range(A, B+1):
#         if str(num) == str(num)[::-1]:
#             root = num ** (1/2)
#             if root % 1 == 0:
#                 if str(int(root)) == str(int(root))[::-1]:
#                     cnt += 1
#     print(f'#{tc} {cnt}')

# [S/W 문제해결 기본] 10일차 - 비밀번호
# for tc in range(1, 11):
#     long, words = input().split()
#     words_list = list(words)
#     result = [-1]
#     while len(words_list) != 0:
#         last = words_list.pop()
#         if last != result[-1]:
#             result.append(last)
#         else:
#             result.pop()
#     result = result[::-1]
#     result = result[:len(result)-1]
#
#     ans = ''.join(list(map(str, result)))
#     print(f'#{tc} {ans}')

# 농작물 수확하기
# def sum_v(lis):
#     total = 0
#     for l in lis:
#         total += l
#     return total
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = []
#     for _ in range(N):
#         arr.append(list(map(int, input())))
#
#     total = 0
#     for i in range(N):
#         total += sum_v(arr[i][abs(N//2-i) : N-abs(N//2-i)])
#     print(f'#{tc} {total}')

# 보충학습과 평균
# T = int(input())
# for tc in range(1, T+1):
#     score = list(map(int, input().split()))
#     for i in range(len(score)):
#         if score[i] < 40:
#             score[i] = 40
#     print(f'#{tc} {int(sum(score)/len(score))}')

# 직사각형 길이 찾기
# T = int(input())
# for tc in range(1, T+1):
#     lis = list(map(int, input().split()))
#     s_lis = set(lis)
#     ans = 0
#
#     if len(s_lis) == 1:
#         ans = s_lis.pop()
#     else:
#         if lis.count(max(lis)) == 2:
#             s_lis.remove(max(lis))
#             ans = s_lis.pop()
#         else:
#             ans = max(lis)
#     print(f'#{tc} {ans}')

# 민석이의 과제 체크하기
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     submit = list(map(int, input().split()))
#     student = []
#     for i in range(1, N+1):
#         student.append(i)
#     answer = list(set(student) - set(submit))
#     answer = ' '.join(map(str, answer))
#
#     print(f'#{tc} {answer}')

# 홀수일까 짝수일까
# T = int(input())
# for tc in range(1, T+1):
#     num = int(input())
#     ans = 'Even'
#     if num % 2:
#         ans = 'Odd'
#     print(f'#{tc} {ans}')

# 최대 성적표 만들기 _ 부분집합으로 풀었더니 제한시간 초과가 뜸
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     scores = list(map(int, input().split()))
#     result = []
#
#     for i in range(1 << N):
#         sub = []
#         for j in range(N):
#             if i & (1 << j):
#                 sub.append(scores[j])
#
#         if len(sub) == K:
#             result.append(sub)
#
#     max_score = 0
#     for i in result:
#         if sum(i) > max_score:
#             max_score = sum(i)
#     print('#{} {}'.format(tc, max_score))

# 무한 사전
# T = int(input())
# for tc in range(1, T+1):
#     first = input().rstrip()
#     second = input().rstrip()
#     if second == first+'a':
#         ans = 'N'
#     else:
#         ans = 'Y'
#     print(f'#{tc} {ans}')

# 최장 경로 _ 실패(dfs)
# def dfs(node, cnt):
#     global ans
#     visited[node] = 1
#     ans = max(ans, cnt)
#     for n in graph[node]:
#         if visited[n] == 0:
#             dfs(n, cnt+1)
#
# from collections import defaultdict
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # 노드개수, 간선정보 개수
#     graph = defaultdict(list)
#     nodes = []
#     for _ in range(M):
#         node1, node2 = map(int, input().split())
#         graph[node1].append(node2)
#         graph[node2].append(node1)
#
#     ans = 0
#     for keys in graph:
#         visited = [0] * (N + 1)
#         if visited[keys] == 0:
#             dfs(keys, 1)
#
#     print(f'#{tc} {ans}')

# 최장 경로 _ 실패(bfs)
# from collections import defaultdict
# from collections import deque
#
# def bfs(q):
#     global max_cnt
#     while q:
#         node, cnt = q.popleft()
#         for n in nodes[node]:
#             if visited[n] == 0:
#                 visited[n] = 1
#                 q.append((n, cnt+1))
#         if cnt > max_cnt:
#             max_cnt = cnt
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # N개 정점, M개 간선
#     nodes = defaultdict(list)
#     q = deque()
#     max_cnt = 1
#
#     for _ in range(M):
#         node1, node2 = map(int, input().split()) # 노드 관계
#         nodes[node1].append(node2)
#         nodes[node2].append(node1)
#
#     min_length = 21
#     for node in nodes:
#         visited = [0] * (N + 1)
#         if len(nodes[node]) < min_length:
#             min_length = len(nodes[node])
#             q.clear()
#             q.append((node, 1))
#             visited[node] = 1
#
#     bfs(q)
#     print(f'#{tc} {max_cnt}')

# 최장 경로 _ dfs로 다시 풀기
# from collections import defaultdict
#
# def dfs(node, cnt):
#     global ans
#     cnt += 1
#     visited[node] = 1
#     if cnt > ans:
#         ans = cnt
#     for n in graph[node]:
#         if visited[n] == 0:
#             dfs(n, cnt)
#     visited[node] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # N개의 정점, M개의 간선
#     graph = defaultdict(list)
#     ans = 0
#     visited = [0] * (N + 1)
#
#     for _ in range(M):
#         node1, node2 = map(int, input().split())
#         graph[node1].append(node2)
#         graph[node2].append(node1)
#
#     for node in graph:
#         dfs(node, 0)
#
#     print(f'#{tc} {ans}')

# D3 2814 최장경로
# def dfs(idx, ans):
#     global answer
#     # 탐색한 노드는 체크하고
#     visited[idx] = 0
#     # 이동횟수 증가
#     ans += 1
#     # 최댓값 갱신
#     if answer < ans: answer = ans
#     # 이동가능 노드 확인
#     for i in graph[idx]:
#         # 이동가능하면 이동
#         if visited[i]: dfs(i, ans)
#     # 사용 해제
#     visited[idx] = 1
#
#
# for t in range(1, int(input()) + 1):
#     # 노드와 간선 정보를 받고
#     N, M = map(int, input().split())
#     # 방문 배열 만들고
#     visited = [1 for _ in range(N + 1)]
#     # 입력받아서
#     temp = [list(map(int, input().split())) for _ in range(M)]
#     # 쉽게 사용하기위한 데이터 편집하기
#     graph = [[] for _ in range(N + 1)]
#     answer = 0
#     # 노드간 이동 경로 표시
#     for a, b, in temp:
#         graph[a].append(b)
#         graph[b].append(a)
#     print(graph)
#     # 시작노드를 다르게해서 최대 길이 찾기
#     for i in range(N): dfs(i, 0)
#     print('#{} {}'.format(t, answer))

# 부분 수열의 합 _ combinations
# from itertools import combinations
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split()) # 원소 개수, 합이 K
#     nums = list(map(int, input().split()))
#     nums.sort()
#     ans = 0
#     search = nums[::]
#
#     for idx in range(N):
#         if nums[idx] > K:
#             search = nums[:idx]
#             break
#
#     for i in range(1, N+1):
#         lis = list(combinations(search, i))
#         for l in lis:
#             if sum(l) ==  K:
#                 ans += 1
#     print(f'#{tc} {ans}')

# 재미있는 오셀로 게임 _ 문제 이해가 아직도 안됨;;
# T = int(input())
# for _ in range(1, T+1):
#     N, M = map(int, input().split()) # 한변의 길이 N, 돌을 놓는 횟수 M
#     board = [[0]*N for _ in range(N)]
#     dir = [(-2,0),(2,0),(0,-2),(0,2),(-2,-2),(-2,2),(2,-2),(2,2)] # 좌상,우상,좌하,우하 대각선
#     change_dir = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)] # 상하좌우
#     a = N//2 - 1
#     b = N//2
#     board[a][a], board[b][b] = 1, 1 # 백돌
#     board[a][b], board[b][a] = 2, 2 # 흑돌
#     for _ in range(M):
#         i, j, color = map(int, input().split()) # x좌표, y좌표, 놓을 돌 색깔
#         x, y = i-1, j-1
#         board[x][y] = color
#         for k in range(8):
#             nx, ny = x+dir[k][0], y+dir[k][1]
#             cx, cy = x + change_dir[k][0], y + change_dir[k][1]
#             if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 0:
#                 print('1')
#                 print(x, y)
#                 print('nx,ny', nx, ny)
#                 print('cx,cy', cx, cy)
#                 print('color', color)
#                 if board[nx][ny] == color:
#                     print('2')
#                     if board[cx][cy] != 0 and board[cx][cy] != color:
#                         print('3')
#                         board[cx][cy] = color
#                         break
#     print(board)

# 최소합 _ 완전 검색으로 풀기
# def dfs(x, y, total):
#     global min_total
#     if total > min_total:
#         return
#
#     if x == n-1 and y == n-1:
#         if total < min_total:
#             min_total = total
#         return
#
#     for d in dir:
#         nx, ny = x + d[0], y + d[1]
#         if 0 <= nx < n and 0 <= ny < n:
#                 dfs(nx, ny, total+int(board[nx][ny]))
#
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     board = [input().split() for _ in range(n)]
#     dir = [(0,1),(1,0)]
#     min_total = 16900
#     dfs(0,0,int(board[0][0]))
#     print(f'#{tc} {min_total}')

# 최소합 _ 최단경로 이용해서 풀기
# from collections import deque
# def navigate(q):
#     while q:
#         x, y = q.popleft()
#         for d in dir:
#             nx, ny = x+d[0], y+d[1]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if weight[x][y]+road[nx][ny] < weight[nx][ny]:
#                     weight[nx][ny] = weight[x][y]+road[nx][ny]
#                     q.append((nx, ny))
#
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     road = [list(map(int, input().split())) for _ in range(n)]
#     # 비용 초기화
#     weight = [[float('inf')]*n for _ in range(n)]
#     weight[0][0] = road[0][0]
#     dir = [(1,0),(0,1)] # 하, 우
#     q = deque()
#     q.append((0,0))
#     navigate(q)
#     print(f'#{tc} {weight[n - 1][n - 1]}')

# 전자카트
# def dfs(row):
#     global min_energy, energy
#
#     if energy < min_energy:
#         visited[row] = 1
#
#         if 0 not in visited:
#             energy += int(office[row][0])
#             if energy < min_energy:
#                 min_energy = energy
#             energy -= int(office[row][0])
#
#     for j in range(n): # 방문할 열
#         if row == j:
#             continue
#         else:
#             if visited[j] == 0:
#                 energy += int(office[row][j])
#                 visited[j] = 1
#                 dfs(j)
#                 energy -= int(office[row][j])
#     visited[row] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     office = [input().split() for _ in range(n)]
#     visited = [0]*n
#     min_energy = 100000
#     energy = 0
#     dfs(0)
#     print(f'#{tc} {min_energy}')

# 전자카트 _ 원재의 솔루션
# def patrol(node,battery,cnt):
#     global ans
#     if ans < battery:
#         return
#
#     if cnt== N:
#         ans=min(ans,battery+cart[node][0])
#         return
#
#     for next_node,cost in enumerate(cart[node]):
#         if visited[next_node] ==0:
#             visited[next_node]=1
#             patrol(next_node,battery+cost,cnt+1)
#             visited[next_node]=0
#
# T=int(input())
# for tc in range(1,T+1):
#     N=int(input())
#     visited=[0]*N
#     cart=[list(map(int,input().split())) for _ in range(N)]
#     ans=10000
#     visited[0]=1
#     patrol(0,0,1)
#     print(f'#{tc} {ans}')

# 화물 도크 _ 시간 초과
# def freight(schedules, start, cnt):
#     global sub
#     for idx in range(len(schedules)):
#         if schedules[idx][0] >= start:
#             freight(schedules[idx+1:], schedules[idx][1], cnt+1)
#     if cnt > sub:
#         sub = cnt
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     schedules = []
#     for _ in range(N):
#         start, end = map(int, input().split())
#         schedules.append((start, end))
#     schedules.sort()
#     ans = 0
#     for idx in range(N):
#         if len(schedules[idx:]) > ans:
#             sub = 0
#             freight(schedules[idx:], 0, 0)
#         if ans < sub:
#             ans = sub
#     print(f'#{tc} {ans}')

# 화물 도크
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     schedules = []
#     for _ in range(N):
#         s, e = map(int, input().split())
#         schedules.append((s,e))
#     schedules.sort(key=lambda x:x[1])
#
#     start = schedules[0][1]
#     cnt = 1
#     for schedule in schedules[1:]:
#         if schedule[0] >= start:
#             cnt += 1
#             start = schedule[1]
#     print(f'#{tc} {cnt}')

# 전기버스2
# def dfs(idx):
#     global charge, min_charge
#
#     if idx + stop_info[idx] >= stop_leng-1:
#         if charge < min_charge:
#             min_charge = charge
#         return
#
#     if charge >= min_charge-1:
#         return
#
#     for i in range(idx+stop_info[idx], idx, -1):
#         charge += 1
#         dfs(i)
#         charge -= 1
#
#
# T = int(input())
# for tc in range(1, T+1):
#     lis = list(map(int, input().split()))
#     stop_leng = lis[0]
#     stop_info = lis[1:]
#     min_charge = 100
#     charge = 0
#     dfs(0)
#     print(f'#{tc} {min_charge}')

# 5207. 이진탐색
# def search(lis, num):
#     global ans
#     start = 0
#     end = N-1
#     flag = 0
#     while start <= end:
#         mid = (start+end) // 2
#         if lis[mid] == num:
#             ans += 1
#             return
#         elif lis[mid] < num:
#             start = mid+1
#             if flag == 1:
#                 return
#             flag = 1
#         elif lis[mid] > num:
#             end = mid-1
#             if flag == -1:
#                 return
#             flag = -1
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     A.sort()
#     ans = 0
#     for b in B:
#         search(A, b)
#     print(f'#{tc} {ans}')

# 5209. 최소 생산 비용
# def Calc(row, cost):
#     global min_cost
#     if row == N:
#         if cost < min_cost:
#             min_cost = cost
#         return
#
#     if cost >= min_cost:
#         return
#
#     for i in range(N):
#         if used[i] == 0:
#             used[i] = 1
#             Calc(row+1, cost + factory[row][i])
#             used[i] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     factory = [list(map(int, input().split())) for _ in range(N)]
#     used = [0]*N # 컬럼의 선택 여부 0,1 로 표시
#     min_cost = 1500
#     Calc(0, 0)
#     print(f'#{tc} {min_cost}')

# 부분 수열의 합
# def backtracking(idx, sub):
#     ans = 0
#     if sum(sub) > K:
#         return 0
#
#     if sum(sub) == K:
#         return 1
#
#     for i in range(idx, N):
#         if used[i] == 0:
#             used[i] = 1
#             ans += backtracking(i, sub + [nums[i]])
#             used[i] = 0
#
#     return ans
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     nums = list(map(int, input().split()))
#     used = [0]*N
#     print(f'#{tc} {backtracking(0, [])}')

# 퀵 정렬 1
# def quick_sort(A, l, r):
#     if l <= r:
#         p = partition(A, l, r)
#         quick_sort(A, l, p-1)
#         quick_sort(A, p+1, r)
#
# def partition(A, l, r):
#     pivot = l
#     while l <= r :
#         while(l <= r and A[l] <= A[pivot]):
#             l += 1
#         while(l <= r and A[r] >= A[pivot]):
#             r -= 1
#         if l < r:
#             A[l], A[r] = A[r], A[l]
#     A[pivot], A[r] = A[r], A[pivot]
#     return r
#
# T = int(input())
# for tc in range(1, 1+T):
#     N = int(input())
#     A = list(map(int, input().split()))
#     quick_sort(A, 0, N - 1)
#     print(f'#{tc} {A[N//2]}')

# 퀵 정렬 2 _ 메모리 크게 나옴
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     left, right = [], []
#     pivot = arr[0]
#
#     for idx in range(1, len(arr)):
#         if arr[idx] < pivot:
#             left.append(arr[idx])
#         else:
#             right.append(arr[idx])
#
#     return quick_sort(left) + [pivot] + quick_sort(right)
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     print(f'#{tc} {quick_sort(arr)[N//2]}')

# 퀵 정렬 3 _ 수업에서 설명한 quick sort
# def partition(arr, start, end):
#     pivot = start
#     L = start
#     R = end
#     while L <= R:
#         # pivot index 보다 작은 인덱스 찾기
#         while L <= R and arr[L] <= arr[pivot]:
#             L += 1
#         while L <= R and arr[pivot] <= arr[R]:
#             R -= 1
#
#         if L < R:
#             arr[L], arr[R] = arr[R], arr[L]
#     arr[start], arr[R] = arr[R], arr[start]
#     return R
#
#
# def quick_sort(arr, start, end):
#     if start < end:
#         pivot = partition(arr, start, end)
#         quick_sort(arr, start, pivot - 1)
#         quick_sort(arr, pivot + 1, end)
#     return arr
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     arr = quick_sort(arr, 0, N - 1)
#     print(f'#{tc}', arr[N // 2])

# 전자카트 _ enumerate 써서 풀어보기
pass

# 그래프 경로2 _ 연습용
# def f(start):
#     global ans
#
#     if G in tree[start]:
#         ans = 1
#
#     visited[start] = 1
#
#     for i in tree[start]:
#         if visited[i] == 0:
#             f(i)
#
# from collections import defaultdict
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split()) # 노드 개수, 간선 개수
#     tree = defaultdict(list)
#     ans = 0
#     visited = [0]*(V+1)
#     for _ in range(E):
#         start, end = map(int, input().split()) # 출발, 도착 노드
#         tree[start].append(end)
#         tree[end].append(start)
#     S, G = map(int, input().split())  # 출발, 도착 노드(경로 확인)
#     f(S)
#     print(f'#{tc} {ans}')

# 그래프 경로2 _ 제출용
# def check(x):
#     global ans
#
#     if x == G:
#         ans = 1
#
#     visited[x] = 1
#
#     for i in range(1, V+1):
#         if visited[i] == 0 and arr[x][i] == 1:
#             check(i)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     arr = [[0]*(V+1) for _ in range(V+1)]
#     visited = [0]*(V+1)
#     ans = 0
#     for _ in range(E):
#         i, j = map(int, input().split())
#         arr[i][j] = 1
#     S, G = map(int, input().split()) # 출발, 도착
#     check(S)
#     print(f'#{tc} {ans}')

# 5248. 그룹 나누기
# def f(idx):
#     for i in tree[idx]:
#         if visited[i] == 0:
#             visited[i] = 1
#             f(i)
#
# from collections import defaultdict
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # 1~N까지 번호, M장의 신청서
#     tree = defaultdict(list)
#     pairs = list(map(int, input().split()))
#     for i in range(M):
#         x = pairs[2*i]
#         y = pairs[2*i+1]
#         tree[x].append(y)
#         tree[y].append(x)
#     visited = [0]*(N+1) # 방문여부
#     ans = 0 # 트리의 개수
#     for i in range(1, N+1):
#         if visited[i] == 0: # 방문안한 노드가 있으면
#             ans += 1 # 트리의 개수를 추가하고, 방문처리한 후
#             visited[i] = 1
#             f(i) # 함수 실행해서 연결된 노드를 모두 방문처리 함
#     print(f'#{tc} {ans}')

# 5249. 최소 신장 트리 _ 크루스칼
# def find_set(x):
#     while x != p[x]:
#         x = p[x]
#     return x
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split()) # 노드번호(0~V), 간선 개수
#     edge = []
#     for _ in range(E):
#         n1, n2, w = map(int, input().split())
#         edge.append((w, n1, n2))
#     edge.sort()
#     p = [i for i in range(V+1)]
#     cnt = 0
#     total = 0
#     for w, n1, n2 in edge:
#         if find_set(n1) != find_set(n2):
#             cnt += 1
#             total += w
#             if n1 < n2:
#                 n1, n2 = n2, n1
#             p[find_set(n1)] = find_set(n2)
#             if cnt == V:
#                 break
#     print(f'#{tc} {total}')

# 5249. 최소 신장 트리 _ 프림
from collections import defaultdict
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # 노드버호(0~V), 간선 개수
    edge = defaultdict(list)
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edge[n1].append((n2, w))

# 5247. 연산 _ 시간초과
# def calc(num, operator):
#     if operator == 1:
#         return num+1
#     elif operator == 2:
#         return num-1
#     elif operator == 3:
#         return num*2
#     elif operator == 4:
#         return num-10
#
# def f(q):
#     while q:
#         num, cnt = q.popleft()
#         if num == M:
#             return cnt
#         if num > 1000000:
#             continue
#         for d in dir:
#             next = calc(num, d)
#             if visited[next] == 0 and next < min_cnt:
#                 visited[next] = 1
#                 q.append((next, cnt+1))
#
# from collections import deque
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     dir = [1, 2, 3, 4]
#     q = deque()
#     min_cnt = 1000000
#     visited = [0]*1000001
#     q.append((N, 0))
#     print(f'#{tc} {f(q)}')
