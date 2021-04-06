# 1991번 (트리 순회)
# def preorder(idx):
#     global pre_ans
#     pre_ans += chr(idx+64)
#     if left[idx] != 0:
#         preorder(left[idx])
#     if right[idx] != 0:
#         preorder(right[idx])
#
# def inorder(idx):
#     global in_ans
#     if left[idx] != 0:
#         inorder(left[idx])
#     in_ans += chr(idx + 64)
#     if right[idx] != 0:
#         inorder(right[idx])
#
# def postorder(idx):
#     global post_ans
#     if left[idx] != 0:
#         postorder(left[idx])
#     if right[idx] != 0:
#         postorder(right[idx])
#     post_ans += chr(idx + 64)
#
# N = int(input()) # 노드의 개수
# left, right = [0]*(N+1), [0]*(N+1)
# for _ in range(N):
#     alpha = input().split()
#     pa = ord(alpha[0]) - 64
#     if alpha[1] != '.':
#         ch1 = ord(alpha[1]) - 64
#         left[pa] = ch1
#     if alpha[2] != '.':
#         ch2 = ord(alpha[2]) - 64
#         right[pa] = ch2
#
# pre_ans = ''
# in_ans = ''
# post_ans = ''
#
# preorder(1)
# inorder(1)
# postorder(1)
#
# print(pre_ans)
# print(in_ans)
# print(post_ans)

# 2263번 (트리의 순회)
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
tree = [0]*(n+1)

while True:
    pass

