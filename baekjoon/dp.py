# 9461번 (파도반 수열)
T = int(input())
def dp(N):
    if N == 1 or N == 2 or N == 3:
        return 1
    elif N == 4 or N == 5:
        return 2

    return dp(N-3) + dp(N-2)

for tc in range(T):
    N = int(input())
    print(dp(N))