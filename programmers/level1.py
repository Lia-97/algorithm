# # K번째수
# def solution(array, commands):
#     answer = []
#     for command in commands:
#         new_array = array[command[0]-1:command[1]]
#         new_array.sort()
#         answer.append(new_array[command[2]-1])
#     return answer
#
# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# # 문자열 내 p와 y의 개수
#
# def solution(s):
#     sentence = s.lower()
#     if sentence.count('p') == sentence.count('y'):
#         return True
#     else:
#         return False
#
# print(solution('Pyy'))

# # 두 정수 사이의 합
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

# # 두 정수 사이의 합 (또 다른 풀이)
#
# def solution(a, b):
#     if a > b:
#         a, b = b, a
#     return sum(range(a, b+1))

# # 같은 숫자는 싫어
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

# # 수박수박수박수박수박수?
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

# # 자릿수 더하기
#
# def solution(n):
#     total = 0
#     for i in str(n):
#         total += int(i)
#     return total

# # 시저 암호
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

# # 소수 찾기
#
# def solution(n):
#     cnt = 0
#     num = 0
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             if i % j == 0:
#                 cnt += 1
#                 if cnt == 2:
#                     num += 1
#     return num
#
# print(solution(10))
# print(solution(5))

# # 문자열 다루기 기본
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

# # 문자열 다루기 isdigit() 함수 사용해보기
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

# # 정수 내림차순으로 배치하기
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