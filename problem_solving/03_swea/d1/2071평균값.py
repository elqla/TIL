T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    #0~1000
    #10개의 수
    cnt = 0
    for i in range(10):
        cnt += arr[i]

    result = round(cnt/10)   #반올림 함수: round


    print(f'#{tc} {result}')