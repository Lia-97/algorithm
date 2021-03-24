# 1100번 (하얀 칸)
# arr = [] # 0흰, 1검
# for i in range(8):
#     if i%2:
#         arr.append([1,0,1,0,1,0,1,0])
#     else:
#         arr.append([0,1,0,1,0,1,0,1])
#
# chess = [list(input()) for _ in range(8)]
# cnt = 0
#
# for i in range(8):
#     for j in range(8):
#         if arr[i][j] == 0 and chess[i][j] == 'F':
#             cnt += 1
# print(cnt)

# 1966번 (프린터 큐)
from collections import deque
T = int(input()) # 테스트케이스 수
N, M = map(int, input().split()) # 문서 개수, 문서 위치
papers = list(map(int,input().split())) # 문서의 중요도
q = deque()
cnt = 0
for i, paper in enumerate(papers):
    q.append((paper,i))

while True:
    num, idx = q.popleft()
    if num >=  and idx == M:
        cnt += 1
        break
    elif num >=  and idx != M:
        continue
    else:
        q.append(num)

print(cnt)