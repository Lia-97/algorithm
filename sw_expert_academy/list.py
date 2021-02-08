# gravity
# N = int(input())
# for x in range(1, N+1):
#     num =int(input())
#     box = list(map(int, input().split()))
#     lis = []
#     for i in range(len(box)):
#         cnt = 0
#         for j in range(i+1, len(box)):
#             if box[i] > box[j]:
#                 cnt += 1
#         lis.append(cnt)
#     print(f'#{x} {max(lis)}')

# view
T = 10
for _ in range(T):
    input()
    floor = list(map(int, input().split()))
    cnt = 0
    for i in range(2, len(floor) - 2):
        if max(floor[i-2:i+3]) == floor[i]:
            cnt += (floor[i] - max([floor[i-2], floor[i-1], floor[i+1], floor[i+2]]))
    print(cnt)