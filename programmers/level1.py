# K번째수
# def solution(array, commands):
#     answer = []
#     for command in commands:
#         new_array = array[command[0]-1:command[1]]
#         new_array.sort()
#         answer.append(new_array[command[2]-1])
#     return answer
#
# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# 문자열 내 p와 y의 개수
#
# def solution(s):
#     sentence = s.lower()
#     if sentence.count('p') == sentence.count('y'):
#         return True
#     else:
#         return False
#
# print(solution('Pyy'))

# 두 정수 사이의 합
#
# def solution(a, b):
#     answer = 0
#     if a <= b:
#         for i in range(a, b+1):
#             answer += i
#     if a > b:
#         for i in range(b, a+1):
#             answer += i
#     return answer
#
# print(solution(5,3))

# 두 정수 사이의 합 (또 다른 풀이)
#
# def solution(a, b):
#     if a > b:
#         a, b = b, a
#     return sum(range(a, b+1))

# 같은 숫자는 싫어
#
# def solution(arr):
#     answer = []
#     pre = 10
#     for a in arr:
#         if a != pre:
#             answer.append(a)
#             pre = a
#         else:
#             continue
#
#     return answer
#
# # 어떻게 동작?
# def no_continuous(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print( no_continuous( "133303" ))

# 수박수박수박수박수박수?
#
# def solution(n):
#     if n % 2 == 0:
#         answer = '수박' * (n // 2)
#     else:
#         answer = '수박' * (n // 2) + '수'
#
#     return answer
#
# print(solution(4))

# 자릿수 더하기
#
# def solution(n):
#     total = 0
#     for i in str(n):
#         total += int(i)
#     return total

# 시저 암호
# # A = 65, a = 97
# # Z = 90, z = 122
#
# def solution(s, n):
#     answer = ''
#     large_al = [chr(i) for i in range(65, 91)]
#     small_al = [chr(i) for i in range(97, 123)]
#     for i in str(s):
#         if i in large_al:
#             if ord(i) + n > 90:
#                 answer = answer + chr(64 + (ord(i) + n) % 90)
#             else:
#                 answer = answer + chr(ord(i) + n)
#         elif i in small_al:
#             if ord(i) + n > 122:
#                 answer = answer + chr(96 + (ord(i) + n) % 122)
#             else:
#                 answer = answer + chr(ord(i) + n)
#         elif i == ' ':
#             answer += ' '
#
#     return answer
#
# print(solution("a B z", 4))

# 문자열 다루기 기본
#
# def solution(s):
#     if len(s) == 4 or len(s) == 6:
#         try:
#             int(s)
#         except ValueError:
#             return False
#         else:
#             return True
#     else:
#         return False
#
# print(solution('a234'))
# print(solution('1234'))

# 문자열 다루기 isdigit() 함수 사용해보기
# # isdigit() => 주어진 문자열이 숫자로 되어있는지 검사하는 함수
# def alpha_string46(s):
#     return s.isdigit() and len(s) in (4, 6)
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print( alpha_string46("a234") )
# print( alpha_string46("1234") )
#
# a = '12345678'
# # True 를 반환한다.
# print(a.isdigit())

# 정수 내림차순으로 배치하기
#
# def solution(n):
#     reverse_int = ''
#     for i in sorted(list(str(n))):
#         reverse_int = i + reverse_int
#     return int(reverse_int)
#
# print(solution(118372))
#
# def solution(n):
#     ls = list(str(n))
#     ls.sort(reverse = True)
#     return int("".join(ls))

# 서울에서 김서방 찾기
# def solution(seoul):
#     for s in enumerate(seoul):
#         if s[1] == 'Kim':
#             place = s[0]
#             return f'김서방은 {place}에 있다.'
# print(solution(['Jane', 'Kim']))

# 약수의 합
#
# def solution(n):
#     answer = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             answer += i
#
#     return answer
#
# print(solution(12))
# print(solution(5))

# 내적
# def solution(a, b):
#     answer = 0
#     for i in range(len(a)):
#         answer += a[i]*b[i]
#     return answer
#
# print(solution([1,2,3,4], [-3,-1,0,2]))

# 문자열 내림차순으로 배치하기
# def solution(s):
#     answer = []
#     result = ''
#     for i in s:
#         answer.append(ord(i))
#     sorted_answer = sorted(answer, reverse=True)
#     for s in sorted_answer:
#         result += chr(s)
#
#     return result
#
# print(solution("Zbcdefg	"))

# 이상한 문자 만들기
#
# def solution(s):
#     s_list = s.split(' ')
#     result=[]
#     for i in s_list:
#         word = ''
#         for j in enumerate(i):
#             if j[0] % 2:
#                 word += j[1].lower()
#             else:
#                 word += j[1].upper()
#         result.append(word)
#     return ' '.join(result)
#
# print(solution('try hello world'))

# 신규 아이디 추천
# import re
# def solution(new_id):
#     answer = ''
#     new_id = new_id.lower()
#     new_id.sub('[a-z]')
#     return answer

# 짝수와 홀수
#
# def solution(num):
#
#     return "Odd" if num % 2 else "Even"

# 평균 구하기
#
# def solution(arr):
#     return sum(arr)/len(arr)

# 3진법 뒤집기
#
# def recur(n):
#     if n == 2:
#         return str(2)
#     if n == 1:
#         return str(1)
#
#     return recur(n // 3) + str(n % 3)
#
# def solution(n):
#     number = recur(n)
#     new_number = number[::-1]
#     answer = 0
#     for i in range(len(new_number)):
#         answer += int(new_number[i]) * (3 ** (len(new_number)-(i+1)))
#
#     return answer
#
# print(solution(45))

# 제일 작은 수 제거하기
#
# def solution(arr):
#     if len(arr) == 1:
#         return [-1]
#     else:
#         new_arr = sorted(arr)
#         minimum = new_arr[0]
#         arr.remove(minimum)
#         return arr
#
# print(solution([4,3,2,1]))

# 정수 제곱근 판별
# def solution(n):
#     if (n ** (1/2)).is_integer():
#         return (n ** (1/2) +1) ** 2
#     else:
#         return -1
#
# print(solution(121))

# 가운데 글자 가져오기
# def solution(s):
#     if len(s) % 2:
#         return s[len(s)//2]
#     else:
#         return s[len(s)//2 - 1:len(s)//2 + 1]
#
# print(solution("abcde"))

# 히샤드 수
# def solution(x):
#     str_x = str(x)
#     lis = []
#     for i in range(len(str_x)):
#         lis.append(str_x[i])
#     num = sum(list(map(int,lis)))
#     if x % num == 0:
#         return True
#     else:
#         return False
# print(solution(10))

# 하샤드 수 2
# def solution(n):
#     return n % sum([int(c) for c in str(n)]) == 0

# 체육복
# def solution(n, lost, reserve):
#     for i in list(lost):
#         if i in reserve:
#             lost.remove(i)
#             reserve.remove(i)
#
#     for i in list(lost):
#         if i not in reserve:
#             if i-1 in reserve:
#                 reserve.remove(i-1)
#                 lost.remove(i)
#             elif i+1 in reserve:
#                 reserve.remove(i+1)
#                 lost.remove(i)
#
#     answer = n - len(lost)
#     return answer

# 행렬의 덧셈
# def solution(arr1, arr2):
#     arr = []
#     for i in range(len(arr1)):
#         sub = []
#         for j in range(len(arr1[0])):
#             sub.append(arr1[i][j] + arr2[i][j])
#         arr.append(sub)
#     return arr

# 핸드폰 번호 가리기
# def solution(phone_number):
#     answer = ''
#     for i in range(len(phone_number)-4):
#         answer += '*'
#     answer += phone_number[len(phone_number)-4:]
#
#     return answer

# 키패드 누르기
# def solution(numbers, hand):
#     answer = ''
#     l = [1, 4, 7]
#     r = [3, 6, 9]
#     L = [10]
#     R = [12]
#     for n in numbers:
#         if n in l:
#             L.append(n)
#             answer += 'L'
#         elif n in r:
#             R.append(n)
#             answer += 'R'
#         else:
#             if n == 0:
#                 n = 11
#             left_d = abs(L[-1] - n)//3 + abs(L[-1] - n)%3
#             right_d = abs(R[-1] - n) // 3 + abs(R[-1] - n)%3
#             if left_d < right_d:
#                 answer += 'L'
#                 L.append(n)
#             elif left_d > right_d:
#                 answer += 'R'
#                 R.append(n)
#             else:
#                 if hand == 'right':
#                     answer += 'R'
#                     R.append(n)
#                 else:
#                     answer += 'L'
#                     L.append(n)
#
#     return answer

# 나누어 떨어지는 숫자 배열
# def solution(arr, divisor):
#     answer = []
#     for i in arr:
#         if i % divisor == 0:
#             answer.append(i)
#     answer.sort()
#     if not answer:
#         answer.append(-1)
#     return answer

# 모의고사
# def solution(answers):
#     answer = [] # 반환할 리스트
#     # 각 학생들이 답을 찍는 규칙
#     student1 = [1, 2, 3, 4, 5]
#     student2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     # 1, 2, 3 학생이 맞은 문제의 갯수가 담길 리스트
#     score = [0, 0, 0]
#     # answers 의 원소가 학생들이 찍은 답과 일치한다면 score 에 +1
#     for i in range(len(answers)):
#         if answers[i] == student1[i % len(student1)]:
#             score[0] += 1
#         if answers[i] == student2[i % len(student2)]:
#             score[1] += 1
#         if answers[i] == student3[i % len(student3)]:
#             score[2] += 1
#     for i in range(len(score)):
#         if score[i] == max(score):
#             answer.append(i + 1)
#     # 오름차순으로 정렬해야 하니까 sort 해서 return
#     answer.sort()
#     return answer

# 두 개 뽑아서 더하기
# def solution(numbers):
#     answer = []
#     numbers_copy = numbers[::]
#     for i in numbers:
#         numbers_copy.remove(i)
#         for j in numbers_copy:
#             answer.append(i + j)
#         numbers_copy.append(i)
#     return sorted(list(set(answer)))

# 2016년
# def solution(a, b):
#     days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     d = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
#     diff_mon = a - 1
#     diff_day = 0
#     if a == 1:
#         diff_day += b
#     elif a > 1:
#         for i in range(diff_mon):
#             diff_day += days[i]
#         diff_day += b
#     answer = d[diff_day % 7 - 1]
#
#     return answer

# 문자열 내 마음대로 정렬하기 _ 딕셔너리로 풀기
# def solution(strings, n):
#     answer = []
#     dic = {}
#     for word in strings:
#         if word[n] not in dic:
#             dic[word[n]] = [word]
#         else:
#             dic[word[n]].append(word)
#     for i in dic:
#         dic[i].sort()
#     alpha = sorted(dic)
#     for a in alpha:
#         answer.extend(dic[a])
#
#     return answer

# 직사각형 별찍기
# a, b = map(int, input().strip().split(' '))
# for _ in range(a):
#     print('*'*b)

# 크레인 인형뽑기 게임
# def solution(board, moves):
#     answer = 0
#     T_board = list(zip(*board))
#     dolls = []
#     for T in T_board:
#         sub = []
#         for t in T:
#             if t != 0:
#                 sub.append(t)
#         dolls.append(sub)
#     stack = [-1]
#     for i in moves:
#         if dolls[i-1]:
#             doll = dolls[i-1].pop(0)
#             if stack[-1] == doll:
#                 stack.pop()
#                 answer += 2
#             else:
#                 stack.append(doll)
#     return answer
#
# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))

# 비밀지도
# def tentotwo(num, n):
#     ans = ''
#     if num == 0:
#         ans += ' '*n
#     else:
#         while num > 1:
#             spare = num % 2
#             if spare == 1:
#                 ans = '#' + ans
#                 print(ans)
#             else:
#                 ans = ' ' + ans
#                 print(ans)
#             num = num // 2
#         ans = '#' + ans
#
#     if len(ans) < n:
#         ans = ' '*(n-len(ans)) + ans
#     return ans
#
# def solution(n, arr1, arr2):
#     answer = []
#     lis1 = list(map(lambda x: tentotwo(x, n), arr1))
#     lis2 = list(map(lambda x: tentotwo(x, n), arr2))
#
#     print(lis1)
#     print(lis2)
#     for i in range(n):
#         sub = ''
#         for j in range(n):
#             if lis1[i][j] == ' ' and lis2[i][j] == ' ':
#                 sub += ' '
#             else:
#                 sub += '#'
#         answer.append(sub)
#
#     return answer

# 예산
# def solution(d, budget):
#     d.sort()
#     answer = 0
#     total = 0
#     for i in range(len(d)):
#         total += d[i]
#         if total > budget:
#             answer = i
#             break
#         else:
#             answer = len(d)
#     return answer

# 프로그래밍
# def solution(v):
#     answer = []
#     x_point= []
#     y_point = []
#     for point in v:
#         x_point.append(point[0])
#         y_point.append(point[1])
#     for x in x_point:
#         if x_point.count(x) == 1:
#             answer.append(x)
#     for y in y_point:
#         if y_point.count(y) == 1:
#             answer.append(y)
#     return answer

# 폰켓몬
# from collections import defaultdict
# def solution(nums):
#     number = defaultdict(int)
#     # 각 종류 별 폰켓몬 : 폰켓몬 개수
#     for n in nums:
#         number[n] += 1
#
#     if len(number) >= len(nums)//2:
#         ans = len(nums)//2
#     else:
#         ans = len(number)
#
#     return ans

# 물류
# N, K = map(int, input().split()) # 라인 길이, 부품 집을 수 있는 거리
# factory = list(input())
# stack=[factory.pop()]
# cnt = 0
# while factory:
#     ans = factory.pop()
#     if stack:
#         if stack[-1] == 'P' and ans == 'H':
#             stack.append(ans)
#             stack.clear()
#             cnt += 1
#         elif stack[-1] == 'H' and ans == 'P':
#             stack.append(ans)
#             stack.clear()
#             cnt += 1
#     else:
#         stack.append(ans)
#
# print(cnt)

# 물류 _ 2
# N, K = map(int, input().split()) # 라인 길이, 부품 집을 수 있는 거리
# factory = list(input())
# picked = [0]*N
# for i in range(N-K):
#     if factory[i] == 'P':
#         if 'H' in factory[i:i+K+1]:

# 바이러스
# P, N = map(int, input().split()) # 증가율, 시간
# virus = list(map(int, input().split()))
# ans = 0
#
# for idx in range(N):
#     ans += virus[idx] * (P**(N-(idx+1)))
#
# print(ans)

# 스마트 물류
# N, K = map(int,input().split())
# factory = [0]*K + list(input()) + [0]*K
# cnt = 0
# for idx in range(len(factory)):
#     if factory[idx] == 'P':
#         for i in range(idx-K, idx+K+1):
#             if factory[i] == 'H':
#                 factory[i] = 0
#                 cnt += 1
#                 break
#
# print(cnt)

# 완주하지 못한 선수
# from collections import defaultdict
# def solution(participant, completion):
#     runner = defaultdict(int)
#     complete = defaultdict(int)
#     for p in participant:
#         runner[p] += 1
#
#     for c in completion:
#         complete[c] += 1
#     print(runner)
#     print(complete)
#     for r in runner:
#         runner[r] = runner[r] - complete[r]
#         if runner[r] != 0:
#             return r

# 실패율 _ 런타임 에러
# from collections import defaultdict
#
# def solution(N, stages):
#     answer = []
#     game = defaultdict(int)
#     for s in stages:
#         game[s] += 1
#     i = 1
#     M = len(stages)
#     while i <= N:
#         answer.append((i, game[i]/M))
#         print((i, game[i]/M))
#         M -= game[i]
#         i += 1
#
#     answer.sort(key=lambda x:-x[1])
#
#     result = []
#
#     for ans in answer:
#         result.append(ans[0])
#
#     return result
#
# print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))

# 실패율
# def solution(N, stages):
#     answer = []
#     i = 1
#     M = len(stages)
#     while i <= N:
#         answer.append((i,stages.count(i)/M))
#         M -= stages.count(i)
#         i += 1
#         if M == 0:
#             break
#
#     answer.sort(key=lambda x:-x[1])
#     result = []
#     for a in answer:
#         result.append(a[0])
#
#     if len(result) < N:
#         for num in range(result[0]+1, N+1):
#             result.append(num)
#     return result
#
# print(solution(4,[2,2,2,2,2]))

# 자연수 뒤집어 배열로 만들기
# def solution(n):
#     answer = []
#     num = str(n)
#     for i in range(len(num)-1,-1,-1):
#         answer.append(int(num[i]))
#     return answer

# 로또
# def solution(lottos, win_nums):
#     answer = []
#     grade = [6,6,5,4,3,2,1]
#     # 최고 순위
#     least = len(list(set(lottos) & set(win_nums)))
#     plus = lottos.count(0)
#     answer.append(grade[least+plus])
#     # 최저 순위
#     answer.append(grade[least])
#     return answer

# 행렬 이동 _ 시간 초과
# import copy
# def solution(rows, columns, queries):
#     # 배열 생성
#     arr = [[0]*(columns+2)]
#     for i in range(1, rows+1):
#         sub = []
#         for j in range(columns-1,-1,-1):
#             sub.append(i*columns-j)
#         arr.append([0]+sub+[0])
#     arr.append([0]*(columns+2))
#
#     # 번호 이동
#     min_v = []
#     for q in queries:
#         arr_copy = copy.deepcopy(arr)
#         minimal = 10000
#         a = q[0]
#         b = q[1]
#         c = q[2]
#         d = q[3]
#         points = [(a,b),(a,d),(c,d),(c,b)]
#         dir = [(0,1),(1,0),(0,-1),(-1,0)] # 이동방향
#         x, y = a, b
#         for d in dir:
#             while True:
#                 nx, ny = x + d[0], y + d[1]
#                 arr[nx][ny] = arr_copy[x][y]
#                 if arr[nx][ny] < minimal:
#                     minimal = arr[nx][ny]
#                 x, y = nx, ny
#                 if (x,y) in points:
#                     break
#         min_v.append(minimal)
#
#     return min_v
#
#
# print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))

# 행렬 이동2 _ 시간 초과 해결
# def solution(rows, columns, queries):
#     # 배열 생성
#     arr = [[0]*(columns+2)]
#     for i in range(1, rows+1):
#         sub = []
#         for j in range(columns-1,-1,-1):
#             sub.append(i*columns-j)
#         arr.append([0]+sub+[0])
#     arr.append([0]*(columns+2))
#
#     # 번호 이동
#     min_v = []
#     for q in queries:
#         arr_copy = []
#         for a in arr:
#             arr_copy.append(a[::])
#
#         minimal = 10000
#         a = q[0]
#         b = q[1]
#         c = q[2]
#         d = q[3]
#         points = [(a,b),(a,d),(c,d),(c,b)]
#         dir = [(0,1),(1,0),(0,-1),(-1,0)] # 이동방향
#         x, y = a, b
#         for d in dir:
#             while True:
#                 nx, ny = x + d[0], y + d[1]
#                 arr[nx][ny] = arr_copy[x][y]
#                 if arr[nx][ny] < minimal:
#                     minimal = arr[nx][ny]
#                 x, y = nx, ny
#                 if (x,y) in points:
#                     break
#         min_v.append(minimal)
#
#     return min_v
#
#
# print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))

# 다단계
# from collections import defaultdict
# # def solution(enroll, referral, seller, amount):
# #     chain = defaultdict(list)
# #     for idx in range(len(enroll)):
# #         if referral[idx] == '-':
# #             chain[enroll[idx]] = [0,0]
# #         else:
# #             chain[enroll[idx]] = [referral[idx],0]
# #
# #     print(chain)
# #
# #     for id in range(len(seller)):
# #         chain[seller[id]][1] = amount[id]*100
# #
# #     print(chain)
# #     for i in chain:
# #         print(chain[i])
# #         if chain[i][0] == 0:
# #             chain[i][1] = chain[i][1]*0.9
# #         else:
# #             chain[chain[i][0]][1] += chain[i][1]*0.1
# #             chain[i][1] = chain[i][1]*0.9
# #     print(chain)
# #     return
# #
# # print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))
#
# #
# from collections import defaultdict
# def solution(enroll, referral, seller, amount):
#     chain = defaultdict(list)
#     for idx in range(len(enroll)):
#         if referral[idx] == '-':
#             chain[enroll[idx]] = [0,0,0]
#         else:
#             chain[enroll[idx]] = [referral[idx],0,chain[referral[idx]][2]+1]
#
#     for id in range(len(seller)):
#         chain[seller[id]][1] = amount[id]*100
#
#     sorted_chain = sorted(chain.items(), key=lambda x:-x[1][2])
#     print(sorted_chain)
#
#     check = {}
#     for sc in sorted_chain:
#         check[sc[0]] = sc[1]
#     print(check)
#
#     for i in check:
#         print(i)
#         if check[i][0] == 0:
#             check[i][1] = check[i][1]*0.9
#         else:
#             check[check[i][0]][1] += check[i][1]*0.1
#             check[i][1] = check[i][1]*0.9
#     print(check)
#     return
#
# print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))

# 1
# def solution(absolutes, signs):
#     total = 0
#     for idx in range(len(absolutes)):
#         if signs[idx] == 'true':
#             total += int(absolutes[idx])
#         else:
#             total -= int(absolutes[idx])
#     return total
#
# print(solution([4,7,12], ['true','false','true']))

# 2
# from collections import deque
# def bracket(lis):
#     global cnt
#     q = deque()
#     s = lis.copy()
#     while s:
#         if q:
#             component = s.pop()
#             if component=='[' and q[-1]== ']':
#                 q.pop()
#             elif component=='(' and q[-1]== ')':
#                 q.pop()
#             elif component=='{' and q[-1]== '}':
#                 q.pop()
#             else:
#                 q.append(component)
#         else:
#             q.append(s.pop())
#     if len(q) == 0:
#         cnt += 1
#
# def solution(s):
#     q = deque(s)
#     global cnt
#     cnt = 0
#     for _ in range(len(q)-1):
#         bracket(q)
#         move = q.popleft()
#         q.append(move)
#     return cnt
#
# print(solution("[](){}"))

# 3
# from collections import defaultdict
# def to_zero(node, a, tree):
#     global answer
#     for idx in tree[node]:
#         if a[node] > 0:
#             while a[node] > 0:
#                 a[node] -= 1
#                 a[idx] += 1
#                 answer += 1
#
#         elif a[node] < 0:
#             while a[node] < 0:
#                 a[node] += 1
#                 a[idx] -= 1
#                 answer += 1
#     for i in tree:
#         if node in tree[i]:
#             tree[i].remove(node)
#     del tree[node]
#
# def solution(a, edges):
#     global answer
#     answer = 0
#     if sum(a) != 0:
#         answer = -1
#         return answer
#     tree = defaultdict(list)
#     for edge in edges:
#         tree[edge[0]].append(edge[1])
#         tree[edge[1]].append(edge[0])
#     copy_tree = tree.copy()
#
#     while len(copy_tree) != 1:
#         for t in copy_tree:
#             if len(copy_tree[t]) == 1:
#                 to_zero(t, a, tree)
#         copy_tree = tree.copy()
#
#     return answer
#
# print(solution([0,1,0], [[0,1],[1,2]]))

# 3
# from collections import defaultdict
# def solution(a, edges):
#     answer = 0
#     if sum(a) != 0:
#         answer = -1
#         return answer
#     nums = defaultdict(int)
#     nodes = []
#     for edge in edges:
#         nums[edge[0]] += 1
#         nums[edge[1]] += 1
#     for k,v in nums.items():
#         nodes.append((k,v))
#     nodes.sort(key=lambda x:-x[1])
#
#     for idx in range(len(nodes)-1,0,-1):
#         if a[nodes[idx][0]] > 0:
#             while a[nodes[idx][0]] > 0:
#                 a[nodes[idx][0]] -= 1
#                 for edge in edges:
#                     if nodes[idx][0] == edge[0]:
#                         next_node = edge[1]
#                         edges.remove(edge)
#                     elif nodes[idx][0] == edge[1]:
#                         next_node = edge[0]
#                         edges.remove(edge)
#                 a[next_node] += 1
#                 answer += 1
#         elif a[nodes[idx][0]] < 0:
#             while a[nodes[idx][0]] < 0:
#                 a[nodes[idx][0]] += 1
#                 for edge in edges:
#                     if nodes[idx][0] == edge[0]:
#                         next_node = edge[1]
#                         edges.remove(edge)
#                     elif nodes[idx][0] == edge[1]:
#                         next_node = edge[0]
#                         edges.remove(edge)
#                 a[next_node] -= 1
#                 answer += 1
#     return answer
#
#
# print('answer', solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]]))

# 3 _ 원재의 솔루션
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)

def dfs(cur, check, node, a):
    global answer
    check[cur] = False

    for i in node[cur]:
        if check[i]:
            dfs(i, check, node, a)
            a[cur] += a[i]
            answer += abs(a[i])

answer = 0
def solution(a, edges):
    max_pos = (0, 0)
    check = [True for _ in range(len(a))]
    for i, val in enumerate(a):
        if abs(val) > abs(max_pos[1]):
            max_pos = (i, val)

    node = defaultdict(list)
    for u, v in edges:
        node[u].append(v)
        node[v].append(u)
    dfs(max_pos[0], check, node, a)
    return -1 if a[max_pos[0]] else answer