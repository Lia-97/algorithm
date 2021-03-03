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
#         else:
#             lost.remove(i)
#             reserve.remove(i)
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
