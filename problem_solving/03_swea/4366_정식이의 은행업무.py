def solve(lst3):
    for i in range(len(lst2)):
        lst2[i] = (lst2[i]+1)%2  # 1비트 값만 바꿔서 10진수 값으로 변환

        deci = 0 # 10진수로 변환
        for idx in range(len(lst2)):
            deci = deci*2 + lst2[idx]

        s = [] # 3진수로 변환
        ret = deci
        while deci>0:
            s.append(deci%3)
            deci //= 3  # 낮은 자리부터 비교하려고 뒤집지 않음
        lst3 = lst3[::-1]

        cnt = 0
        for idx in range(min(len(s), len(lst3))):
            if s[idx]!=lst3[idx]:
                cnt += 1 # 다르다면 cnt 증가
        cnt += abs(len(s) - len(lst3))  # 길이가 다르다면, 다른 값임 !

        if cnt == 1: # 3진수로 바꿨더니 하나만 다르다면
            return ret


        lst2[i] = (lst2[i]+1)%2 # 원상복귀




t = int(input())
for tc in range(1, t+1):
    lst2 = list(map(int, input()))
    lst3 = list(map(int, input()))

    ans = solve(lst3)

    print(f'#{tc} {ans}')

'''
1
1010
212
'''