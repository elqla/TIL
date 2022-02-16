T = int(input())

for tc in range(1, T + 1):

    arr = list(map(int, input().split()))
    #0~1000
    mx = arr[0]
    for i in range(10):
        if mx<arr[i]:
            mx = arr[i]



    print(f'#{tc} {mx}')