# 물놀이를 가자
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M  = map(int, input().split()) # 행개수, 열개수
    arr = [list(input()) for _ in range(N)]
    dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                