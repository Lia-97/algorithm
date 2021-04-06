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

# subtree _ 실패
# T = int(input())
# for tc in range(1, T+1):
#     E, N = map(int, input().split()) # 간선 개수, 루트로 할 노드
#     pa = [0] * (E+2)
#     node = list(map(int, input().split()))
#     for i in range(E):
#         n1, n2 = node[2*i], node[2*i+1]
#         pa[n2] = n1 # 자식을 인덱스로 부모 저장
#
#     check = N
#     cnt = 0
#     print(pa)
#     while True:
#         if check not in pa:
#             break
#         cnt += 1
#         check = pa.index(check)
#
#     print(f'#{tc} {cnt}')

# subtree _ 정답
# def inorder(node):
#     global cnt
#     if node == 0:
#         return
#     cnt += 1
#     inorder(left[node])
#     inorder(right[node])
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split()) # 간선 개수, 루트로 할 노드
#     node = list(map(int, input().split()))
#     left = [0] * (V+2)
#     right = [0] * (V+2)
#     cnt = 0
#     for i in range(V):
#         pa = node[2*i]
#         chi = node[2*i+1]
#         if left[pa]:
#             right[pa] = chi
#         else:
#             left[pa] = chi
#
#     inorder(E)
#     print(f'#{tc} {cnt}')

# 이진탐색
# def Tree(root):
#     global number
#     if root <= V:
#         Tree(root*2)
#         tree[root] = number
#         number += 1
#         Tree(root*2+1)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     V = int(input())
#     tree = [0]*(V+1)
#     number = 1
#
#     Tree(1)
#     ans1 = tree[1]
#     ans2 = tree[V//2]
#     print(f'#{tc} {ans1} {ans2}')

# 이진 힙

# 노드의 합
# T = int(input())
# for tc in range(1, T+1):
#     N, M, L = map(int, input().split()) # 노드 수, 리프 노드 수, 값을 출력할 노드 번호
#     tree = [0]*(N+1)
#     for _ in range(M):
#         node, val = map(int, input().split()) # 노드 번호, 값
#         tree[node] = val
#
#     i=N//2
#     while True:
#         if i == 0:
#             break
#         if 2*i+1 <= N:
#             tree[i] = tree[2*i] + tree[2*i+1]
#         else:
#             tree[i] = tree[2*i]
#         i -= 1
#
#     print(f'#{tc} {tree[L]}')

# 사칙연산 _ 실패
# def inorder(idx):
#     global result
#     left = idx*2
#     right = idx*2+1
#     if left <= N:
#         inorder(left)
#
#     if type(tree[idx]) == int and len(result)==0:
#         result.append(tree[idx])
#     elif type(tree[idx]) != int:
#         result.append(tree[idx])
#     elif type(tree[idx]) == int and len(result) != 0:
#         calc = result.pop()
#         num = result.pop()
#         if calc == '-':
#             result.append((num-tree[idx]))
#         elif calc == '+':
#             result.append((num + tree[idx]))
#         elif calc == '/':
#             result.append((num / tree[idx]))
#         elif calc == '*':
#             result.append((num * tree[idx]))
#
#     if right <= N:
#         inorder(right)
#
# N = int(input())
# tree = [0]*(N+1)
# result = []
# for _ in range(N):
#     info = input().split()
#     if len(info) > 2:
#         tree[int(info[0])] = info[1]
#         tree[int(info[2])] = 0
#         tree[int(info[3])] = 0
#     else:
#         tree[int(info[0])] = int(info[1])
#
# inorder(1)
# print(result.pop())

# 사칙연산 _ 정답
# def solve(a, b, c):
#     if b == '-':
#         return a-c
#     elif b == '+':
#         return a+c
#     elif b == '*':
#         return a*c
#     elif b == '/':
#         return a/c
#
# for tc in range(1, 11):
#     N = int(input())
#     tree = [0]*(N+1)
#     calc = []
#     for _ in range(N):
#         info = input().split()
#         if len(info) > 2:
#             calc.append(list(info))
#         else:
#             tree[int(info[0])] = int(info[1])
#
#     for c in calc[::-1]:
#         tree[int(c[0])] = solve(tree[int(c[2])],c[1] ,tree[int(c[3])])
#
#     print(f'#{tc} {int(tree[1])}')
