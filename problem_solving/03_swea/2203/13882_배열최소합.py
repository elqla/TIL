def permute(i, r):
    global mn
    if i==r:
        s = 0
        for k in range(r):
            s += arr[k][bit[k]]
            if s>=mn: #만일 계산도중, 합이 최소값보다 커지면 계산을 멈춤
                return
        if s < mn:
            mn = s
    for n in range(r):
        if n not in bit[0:i]:
            bit[i] = n
            permute(i+1, r)


t = int(input())
for tc in range(1, t+1):
    r = int(input())  # 각 배열의 길이, + 부분집합의 길이를 결정
    arr = [list(map(int, input().split())) for _ in range(r)]

    mn = 10000
    bit = [0] * r
    permute(0, r)


    print(f'#{tc} {mn}')

'''
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8
'''