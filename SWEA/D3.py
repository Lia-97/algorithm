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

# [S/W 문제해결 기본] 8일차 - 암호문3
for tc in range(1, 11):
    N = int(input())
    password = list(map(int, input().split()))
    num = int(input())
    control = list(map())