T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    cnt = 0
    for a in arr:
        if a%2 == 1:
            cnt += a

    print(f'#{tc} {cnt}')