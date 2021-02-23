# GNS
# # 글자를 숫자로 변환해 반환하는 함수
# def wordtonum(word):
#     week = {'ZRO': 0,
#             'ONE': 1,
#             'TWO': 2,
#             'THR': 3,
#             'FOR': 4,
#             'FIV': 5,
#             'SIX': 6,
#             'SVN': 7,
#             'EGT': 8,
#             'NIN': 9
#             }
#     return week.get(word)
#
# # 숫자를 글자로 변환해 반환하는 함수
# def numtoword(num):
#     week = {0: 'ZRO',
#             1: 'ONE',
#             2: 'TWO',
#             3: 'THR',
#             4: 'FOR',
#             5: 'FIV',
#             6: 'SIX',
#             7: 'SVN',
#             8: 'EGT',
#             9: 'NIN'
#             }
#     return week.get(num)
#
# T = int(input())
# for tc in range(1, T+1):
#     num = list(input().split())
#     days = input().split()
#     result = []
#     # 리스트의 원소들을 숫자로 변환해 result 리스트에 더해준다.
#     for day in days:
#         result.append(wordtonum(day))
#
#     # result 리스트를 오름차순으로 정렬한다.
#     for i in range(len(result)-1):
#         min_idx = i
#         for j in range(i+1, len(result)):
#             if result[j] < result[min_idx]:
#                 min_idx = j
#         result[i], result[min_idx] = result[min_idx], result[i]
#
#     # result 리스트의 원소를 숫자로 반환해 ans 리스트에 더해주고 join 을 통해 문자열로 출력한다.
#     print(' '.join(map(lambda x: numtoword(x), result)))

# GNS _ 다른 방법으로 풀어보기
# T = int(input())
# numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
# for tc in range(1, T+1):
#     input()
#     cnt = [0] * 10
#     eng_number = input().split()
#     for num in eng_number:
#         cnt[numbers.index(num)] += 1
#
#     result = []
#     for i in range(10):
#         result += [numbers[i]] * cnt[i]
#
#     result = ' '.join(result)
#     print(f'#{tc}\n{result}')

# # 브루트 포스
# p = 'rithm'
# t = 'A pattern matching algorithm'
#
# M = len(p) # 찾을 패턴의 길이
# N = len(t) # 전체 텍스트의 길이
#
# # def BruteForce(p, t):
# #     i = 0 # t 의 인덱스
# #     j = 0 # p 의 인덱스
# #     while j < M and i < N:
# #         # t 와 p 의 원소가 다르다면
# #         if t[i] != p[j]:
# #             i = i - j # 지나쳐온 원소 중에 찾을 패턴의 첫번째 원소가 있는지 확인하기 위함
# #             j = -1 # if 문을 탈출해서 인덱스를 원위치 시키기 위함
# #         i = i + 1
# #         j = j + 1
# #     if j == M : return i - M # 검색 성공
# #     else: return -1 # 검색 실패
#
#
# # 브루트 포스 2
# p = 'rithm'
# t = 'A pattern matching algorithm'
#
# M = len(p) # 찾을 패턴의 길이
# N = len(t) # 전체 텍스트의 길이
# # def BruteForce2(p,t):
# #     N = len(t)
# #     M = len(p)
# #
# #     # 시작 위치를 컨트롤
# #     for i in range(N-M+1):
# #         cnt = 0
# #         for j in range(M):
# #             if t[i+j] == p[j]:
# #                 cnt += 1
# #             else:
# #                 break
# #         if cnt == M:
# #             return i
# #     return -1
# #
# # print(BruteForce2(p,t))


# 보이어-무어 이해하기


# [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교
# T = int(input())
# for tc in range(1, T+1):
#     str1 = input()
#     str2 = input()
#     N = len(str1)
#     M = len(str2)
#     cnt = 0
#     # M-N 번째 인덱스가 str1 을 비교시작할 수 있는 마지막 인덱스
#     for i in range(M-N+1):
#         # str2 에서 앞에서부터 str1 의 길이만큼 확인해보았을때 st1과 같으면 cnt +1
#         if str2[i:i+N] == str1:
#             cnt = 1
#             break
#     print('#{} {}'.format(tc, cnt))

# [파이썬 S/W 문제해결 기본] 3일차 - 회문
# T= int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = []
#     ans = 0
#     # 2차원 배열을 만든다.
#     for _ in range(N):
#         arr.append(list(map(str, input())))
#     # 세로로 찾기 위해 전치행렬을 만든다.
#     T_arr = list(zip(*arr))
#
#     # 각 행 별로 주어진 길이만큼 잘라서 회문인지 확인한다.
#     for i in range(N):
#         for j in range(N-M+1):
#             lis = arr[i][j:j+M]
#             T_lis = T_arr[i][j:j+M]
#             # 회문이면 ans에 해당 회문을 저장한다.
#             if lis == lis[::-1]:
#                 ans = lis
#                 break # lis 를 찾으면 break (안했더니 제한시간 초과 뜸)
#             if ans: break # ans 를 찾으면 세로를 탐색할 필요가 없음
#             if T_lis == T_lis[::-1]:
#                 ans = T_lis
#                 break
#     result = ''.join(ans)
#     print('#{} {}'.format(tc, result))

# [파이썬 S/W 문제해결 기본] 3일차 - 글자수
# T = int(input())
# for tc in range(1, T+1):
#     # str1 은 문자를 하나씩 쪼개서 리스트로 만든다.
#     str1 = list(map(str, input()))
#     # 카운트 정렬을 하기 위해 str1 의 길이와 같은 0으로 된 리스트를 만든다.
#     str1_cnt = [0]*len(str1)
#     str2 = input()
#
#     # str2 를 순회하면서
#     for i in str2:
#         # 각 원소가 str1 안에 있다면
#         if i in str1:
#             # 해당 원소의 str1 내에서의 index를 찾아서 str1_cnt 에 1씩 더해준다.
#             str1_cnt[str1.index(i)] += 1
#
#     # str1_cnt 안에서 가장 큰 값을 max_val 에 저장한다.
#     max_val = 0
#     for c in str1_cnt:
#         if c > max_val:
#             max_val = c
#
#     print(f'#{tc} {max_val}')


# [S/W 문제해결 기본] 3일차 - 회문2 (flag)
# for tc in range(1, 11):
#     int(input())
#     arr = []
#     for _ in range(100):
#         arr.append(input())
#     T_arr = list(zip(*arr))
#     long = 100
#     ans = 0
#
#     flag = False
#     for long in range(100,-1,-1):
#         for i in range(100):
#             for j in range(100-long+1):
#                 pattern = arr[i][j:j+long]
#                 reverse_pattern = pattern[::-1]
#                 if pattern == reverse_pattern:
#                     ans = long
#                     flag = True
#                 T_pattern = T_arr[i][j:j + long]
#                 T_reverse_pattern = T_pattern[::-1]
#                 if T_pattern == T_reverse_pattern:
#                         ans = long
#                         flag = True
#             if flag: break
#         if flag: break
#
#
#     print(f'#{tc} {ans}')

# [S/W 문제해결 기본] 3일차 - 회문2 (flag)_원재가 좀 더 간단하게 만들어봄
# for tc in range(1, 11):
#     input()
#     arr = []
#     for _ in range(100):
#         arr.append(input())
#     T_arr = list(zip(*arr))
#     ans = 0
#     flag=False
#
#     for long in range(100,-1,-1):
#         for i in range(100):
#             for j in range(100-long+1):
#                 pat1 = arr[i][j:j+long]
#                 pat2 = T_arr[i][j:j+long]
#                 if pat1==pat1[::-1] or pat2 == pat2[::-1]:
#                     ans=long
#                     flag=True
#                     break
#             if flag: break
#         if flag: break
#
#     print(f'#{tc} {ans}')

# [S/W 문제해결 기본] 3일차 - 회문2 (def)
# for tc in range(1, 11):
#     int(input())
#     arr = []
#     for _ in range(100):
#         arr.append(input())
#     T_arr = list(zip(*arr))
#     long = 100
#     ans = 0
#
#     def Palindrome():
#         for long in range(100,-1,-1):
#             for i in range(100):
#                 for j in range(100-long+1):
#                     pattern = arr[i][j:j+long]
#                     T_pattern = T_arr[i][j:j+long]
#                     if pattern == pattern[::-1] or T_pattern == T_pattern[::-1]:
#                         ans = long
#                         return ans
#
#     print(f'#{tc} {Palindrome()}')

# [S/W 문제해결 기본] 3일차 - 회문2 (def)
# def search():
#     global ans
#     for long in range(100,-1,-1):
#         for i in range(100):
#             for j in range(100-long+1):
#                 pat1 = arr[i][j:j+long]
#                 pat2 = T_arr[i][j:j+long]
#                 if pat1==pat1[::-1] or pat2 == pat2[::-1]:
#                     ans=long
#                     return
#
# for tc in range(1, 11):
#     input()
#     arr = []
#     for _ in range(100):
#         arr.append(input())
#     T_arr = list(zip(*arr))
#     ans = 0
#     search()
#     print(f'#{tc} {ans}')

# 가장 빠른 문자열 타이핑
# T = int(input())
# for tc in range(1, T+1):
#     word, part = map(list,input().split())
#     M = len(word)
#     N = len(part)
#     for i in range(M-N+1):
#         if word[i:i+N] == part:
#             word[i:i+N] = '0'
#     cnt = 0
#     for i in word:
#         cnt += 1
#     print(f'#{tc} {cnt}')

# 가장 빠른 문자열 타이핑
# T=int(input())
# for tc in range(1,T+1):
#     A,B=input().split()
#     B_in_A=A.count(B)
#     ans=B_in_A+len(A)-len(B)*B_in_A
#     print(f'#{tc} {ans}')

# 가장 빠른 문자열 타이핑
# T = int(input())
# for tc in range(1, T + 1):
#     A, B = input().split()
#     M = len(A)
#     N = len(B)
#
#     cnt = 0
#     i = 0
#     while i < M - N + 1:
#         if A[i:i + N] == B:
#             cnt += 1
#             i += N
#             continue
#         i += 1
#     ans = cnt + M - N * cnt
#     print(f'#{tc} {ans}'

# 쇠막대기 자르기_ 라이브강의 해설
# T = int(input())
# for tc in range(1, T+1):
#     iron_bar = input()
#
#     cnt = 0
#     ans = 0
#
#     for i in range(len(iron_bar)):
#         # 열린 괄호라면 막대 추가
#         if iron_bar[i] == '(':
#             cnt += 1
#         else:
#             # 닫힌 괄호라면 막대 감소
#             # 레이저라면 당연히 잘못 세었으니 뺀다.
#             # 아니라면 어차피 철봉 끝이니 빼는게 맞다.
#             cnt  -= 1
#
#             # 레이저라면
#             if iron_bar[i-1] == '(':
#                 # 레이저로 인해 잘린 막대들이 생겼으므로
#                 ans += cnt
#             else:
#                 # 막대 끝이라는 뜻
#                 ans += 1
#     print('#{} {}'.format(tc, ans))


# 쇠막대기 자르기_ 라이브강의 해설 (stack 으로 풀어보기)
# T = int(input())
# for tc in range(1, int(input())+1):
#     iron_bar = input()
#
#     # 실제로 쇠막대가 담길 리스트
#     s = []
#     ans = 0
#
#     for i in range(len(iron_bar)):
#         # 열릴 괄호라면 s 리스트에 넣기
#         if iron_bar[i] == '(':
#             s.append('(')
#         else:
#             # 무조건 꺼내기
#             s.pop()
#             # 레이저
#             if iron_bar[i-1] == '(':
#                 ans += len(s)
#             else:
#                 ans += 1
#     print('#{} {}'.format(tc, ans))

# 의석이의 세로로 말해요 _ 처음 시도했을 때 풀이
# T = int(input())
# for tc in range(1,T+1):
#     arr = []
#     arr2 = []
#     for _ in range(5):
#         arr.append(input())
#     # arr 에 더해준 리스트 중에서 가장 긴 길이가 무엇인지 구한다.
#     longest = 0
#     for i in arr:
#         if len(i)> longest:
#             longest = len(i)
#     # arr 의 행 길이가 longest 와 같으면 변화 없이 arr2에 appebd하고, 짧으면 임의의 문자 *을 빈 자리만큼 추가해 append 한다.
#     for i in arr:
#         if len(i) == longest:
#             arr2.append(i)
#         elif len(i) < longest:
#             arr2.append(i + '*'*(longest-len(i)))
#
#     # arr2 의 전치행렬을 만든다
#     T_arr = list(zip(*arr2))
#     result = []
#     # 행의 길이는 T_arr 의 길이, j 는 각 행의 길이로 놓고 각 원소를 순회하면서
#     for i in range(len(T_arr)):
#         for j in range(len(T_arr[i])):
#             # 빈 result 리스트에 더한다.
#             result.append(T_arr[i][j])
#     # 필요없는 문자 * 을 제거한다.
#     ans = ''
#     for i in result:
#         if i != '*':
#             ans += i
#     print(f'#{tc} {ans}')


# 의석이의 세로로 말해요 _ try-except 로 풀어보기
# T= int(input())
# for tc in range(1, T+1):
#     arr = [0] * 5
#     max_len = 0
#     for i in range(5):
#         arr[i] = list(input())
#
#         if len(arr[i]) > max_len:
#             max_len = len(arr[i])
#     # 세로로 읽어보자
#     print(f'#{tc}', end=' ')
#     for i in range(max_len):
#         for j in range(5):
#             # if len(arr[j] > i):
#             #     print(arr[j][i], end="")
#             try:
#                 print(arr[j][i], end = '')
#             except:
#                 pass

# 의석이의 세로로 말해요 _ try-except 없이 간단히 풀어보기
# T = int(input())
# for tc in range(1, T + 1):
#
#     arr = []
#     L = 0
#
#     for _ in range(5):
#
#         temp = input()
#         arr.append(temp)
#
#         if L < len(temp):
#             L = len(temp)
#
#     result = ''
#     for j in range(L):
#         for i in range(5):
#             if j < len(arr[i]):
#                 result += arr[i][j]
#
#     print(f'#{tc} {result}')