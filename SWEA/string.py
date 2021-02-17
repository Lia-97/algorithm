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
#     ans = []
#     for r in result:
#         ans.append(numtoword(r))
#     print('#{}'.format(tc))
#     print(' '.join(ans))

# GNS _ 다른 방법으로 풀어보기
# T = int(input())
# numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
# cnt = [0] * 10
# for tc in range(1, T+1):
#     input()
#     eng_number = input().split()
#

# 브루트 포스
p = 'rithm'
t = 'A pattern matching algorithm'

M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

# def BruteForce(p, t):
#     i = 0 # t 의 인덱스
#     j = 0 # p 의 인덱스
#     while j < M and i < N:
#         # t 와 p 의 원소가 다르다면
#         if t[i] != p[j]:
#             i = i - j # 지나쳐온 원소 중에 찾을 패턴의 첫번째 원소가 있는지 확인하기 위함
#             j = -1 # if 문을 탈출해서 인덱스를 원위치 시키기 위함
#         i = i + 1
#         j = j + 1
#     if j == M : return i - M # 검색 성공
#     else: return -1 # 검색 실패


# 브루트 포스 2
p = 'rithm'
t = 'A pattern matching algorithm'

M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이
# def BruteForce2(p,t):
#     N = len(t)
#     M = len(p)
#
#     # 시작 위치를 컨트롤
#     for i in range(N-M+1):
#         cnt = 0
#         for j in range(M):
#             if t[i+j] == p[j]:
#                 cnt += 1
#             else:
#                 break
#         if cnt == M:
#             return i
#     return -1
#
# print(BruteForce2(p,t))

# [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
