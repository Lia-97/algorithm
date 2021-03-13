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