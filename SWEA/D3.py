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
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = []
#     for _ in range(N):
#         arr.append(list(map(int, input())))
#
#     total = 0
#     for i in range(N):
#         total += sum(arr[i][abs(N//2-i) : N-abs(N//2-i)])
#     print(f'#{tc} {total}')

# 보충학습과 평균
# T = int(input())
# for tc in range(1, T+1):
#     score = list(map(int, input().split()))
#     for i in range(len(score)):
#         if score[i] < 40:
#             score[i] = 40
#     print(f'#{tc} {int(sum(score)/len(score))}')