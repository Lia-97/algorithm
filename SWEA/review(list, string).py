# Gravity
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     box = list(map(int, input().split()))
#     max_cnt = 0
#     for i in range(N-1):
#         cnt = 0
#         for j in range(i+1, N):
#             if box[i] > box[j]:
#                 cnt += 1
#             if cnt > max_cnt:
#                 max_cnt = cnt
#     print(f'#{tc} {max_cnt}')

# View
# def max_v(lis):
#     max_val = lis[0]
#     for l in lis:
#         if l > max_val:
#             max_val = l
#     return max_val
#
# for tc in range(1, 11):
#     N = int(input())
#     buildings = list(map(int, input().split()))
#     total = 0
#     for i in range(2, N-2):
#         if max_v(buildings[i-2:i+3]) == buildings[i]:
#             diff = float('inf')
#             for building in buildings[i-2:i]+buildings[i+1:i+3]:
#                 if buildings[i]-building < diff:
#                     diff = buildings[i]-building
#             total += abs(diff)
#     print(f'#{tc} {total}')
