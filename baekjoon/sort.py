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