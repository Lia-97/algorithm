# 부품 찾기
def binary_search(node):
    ans = 'no'
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end) // 2
        if node == stocks[mid]:
            ans = 'yes'
            return ans

        if node < stocks[mid]:
            end = mid-1
        elif node > stocks[mid]:
            start = mid+1

    return ans

import sys
N = int(sys.stdin.readline()) # 가게에 있는 부품 개수
stocks = list(map(int, sys.stdin.readline().split())) # 가게에 있는 부품 리스트
stocks.sort() # 이진탐색을 위해 정렬
M = int(sys.stdin.readline()) # 손님이 주문하는 부품 개수
orders = list(map(int, sys.stdin.readline().split())) # 손님이 주문하는 부품 리스트
for order in orders:
    print(binary_search(order), end=' ')