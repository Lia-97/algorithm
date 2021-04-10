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

#