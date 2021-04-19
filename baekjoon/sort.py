# 11650번 (좌표 정렬하기)
# import sys
# N = int(sys.stdin.readline())
# dots = []
# for _ in range(N):
#     x, y = map(int, sys.stdin.readline().split())
#     dots.append((x,y))
# dots.sort(key=lambda x:(x[0], x[1]))
# for dot in dots:
#     print(dot[0], dot[1])

# 1181번 (단어 정렬)
# N = int(input())
# words = []
# for _ in range(N):
#     words.append(input())
# words = list(set(words))
# words.sort(key=lambda x:(len(x), x))
# for word in words:
#     print(word)

# 10814번 (나이순 정렬)
# import sys
# N = int(sys.stdin.readline())
# members = []
# for i in range(N):
#     age, name = sys.stdin.readline().split()
#     members.append((int(age), name))
# members.sort(key=lambda x:(x[0]))
# for member in members:
#     print(member[0], member[1])

# 5052번 (전화번호 목록)
# import sys
#
# def check(numbers):
#     global ans
#     for i in range(len(numbers)-1):
#         if numbers[i+1][:len(numbers[i])] == numbers[i]:
#             ans = 'NO'
#             return
#
# T = int(input())
# for _ in range(T):
#     n = int(sys.stdin.readline())
#     numbers = []
#     ans = 'YES'
#     for _ in range(n):
#         numbers.append(sys.stdin.readline().strip())
#     numbers.sort()
#     check(numbers)
#     print(ans)

# 1026번 (보물)
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# A.sort()
# B.sort(reverse=True)
# ans = 0
# for idx in range(len(A)):
#     ans += A[idx]*B[idx]
# print(ans)

# 10815번 (숫자 카드) _ 시간 초과
# import sys
# N = int(sys.stdin.readline())
# cards = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# judges = list(map(int, sys.stdin.readline().split()))
# for idx in range(M):
#     if judges[idx] in cards:
#         judges[idx] = 1
#     else:
#         judges[idx] = 0
# print(' '.join(list(map(str, judges))))

# 10815번 (숫자 카드) _ 이분탐색으로 풀기

# 11004번 (K번째 수)
# import sys
# N, K = map(int, sys.stdin.readline().split())
# A = list(map(int, sys.stdin.readline().split()))
# A.sort()
# print(A[K-1])