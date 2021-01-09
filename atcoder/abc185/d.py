import math

if __name__ == '__main__':
    N, M = map(int, input().split())
    if M == 0:
        print(1)
    elif N == M:
        print(0)
    else:
        A = list(map(int, input().split()))
        A = list(map(lambda x: x - 1, A))
        A.sort()
        white_count = []
        if A[0] != 0:
            white_count.append(A[0])
        if N - A[M-1] - 1 != 0:
            white_count.append(N - A[M-1] - 1)
        for i in range(M-1):
            if A[i + 1] - A[i] != 1:
                white_count.append(A[i + 1] - A[i] - 1)
        white_count.sort()
        min_white_count = white_count[0]
        ans = 0
        for i, _ in enumerate(white_count):
            ans += math.ceil(white_count[i] / min_white_count)
        print(ans)




