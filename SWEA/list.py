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

# Flatten _ while 문으로 풀기 (원재)
# T=10
# for tc in range(1,T+1):
#     dump=int(input())
#     boxes=list(map(int,input().split()))
#
#     while dump > 0:
#         # (index, val)
#         min_val=boxes[0]
#         max_val=boxes[0]
#         # 최고, 최저 탐색
#         for val in boxes:
#             if max_val < val:
#                 max_val=val
#             if min_val > val:
#                 min_val=val
#         boxes[boxes.index(max_val)]-=1
#         boxes[boxes.index(min_val)]+=1
#         dump-=1
#
#         max_ans=boxes[0]
#         min_ans=boxes[0]
#         for box in boxes:
#             if max_ans<box:
#                 max_ans=box
#             if min_ans>box:
#                 min_ans=box
#         if max_ans - min_ans<=1:
#             break
#     print(f'#{tc} {max_ans-min_ans}')

# 당근 수확
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     carrot = list(map(int, input().split()))
#     result = []
#     for i in range(N):
#         a = sum(carrot[:i+1])
#         b = sum(carrot[i+1:])
#         result.append((i+1, abs(a-b)))
#     work = 0
#     diff = float('inf')
#     for r in result:
#         if r[1] < diff:
#             work = r[0]
#             diff = r[1]
#     print(f'#{tc} {work} {diff}')

# 당근 수확 _ 2
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     # 일꾼 a, b의 수확량
#     a, b = 0, 0
#
#     carrot_list = list(map(int, input().split()))
#
#     for carrot in carrot_list:
#         b += carrot
#
#     min_diff = abs(b - a)
#     for i in range(N):
#         a += carrot_list[i]
#         b -= carrot_list[i]
#         if abs(b - a) > min_diff:
#             break
#         else:
#             min_diff = abs(b - a)
#
#     # i-1번째 인덱스가 첫 번째 일꾼의 최종 구역. 다만 정답은 1 번째부터 세므로 그대로 i 출력
#
#     print(f'#{tc} {i} {min_diff}')

# 당근밭 옆 고구마밭 _ 미완
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = [-1] + list(map(int, input().split())) + [-1]
#     root_len = 0
#     total = 0
#     result = []
#     for i in range(1, len(numbers)):
#         if numbers[i] > numbers[i-1]:
#             root_len += 1
#             total += numbers[i]
#         else:
#             result.append((root_len, total))
#             if numbers[i] == -1:
#                 break
#             else:
#                 if numbers[i] < numbers[i+1]:
#                     root_len = 1
#                     total = numbers[i]
#                 else:
#                     root_len = 0
#                     total = 0
#     print(result)
#
#     # cnt = 0
#     # max = 0
#     # for i in result:
#     #     if i[0] != 0:
#     #         cnt += 1
#     #     if i[0] > max:
#     #         max = i[0]
#
#     # cnt = 0
#     # max = float('-inf')
#     # for i in result:
#     #     if i[0] != 0:
#     #         cnt += 1
#     #     if i[1] > max:
#     #         max = i[1]
#     # print(f'#{tc} {cnt} {max}')

# 당근의 개수
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     max = float('-inf')
#     order = 0
#     for number in enumerate(numbers):
#         if number[1] > max:
#             order = number[0]
#             max = number[1]
#     print(f'#{tc} {order+1} {max}')

# 연속한 1의 개수
# T= int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = input()
#     cnt = 0
#     max_cnt = 0
#     for number in numbers:
#         if number == '1':
#             cnt += 1
#             if cnt > max_cnt:
#                 max_cnt = cnt
#         else:
#             cnt = 0
#     print('#{} {}'.format(tc, max_cnt))

# 점점 커지는 당근의 개수
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     carrots = list(map(int, input().split()))
#     cnt = 1
#     max_cnt = 1
#     for i in range(1, N):
#         if carrots[i] > carrots[i-1]:
#             cnt += 1
#             if cnt > max_cnt:
#                 max_cnt = cnt
#         else:
#             cnt = 1
#     print('#{} {}'.format(tc, max_cnt))

# 이웃한 요소와의 차의 절댓값의 합
# T = int(input())
# dir1 = [0,0,1,-1]
# dir2 = [1,-1,0,0]
# for tc in range(1, T+1):
#     num = int(input())
#     arr = []
#     total = 0
#     for _ in range(num):
#         lis = arr.append(list(map(int, input().split())))
#     for i in range(num):
#         for j in range(num):
#             for l in range(4):
#                 r = i + dir1[l]
#                 c = j + dir2[l]
#                 if 0 <= r < num and 0<= c < num:
#                     total += abs(arr[i][j] - arr[r][c])
#     print(f'#{tc} {total}')

# 부분집합의 합이 0 이 되는 프로그램
# T = int(input())
# for tc in range(1, T+1):
#     arr = list(map(int, input().split()))
#     n = len(arr)
#     for i in range(1<<n):
#         ans = []
#         for j in range(n):
#             if i & (1<<j):
#                 ans.append(arr[j])
#         if sum(ans) == 0 and len(ans) != 0:
#             result = 1
#             break
#         else:
#             result = 0
#     print(f'#{tc} {result}')

# 달팽이 숫자
# T = int(input())
# dr = [0,1,0,-1]
# dc = [1,0,-1,0]
# for tc in range(1, T+1):
#     num = int(input())
#     arr = []
#     for _ in range(num):
#         arr.append([0] * num)
#     i = 0
#     j = -1
#     k = 0
#     change = 1
#     while change <= num * num:
#         r = i + dr[k]
#         c = j + dc[k]
#         if 0 <= r < num and 0 <= c < num and arr[r][c] == 0:
#             i = r
#             j = c
#             arr[i][j] = change
#             change += 1
#         else:
#             k = (k+1) % 4
#     print(f'#{tc}')
#     for array in arr:
#         print(' '.join(map(str, array)))

# [S/W 문제해결 기본] 2일차 - Sum
# for tc in range(1, 11):
#     input()
#     arr = []
#     for _ in range(100):
#         arr.append(list(map(int, input().split())))
#
#     result = []
#     result2 = []
#     total3 = 0
#     total4 =0
#     for i in range(len(arr)):
#         total = 0
#         total2 = 0
#         for j in range(len(arr[i])):
#             total += arr[i][j]
#             total2 += arr[j][i]
#             if i == j:
#                 total3 += arr[i][j]
#             if j == len(arr)-1-i:
#                 total4 += arr[i][j]
#
#         result.append(total)
#         result2.append(total2)
#
#     max_val1 = 0
#     for r in result:
#         if r > max_val1:
#             max_val1 = r
#     max_val2 = 0
#     for r2 in result2:
#         if r2 > max_val2:
#             max_val2 = r2
#     ans = 0
#     for i in [max_val1, max_val2, total3, total4]:
#         if i > ans:
#             ans = i
#     print(f'#{tc} {ans}')

# [S/W 문제해결 기본] 2일차 - Sum
# 가장 큰 수 구하는 함수 정의하기
# def Max_Sum():
#     pass
# input 받아서 위에서 정의한 함수 사용하기

# [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기
# T = int(input())
# for tc in range(1, T+1):
#     num = int(input())
#     for _ in range(num):
#         int

# [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색
# def search(long, find):
#     start = 1
#     end = long
#     cnt = 0
#     while start <= end:
#         middle = (start + end)//2
#         if middle == find:
#             cnt += 1
#             break
#         elif middle > find:
#             end = middle
#             cnt += 1
#         else:
#             start = middle
#             cnt += 1
#     return cnt
#
# T = int(input())
# for tc in range(1, T+1):
#     P, A, B = map(int, input().split())
#     cnt_A = search(P, A)
#     cnt_B = search(P, B)
#     if cnt_A < cnt_B:
#         ans = 'A'
#     elif cnt_A > cnt_B:
#         ans = 'B'
#     else:
#         ans = 0
#     print('#{} {}'.format(tc, ans))

# [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬
# T= int(input())
# for tc in range(1, T+1):
#     long = int(input())
#     numbers = list(map(int, input().split()))
#     # 선택정렬로 작은 수부터 오름차순으로 정렬한다.
#     for i in range(long-1):
#         min_idx = i
#         for j in range(i+1, long):
#             if numbers[j] < numbers[min_idx]:
#                 min_idx = j
#         numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
#
#     # 내림차순 정렬된 새로운 리스트를 만든다.
#     reverse_numbers = numbers[::-1]
#     # long 길이를 가지는 임의의 리스트를 만든다. (값을 바꿔나갈 예정)
#     result = [0] * long
#     half = long // 2
#     # result 의 짝수번째 인덱스에 큰 값부터 넣어준다.
#     for i in range(0,half):
#         result[2*i] = reverse_numbers[i]
#     # result 의 홀수번째 인덱스에 작은 값부터 넣어준다.
#     for j in range(0,long-half):
#         result[2*j+1] = numbers[j]
#
#     ans = result[:10]
#     ans = ' '.join(list(map(str, ans)))
#     print('#{} {}'.format(tc, ans))

# [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합
# def sum_val(lis):
#     total = 0
#     for l in lis:
#         total += l
#     return total
#
# def len_val(lis):
#     long = 0
#     for l in lis:
#         long += 1
#     return long
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     A = [i for i in range(1, 13)]
#     cnt = 0
#     for i in range(1 << len(A)):
#         sub = []
#         for j in range(len(A)):
#             if i & 1 << j:
#                 sub.append(A[j])
#         if len_val(sub) == N and sum_val(sub) == K:
#             cnt += 1
#     print('#{} {}'.format(tc, cnt))

# [S/W 문제해결 기본] 2일차 - Ladder1
# for tc in range(1, 11):
#     int(input())
#     arr = []
#     for _ in range(100):
#         arr.append(list(input().split()))
#     for a in arr[99]:
#         if a == '2':
#             two = arr[99].index(a)
#     dr = [-1, 0, 0]
#     dc = [0, -1, 1]
#     r = 99
#     c = two
#     while r > 0:
#         r = r + dr[0]
#         c = c + dc[0]
#
#         if 0 <= c-1 <100 and arr[r][c-1] == '1':
#             while arr[r][c-1] == '1':
#                 r = r + dr[1]
#                 c = c + dc[1]
#                 if arr[r-1][c] == '1':
#                     break
#
#         elif 0 <= c+1 <100 and arr[r][c+1] == '1':
#             while arr[r][c+1] == '1':
#                 r = r + dr[2]
#                 c = c + dc[2]
#                 if arr[r-1][c] == '1':
#                     break
#     print(f'#{tc} {c}')

# 파리 퇴치
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = []
#     for _ in range(N):
#         arr.append(list(map(int, input().split())))
#         result = []
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             total = 0
#             max_val = 0
#             for l in range(i, i+M):
#                 total += sum(arr[l][j:j+M])
#             if max_val < total:
#                 max_val = total
#             result.append(max_val)
#
#     ans = result[0]
#     for r in result:
#         if r > ans:
#             ans = r
#
#     print(f'#{tc} {ans}')

# 어디에 단어가 들어갈 수 있을까
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = []
#     cnt = 0
#     for _ in range(N):
#         arr.append(list(input().split()))
#
#     for i in range(N):
#         long = 0
#         long2 = 0
#         for j in range(N):
#             if arr[i][j] == '1' and j != N-1:
#                 long += 1
#             elif arr[i][j] == '1' and j == N-1:
#                 long += 1
#                 if long == K:
#                     cnt += 1
#             elif arr[i][j] == '0':
#                 if long == K:
#                     cnt += 1
#                 long = 0
#
#             if arr[j][i] == '1' and i != N-1:
#                 long2 += 1
#             elif arr[j][i] == '1' and i == N-1:
#                 long2 += 1
#                 if long2 == K:
#                     cnt += 1
#             elif arr[j][i] == '0':
#                 if long2 == K:
#                     cnt += 1
#                 long2 = 0
#
#     print(f'#{tc} {cnt}')