# 연습문제
# 노드 6개, 간선 5개, 1 2 1 3 2 4 3 5 3 6

"""
1. 부모 노드를 인덱스로 자식 번호를 저장
부모 p, 자식 c
if ch1[p] == 0: # ch1이 비어 있으면 거기에 넣고
    ch1[p] = c
else: # 아니면 ch2 자리에 넣어라
    ch2[p] = c

2. 자식 노드를 인덱스로 부모 번호를 저장 --> root 를 찾을 때 사용
par[c] = p
"""

"""
5 4
2 1 2 4 4 3 4 5
"""

# def preorder(n):
#     if n > 0:
#         print(n, end=' ')
#         preorder(left[n])
#         preorder(right[n])
#
# # 1번 부터 v번 까지 노드, E 개의 간선
# V, E = map(int, input().split())
# edge = list(map(int, input().split()))
#
# left = [0]*(V+1) # 부모를 인덱스로 왼쪽 자식번호 저장
# right = [0]*(V+1) # 부모를 인덱스로 오른쪽 자식번호 저장
#
# pa = [0]*(V+1) # 자식을 인덱스로 부모번호 저장
#
# for i in range(E):
#     n1, n2 = edge[i*2], edge[i*2+1]
#     if left[n1] == 0: # 왼쪽 자식이 없으면
#         left[n1] = n2 # 부모를 인덱스로 자식번호 저장
#     else: # 왼쪽 자식이 있으면
#         right[n1] = n2 # 부모를 인덱스로 자식 번호 저장
#
#     pa[n2] = n1 # 자식을 인덱스로 부모를 저장
#
# # 루트 찾기
# root=0
# for i in range(1, V+1):
#     if pa[i] == 0: # 부모가 없으면 root
#         root = i
#         break
#
# preorder(root)

# 중위순회
# def inorder(tree, idx):
#     result = ''
#
#     left = idx*2
#     right = idx*2+1
#
#     if left < len(tree):
#         result += inorder(tree, left)
#
#     result += tree[idx]
#
#     if right < len(tree):
#         result += inorder(tree, right)
#
#     return result
#
#
# for tc in range(1, 11):
#     N = int(input()) # 정점의 총 수
#     tree = [0]*(N+1)
#     for _ in range(N):
#         alpha = input().split()
#         tree[int(alpha[0])] = alpha[1]
#
#     print(f'#{tc} {inorder(tree, 1)}')

# 중위순회_ 두번째 풀이
# def inorder(N, idx):
#     result = ''
#
#     left = idx*2
#     right = idx*2+1
#
#     if left < N+1:
#         result += inorder(N, left)
#
#     result += tree[idx]
#
#     if right < N+1:
#         result += inorder(N, right)
#
#     return result
#
#
# for tc in range(1, 11):
#     N = int(input()) # 정점의 총 수
#     tree = [0]*(N+1)
#     for _ in range(N):
#         alpha = input().split()
#         tree[int(alpha[0])] = alpha[1]
#     print(tree)
#     print(f'#{tc} {inorder(N, 1)}')