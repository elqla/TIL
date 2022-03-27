t = int(input())
for tc in range(1, t+1):
    a, b_list = map(list, input().split())

    res = ''
    for b in b_list:
        deci = int(b, 16) # 10진수로 변환
        binary = bin(deci).replace('0b','').rjust(4,'0') #우측정렬된것에 4만큼의 길이에 맞춰 0을 채워줌
        res += binary
    print(f'#{tc} {res}')