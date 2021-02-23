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

# min max
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     max_val = numbers[0]
#     min_val = numbers[0]
#
#     for n in numbers:
#         if n > max_val:
#             max_val = n
#         if n < min_val:
#             min_val = n
#
#     print('#{} {}'.format(tc, max_val-min_val))

# 숫자 카드
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cards = input()
#     counting = [0] * 10
#
#     for card in cards:
#         counting[int(card)] += 1
#
#     max_num = 0
#     max_cnt = 0
#     for i in range(10):
#         if counting[i] >= max_cnt:
#             max_cnt = counting[i]
#             max_num = i
#
#     print('#{} {} {}'.format(tc, max_num, max_cnt))

# 전기버스
# T = int(input())
# for tc in range(1, T+1):
#     K, N, M = map(int, input().split())
#     stop = list(map(int, input().split())) # 충전소의 위치
#     bus = 0 # 버스의 위치
#     cnt = 0 # 충전 횟수
#     while bus < N:
#         bus += K
#         if bus >= N:
#             break
#         if bus in stop:
#             cnt += 1
#         else:
#             same = list(set(range(bus - (K-1), bus)) & set(stop))
#             if len(same) == 0:
#                 cnt = 0
#                 break
#             else:
#                 bus = same[len(same)-1]
#                 cnt += 1
#
#     print(cnt)

# 구간합
# def sum_v(lis):
#     total = 0
#     for l in lis:
#         total += l
#     return total
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     nums = list(map(int, input().split()))
#     max_total = float('-inf')
#     min_total = float('inf')
#     for i in range(N-M+1):
#         if sum_v(nums[i:i+M]) > max_total:
#             max_total = sum_v(nums[i:i+M])
#         if sum_v(nums[i:i+M]) < min_total:
#             min_total = sum_v(nums[i:i+M])
#
#
#     print('#{} {}'.format(tc, max_total - min_total))

# 현주의 상자 바꾸기
# T = int(input())
# for tc in range(1, T+1):
#     N, Q = map(int, input().split())
#     result = [0] * N
#     arr = []
#     for _ in range(Q):
#         arr.append(list(map(int, input().split())))
#     for i in range(len(arr)):
#         for j in range(arr[i][0]-1,arr[i][1]):
#             result[j] = i+1
#     result= list(map(str, result))
#     result = ' '.join(result)
#     print('#{} {}'.format(tc, result))

# 현주의 상자 바꾸기2
# T = int(input())
# for tc in range(1, T+1):
#     N, Q = map(int, input().split())
#     result = [0] * N
#     for i in range(1, Q+1):
#         L, R = map(int, input().split())
#         for j in range(L-1, R):
#             result[j] = i
#     result = list(map(str, result))
#     result= ' '.join(result)
#     print('#{} {}'.format(tc, result))

# 간단한 소인수분해
# T = int(input())
# for tc in range(1, T+1):
#     num = int(input())
#     numbers = [2, 3, 5, 7, 11]
#     cnt = [0] * 5
#
#     for i in range(5):
#         while num % numbers[i] == 0:
#             cnt[i] += 1
#             num = num // numbers[i]
#     cnt = list(map(str, cnt))
#     cnt = ' '.join(cnt)
#     print('#{} {}'.format(tc, cnt))

# Flatten
# def max_v(lis):
#     max_val = 1
#     for l in lis:
#         if l > max_val:
#             max_val = l
#     return max_val
#
# def min_v(lis):
#     min_val = 100
#     for l in lis:
#         if l < min_val:
#             min_val = l
#     return min_val
#
# for tc in range(1, 11):
#     dump = int(input())
#     nums = list(map(int, input().split()))
#     for _ in range(dump):
#         nums[nums.index(max_v(nums))] -= 1
#         nums[nums.index(min_v(nums))] += 1
#         if max_v(nums) - min_v(nums) == 1:
#             break
#
#     print('#{} {}'.format(tc, max_v(nums) - min_v(nums)))

# 삼성시의 버스노선
# T= int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cnt = [0] * (5001)
#     for _ in range(N):
#         start, end = map(int, input().split())
#         for i in range(start, end+1):
#             cnt[i] += 1
#     result = []
#     stop = int(input())
#     for _ in range(stop):
#         j = int(input())
#         result.append(cnt[j])
#
#     result = map(str, result)
#     result = ' '.join(result)
#
#     print('#{} {}'.format(tc, result))

# 숫자를 정렬하자
# T = int(input())
# for tc in range(1, T+1):
#     cnt = int(input())
#     nums = list(map(int, input().split()))
#     for i in range(cnt-1, -1, -1):
#         for j in range(i):
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     nums = map(str, nums)
#     nums = ' '.join(nums)
#
#     print('#{} {}'.format(tc, nums))

# 두 개의 숫자열
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#
#     if N > M:
#         N, M = M, N
#         A, B = B, A
#
#     max_v = 0
#     for i in range(M-N+1):
#         move = B[i:i+M]
#         total = 0
#         for j in range(N):
#             total += move[j] * A[j]
#         if total > max_v:
#             max_v = total
#
#     print('#{} {}'.format(tc, max_v))

# 연속한 1의 개수
# T = int(input())
# for tc in range(1, T+1):
#     long = int(input())
#     nums = input()
#     cnt = 0
#     max_v = 0
#     for n in nums:
#         if n == "1":
#             cnt += 1
#         else:
#             cnt = 0
#         if cnt > max_v:
#             max_v = cnt
#     print('#{} {}'.format(tc, max_v))

# 점점 커지는 당근의 개수
# T = int(input())
# for tc in range(1, T+1):
#     long = int(input())
#     carrots = list(map(int, input().split())) + [-1]
#     cnt = 1
#     max_v = 1
#     for i in range(len(carrots)-1):
#         if carrots[i] < carrots[i+1]:
#             cnt += 1
#         else:
#             if cnt >max_v:
#                 max_v=cnt
#             cnt=1
#     print('#{} {}'.format(tc, max_v))

# 당근의 개수
# T = int(input())
# for tc in range(1, T+1):
#     long = int(input())
#     carrots = list(map(int, input().split()))
#
#     max_idx = 0
#     max_v = 0
#     for i in range(long):
#         if carrots[i] > max_v:
#             max_v = carrots[i]
#             max_idx = i+1
#     print('#{} {} {}'.format(tc, max_idx, max_v))

# 당근 수확
# def sum_v(lis):
#     total = 0
#     for l in lis:
#         total += l
#     return total
#
# T= int(input())
# for tc in range(1, T+1):
#     long = int(input())
#     carrots = list(map(int, input().split()))
#
#     min_v = float('inf')
#     part = 0
#     for mid in range(1, long-1):
#         diff = abs(sum_v(carrots[:mid])-sum_v(carrots[mid:]))
#         if diff < min_v:
#             min_v = diff
#             part = mid
#
#     print('#{} {} {}'.format(tc, part, min_v))

# 당근밭 옆 고구마밭
# T = int(input())
# for tc in range(1, T+1):
#     long = int(input())
#     potato = list(map(int,input().split())) + [-1]
#     root = 0
#     total = 0
#     max_total = 0
#     length = 0
#     max_lenght = 0
#     for i in range(long):
#         if potato[i] < potato[i+1]:
#             total += potato[i]
#             length += 1
#         else:
#             if total != 0:
#                 total += potato[i]
#                 root += 1
#                 length += 1
#                 if length > max_lenght:
#                     max_lenght = length
#                     max_total = total
#                 elif length == max_lenght:
#                     if total > max_total:
#                         max_total = total
#                 total = 0
#                 length = 0
#             else:
#                 continue
#     print('#{} {} {}'.format(tc, root, max_total))

# list2_연습1
# T = int(input())
# for tc in range(1, T+1):
#     size = int(input())
#     arr = []
#     for i in range(size):
#         row = list(map(int, input().split()))
#         arr.append([row[0]] + row + [row[len(row)-1]])
#     arr = [arr[0]] + arr + [arr[len(arr)-1]]
#     ans = 0
#     for i in range(1, size+1):
#         for j in range(1, size+1):
#             up = abs(arr[i][j] - arr[i-1][j])
#             down = abs(arr[i][j] - arr[i+1][j])
#             left = abs(arr[i][j] - arr[i][j-1])
#             right = abs(arr[i][j] - arr[i][j+1])
#             total = up + down + left + right
#             ans += total
#     print('#{} {}'.format(tc, ans))

# list2_연습2 (부분집합의 합이 0이 되는 문제. 비트연산자 모르겠음..)


# 달팽이 숫자
# T = int(input())
# for tc in range(1, T+1):
#     size = int(input())
#     arr = []
#     num = list(range(size*size+1))
#     idx = 1
#     i = 0
#     j = -1
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     k = 0
#     for _ in range(size):
#         arr.append([0] * size)
#     while idx <= size**2:
#         next_i = i + dr[k%4]
#         next_j = j + dc[k%4]
#         if 0 <= next_i < size and 0 <= next_j < size and arr[next_i][next_j] == 0:
#             arr[next_i][next_j] = num[idx]
#             idx += 1
#             i = next_i
#             j = next_j
#
#         else:
#             k += 1
#
#     print('#{}'.format(tc))
#     for i in arr:
#         i = list(map(str, i))
#         i = ' '.join(i)
#         print(i)

# sum
# for tc in range(1, 11):
#     int(input())
#     arr = []
#     for _ in range(100):
#         arr.append(list(map(int, input().split())))
#     total = 0
#     total2 = 0
#     total3 = 0
#     total4 = 0
#     max_total = 0
#     max_total2 = 0
#     for i in range(100):
#         for j in range(100):
#             total += arr[i][j]
#             total2 += arr[j][i]
#             if i == j:
#                 total3 += arr[i][j]
#             if i == 99-j:
#                 total4 += arr[i][j]
#         if total > max_total:
#             max_total = total
#         if total2 > max_total2:
#             max_total2 = total2
#         total = 0
#         total2 = 0
#     ans = 0
#     for i in [max_total, max_total2, total3, total4]:
#         if i > ans:
#             ans = i
#     print('#{} {}'.format(tc, ans))

# 색칠하기
# T= int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [[0]*10 for _ in range(10)]
#     quest = []
#     cnt = 0
#     for _ in range(N):
#         quest.append(list(map(int, input().split())))
#     for lis in quest:
#         for i in range(lis[0], lis[2]+1):
#             for j in range(lis[1], lis[3]+1):
#                 arr[i][j] += lis[4]
#     for i in range(10):
#         for j in range(10):
#             if arr[i][j] == 3:
#                 cnt += 1
#     print('#{} {}'.format(tc, cnt))

# 이진 탐색
# def find(P, find):
#     start = 1
#     end = P
#     cnt = 0
#     while start != end:
#         mid = (start+end)//2
#         if find > mid:
#             cnt += 1
#             start = mid
#         elif find < mid:
#             cnt += 1
#             end = mid
#         else:
#             cnt += 1
#             return cnt
#
# T = int(input())
# for tc in range(1, T+1):
#     P, A, B = map(int, input().split())
#     if find(P, A) < find(P, B):
#         ans = 'A'
#     elif find(P, A) > find(P, B):
#         ans = 'B'
#     else:
#         ans = 0
#     print('#{} {}'.format(tc, ans))

# 당근 수확4
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = []
#     total1 = 0
#     total2 = 0
#     total3 = 0
#     total4 = 0
#     for _ in range(N):
#         arr.append(list(map(int, input().split())))
#     center = len(arr)//2
#     for i in range(center):
#         for j in range(1+i, N-(1+i)):
#             total1 += arr[i][j]
#             total2 += arr[j][i]
#     for i in range(center+1, N):
#         for j in range(N-i ,i):
#             total3 += arr[i][j]
#             total4 += arr[j][i]
#
#     max_v = total1
#     min_v = total1
#     for i in [total1, total2, total3, total4]:
#         if i > max_v:
#             max_v = i
#         if i < min_v:
#             min_v = i
#     print('#{} {}'.format(tc, max_v - min_v))

# 고대 유적
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = []
#     for _ in range(N):
#         arr.append(list(map(int, input().split())))
#     max_long = 0
#     for i in range(N):
#         long = 0
#         for j in range(M):
#             if arr[i][j] == 1:
#                 long += 1
#             else:
#                 long = 0
#             if long > max_long:
#                 max_long = long
#
#     T_arr = list(zip(*arr))
#
#     for i in range(M):
#         long2 = 0
#         for j in range(N):
#             if T_arr[i][j] == 1:
#                 long2 += 1
#             else:
#                 long2 = 0
#             if long2 > max_long:
#                 max_long = long2
#
#     print('#{} {}'.format(tc, max_long))

# 우주선 착륙
# def max_v(lis):
#     max_val = float('-inf')
#     for l in lis:
#         if l > max_val:
#             max_val = l
#     return max_val
#
# def min_v(lis):
#     min_val = float('inf')
#     for l in lis:
#         if l < min_val:
#             min_val = l
#     return min_val
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M, K, H = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 0
#     for i in range(1, N-1):
#         for j in range(1, M-1):
#             center = arr[i][j]
#             around = arr[i-1][j-1:j+2] + [arr[i][j-1]]+ [arr[i][j+1]] + arr[i+1][j-1:j+2]
#             if max_v(around) - min_v(around) <= K and center >= min_v(around) and center - min_v(around) <= H:
#                 cnt += 1
#     print('#{} {}'.format(tc, cnt))

# 파리 퇴치
# def sum_v(lis):
#     total = 0
#     for l in lis:
#         total += l
#     return total
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = []
#     for _ in range(N):
#         arr.append(list(map(int, input().split())))
#     max_sum = 0
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             sub_sum = sum_v(map(lambda x:sum_v(x[j:j+M]), arr[i:i+M]))
#             if sub_sum > max_sum:
#                 max_sum = sub_sum
#     print('#{} {}'.format(tc, max_sum))

# 영준이의 카드 카운팅
# def sum_v(lis):
#     total = 0
#     for l in lis:
#         total += l
#     return total
#
# T = int(input())
# for tc in range(1, T+1):
#     cards = input()
#     card = []
#     # 각 카드가 13개씩 있어야 한다.
#     match = {'S': [0]*13, 'D':[0]*13, 'H': [0]*13, 'C':[0]*13}
#     # input을 입력받으면 3자리씩 잘라서 card 라는 리스트에 넣는다.
#     for i in range(len(cards)//3):
#         card.append(cards[i*3:(i+1)*3])
#     # card 리스트의 원소의 0 인덱스는 카드의 모양, 뒤 두자리는 카드의 번호이기 때문에 딕셔너리에서 해당 카드 번호에 1을 더해준다.
#     for c in card:
#         match.get(c[0])[int(c[1:3])-1] += 1
#
#     ans = []
#     for v in match.values():
#         flag = False
#         # match 딕셔너리의 value 값의 원소의 합을 13에서 빼주면 부족한 카드의 갯수를 구할 수 있다.
#         ans.append(13 - sum_v(v))
#         # value 리스트의 원소가 1 보다 크면 ans 에 error 를 저장하고 반복문을 탈출한다.
#         for i in v:
#             if i > 1:
#                 ans = 'ERROR'
#                 flag = True
#             if flag: break
#         if flag:break
#
#     # ans 의 타입이 리스트라는 것은 에러가 아니라는 뜻이므로 문자열로 변환해 출력한다.
#     if type(ans) == list:
#         ans = map(str, ans)
#         ans = ' '.join(ans)
#
#     print('#{} {}'.format(tc, ans))

# 오목 판정
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [input() for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             std = arr[i][j]

# 퍼펙트 셔플
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     half = N // 2
#     cards = list(input().split())
#     ans = []
#     # 홀수일때
#     if N%2:
#         # 먼저 놓는 쪽에 한장 더 많게 분배
#         up = cards[:half+1]
#         down = cards[half+1:]
#         # up 과 down 에서 앞에서부터 하나씩 ans에 더한다.
#         for i in range(half+1):
#             ans.append(up[i])
#             # 인덱스 에러 방지하기 위해 i 가 down 인덱스를 초과하면 pass 하도록 조건문
#             if i < len(down):
#                 ans.append(down[i])
#
#     # 짝수일때
#     else:
#         up = cards[:half]
#         down = cards[half:]
#         for i in range(half):
#             ans.append(up[i])
#             ans.append(down[i])
#
#     ans = ' '.join(ans)
#     print('#{} {}'.format(tc, ans))

# 원재의 메모리 복구하기
# T = int(input())
# for tc in range(1, T+1):
#     bit = input()
#     cnt = 0 # 수정 횟수
#     std = '0' # 비교할 문자
#     for i in range(len(bit)):
#         # 기준 문자와 다르면 수정이 일어났다는 의미이므로 cnt +1
#         if bit[i] != std:
#             cnt += 1
#             std = bit[i] # 해당 문자로 기준 문자를 변경한다.
#     print('#{} {}'.format(tc,cnt))