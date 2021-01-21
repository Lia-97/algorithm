# # 10872번 (팩토리얼)
# N = int(input())
# def fac(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     return n * fac(n-1)
# print(fac(N))

# # 10870번 (피보나치 수 5)
# x = int(input())
# def fibo(x):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     elif x >= 2:
#         return fibo(x-1) + fibo(x-2)
#
# print(fibo(x))

# 2447번 (별 찍기 - 10)
def star(N):
    print('*' * N)