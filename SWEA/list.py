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
# T = 10
# # 10번의 테스트케이스
# for tc in range(1, T+1):
#     n = input()
#     # n 개의 길이를 갖는 list인 floor
#     floor = list(map(int, input().split()))
#     cnt = 0
#     # floor[2] 부터 floor[len(floor)-2] 를 순회한다.
#     for i in range(2, len(floor) - 2):
#         max_val = 0
#         # 특정 세대의 앞 2개, 뒤 2개 중 가장 높은 세대의 층을 구한다.
#         for j in floor[i-2:i+3]:
#             if j > max_val:
#                 max_val = j
#         # 5개 세대 중에서 가운데 있는 세대의 층이 가장 높다면
#         if max_val == floor[i]:
#             second_max_val = 0
#             # 두번째로 높은 세대의 층을 구해서
#             for l in [floor[i - 2], floor[i - 1], floor[i + 1], floor[i + 2]]:
#                 if l > second_max_val:
#                     second_max_val = l
#             # 그 차 만큼 cnt 에 더해준다.
#             cnt += floor[i] - second_max_val
#     print(f'#{tc} {cnt}')

# 구간합
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     a = list(map(int, input().split()))
#     # a 리스트의 0번째 부터 M 개의 원소를 각각 최댓값, 최솟값으로 설정한다.
#     max_val = sum(a[0:M])
#     min_val = sum(a[0:M])
#     # 연속된 M 개의 수의 합을 구할 것이기 때문에 범위는 range(N-M+1)
#     for i in range(N-M+1):
#         # i 인덱스부터 M 개 숫자의 합을 구해 각각 최댓값과 최솟값을 구한다.
#         if sum(a[i:i+M]) > max_val:
#             max_val = sum(a[i:i+M])
#         if sum(a[i:i+M]) < min_val:
#             min_val = sum(a[i:i+M])
#
#     print(f'#{tc} {max_val-min_val}')

# min max
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     # 리스트 numbers의 첫번째 원소를 max 값과 min 값으로 설정해준다.
#     max_val = numbers[0]
#     min_val = numbers[0]
#     # 리스트 numbers를 순회하면서 max_val 보다 큰 값은 max 로, min_val 보다 작은 값은 min 으로 계속 바꿔준다.
#     for number in numbers:
#         if number > max_val:
#             max_val = number
#         if number < min_val:
#             min_val = number
#     print(f'#{tc} {max_val-min_val}')

# 숫자 카드_카운팅 정렬으로 풀기
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     nums = input()
#     # 카운팅 정렬을 위해 nums 의 범위(0 이상 9 이하)만큼 0값을 가지는 리스트를 만든다.
#     cnt = [0] * 10
#     # 입력받은 nums 를 순회하면서 cnt에서 num 값을 인덱스로 가지는 위치에 1씩 더한다.
#     for num in nums:
#         cnt[int(num)] += 1
#     # max 값을 cnt의 첫번째 원소로 초기화 해주고, card 의 수를 0으로 초기화한다.
#     max = cnt[0]
#     card_cnt = 0
#     # cnt 를 순회하면서 최댓값 보다 크거나 같으면(카드의 갯수가 같을 시, 더 큰 값을 반환하기 위해) max 와 card_cnt 를 변경해준다.
#     for i in range(0,10):
#         if cnt[i] >= max:
#             max = cnt[i]
#             card_cnt = i
#     print(f'#{tc} {card_cnt} {max}')

# 숫자 카드_딕셔너리로 풀기
# t = int(input())
#
# for tc in range(1, t + 1):
#
#     n = int(input())
#     card = list(map(int, input()))
#
#     result = {}
#     for i in range(0, n):
#         if card[i] in result.keys():
#             result[card[i]] += 1
#         else:
#             result[card[i]] = 1
#
#     max_k = 0
#     max_v = 0
#     for k, v in result.items():
#         if v > max_v:
#             max_k = k
#             max_v = v
#         elif v == max_v:
#             if k > max_k:
#                 max_k = k
#
#     print(f'#{tc} {max_k} {max_v}')

# 전기버스
# T = int(input())
# for tc in range(1, T+1):
#     K, N, M = map(int, input().split())
#     stop= list(map(int, input().split()))
#     bus = 0
#     cnt = 0
#     while bus < N:
#         bus += K
#         if bus >= N:
#             break
#         if bus in stop:
#             cnt += 1
#         else:
#             inter = list(set(range(bus-K+1, bus)) & set(stop))
#             if len(inter) == 0 :
#                 cnt = 0
#                 break
#             else:
#                 bus = inter[len(inter)-1]
#                 cnt += 1
#     print(f'#{tc} {cnt}')

# 간단한 소인수분해
# T = int(input())
# for tc in range(1, T+1):
#     lis = [0] * 12
#     N = int(input())
#     for i in [2, 3, 5, 7, 11]:
#         while N % i == 0:
#             lis[i] += 1
#             N = N // i
#     a = lis[2]
#     b = lis[3]
#     c = lis[5]
#     d = lis[7]
#     e = lis[11]
#     print(f'#{tc} {a} {b} {c} {d} {e}')

# 현주의 상자 바꾸기
# T = int(input())
# for tc in range(1, T+1):
#     N, Q = map(int, input().split())
#     zero_list = [0] * N
#     for q in range(1, Q+1):
#         L, R = map(int, input().split())
#         for i in range(L-1,R):
#             zero_list[i] = q
#     result = ' '.join(map(str, zero_list))
#     print(f'#{tc} {result}')

# 두 개의 숫자열 _ 정석
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     result = []
#     if N > M:
#         fix = list(map(int, input().split()))
#         move = list(map(int, input().split()))
#     else:
#         N, M = M, N
#         move = list(map(int, input().split()))
#         fix = list(map(int, input().split()))

# 두 개의 숫자열 _ [0]*N
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     max_val = []
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     if N > M:
#         for i in range(N-M+1):
#             result = [0] * N
#             result[i:i+M] = (b for b in B)
#             total = 0
#             for j in range(N):
#                 total += result[j] * A[j]
#             max_val.append(total)
#
#     if M > N:
#         for i in range(M-N+1):
#             result = [0] * M
#             result[i:i+N] = (a for a in A)
#             total = 0
#             for j in range(M):
#                 total += result[j] * B[j]
#             max_val.append(total)
#
#     answer = max_val[0]
#     for m in max_val:
#         if m > answer:
#             answer = m
#     print(f'#{tc} {answer}')

# 두 개의 숫자열 _ 원재
#
# def arr_mul(a,b):
#     ans=0
#     for n,m in zip(a,b):
#         ans+=n*m
#     return ans
#
# T=int(input())
# for tc in range(1,T+1):
#     N, M= map(int,input().split())
#     A=list(map(int,input().split()))
#     B=list(map(int,input().split()))
#
#     # A가 더 작으면 A의 list가 더 큰걸로 바꿔준다.
#     if N < M :
#         N,M=M,N
#         A,B=B,A
#
#     max_sum=float('-inf')
#     for i in range(N-M+1):
#         sub_sum=arr_mul(A[i:i+M],B)
#         if max_sum < sub_sum:
#             max_sum=sub_sum
#
#     print(f'#{tc} {max_sum}')

# 숫자를 정렬하자
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     for i in range(N-1):
#         for j in range(i+1, N):
#             if numbers[i] > numbers[j]:
#                 numbers[i], numbers[j] = numbers[j], numbers[i]
#     numbers = list(map(str, numbers))
#     result = ' '.join(numbers)
#     print(f'#{tc} {result}')

# 삼성시의 버스 노선
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     result = []
#     setting = [0] * 5001
#     for n in range(N):
#         A, B = map(int, input().split())
#         for i in range(A,B+1):
#             setting[i] += 1
#     P = int(input())
#     for _ in range(P):
#         j = int(input())
#         result.append(str(setting[j]))
#
#     result = ' '.join(result)
#     print(f'#{tc} {result}')

# Flatten
# for tc in range(1, 11):
#     dump = int(input())
#     height = list(map(int, input().split()))
#     for _ in range(dump):
#         max_val = height[0]
#         min_val = height[0]
#         for h in height:
#             if h > max_val:
#                 max_val = h
#             if h < min_val:
#                 min_val = h
#         max_index = height.index(max_val)
#         min_index = height.index(min_val)
#         height[max_index] -= 1
#         height[min_index] += 1
#
#     max_ans = height[0]
#     min_ans = height[0]
#     for h in height:
#         if h > max_ans:
#             max_ans = h
#         if h < min_ans:
#             min_ans = h
#     print(f'#{tc} {max_ans - min_ans}')