# 3-1 거스름돈
"""
당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이
무한히 존재한다고 가정한다. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
"""

# 나의 풀이
# def solution(N):
#     a = N // 500
#     b = (N % 500) // 100
#     c = ((N % 500) % 100) // 50
#     d = (((N % 500) % 100) % 50) // 10
#
#     return a+b+c+d
#
# print(solution(1260))

# 답안 예시
# def solution(N):
#     count = 0
#     coin_type = [500, 100, 50, 10]
#     for coin in coin_type:
#         count += N // coin
#         N = N % coin
#
#     return count
#
# print(solution(1260))

# 3-2 큰 수의 법칙
"""
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙.
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
입력으로 주어지는 K는 항상 M보다 작거나 같다.
"""

N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[-1]
second = data[-2]
result = 0

if first == second:
    result = first * M
else:
    while True:
        if M == 0:
            break
        for _ in range(K):
            result += first
            M -= 1
            if M == 0:
                break
        result += second
        M -= 1

print(result)






