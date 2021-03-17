# 요리사
from itertools import combinations
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    foods = [[0]*(N+2)]
    for _ in range(N):
        foods.append([0]+list(map(int, input().split()))+[0])
    foods.append([0]*(N+2))

    lis = list(combinations(list(range(1, N + 1)), N // 2))
    part_a = lis[:len(lis)//2]
    part_b = lis[len(lis)//2:][::-1]
    print(part_a, part_b)

    diff = 20000
    for i in range(len(part_a)):
        S = foods[part_a[i][0],part_b[i][0]]+foods[part_b[i][0], part_a[i][0]]
        if S < diff:
            diff = S

    print(diff)
