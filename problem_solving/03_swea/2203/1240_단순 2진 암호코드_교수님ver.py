patterns = {
    (3,2,1,1) : 0,
    (2,2,2,1) : 1,
    (2,1,2,2) : 2,
    (1,4,1,1) : 3,
    (1,1,3,2) : 4,
    (1,2,3,1) : 5,
    (1,1,1,4) : 6,
    (1,3,1,2) : 7,
    (1,2,1,3) : 8,
    (3,1,1,2) : 9,
    }

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    data = [list(map(int, input())) for _ in range(n)]
    # 패턴 비율로 암호 숫자를 찾기
    # 각 행의 맨 뒤에서부터 1찾기: 1 찾으면 패턴의 시작을 찾은 것!

    is_find = False
    password = []
    for i in range(n):
        idx = m-1
        while idx >=55:
            if data[i][idx] == 1: # 패턴 시작
                is_find = True
                for _ in range(8): #패턴 8개 찾을거임
                    c1 = c2 = c3 = c4 = 0 # 패턴의 각 부분의 길이/width
                    # 1의 개수 세서 c4에 저장
                    while data[i][idx] == 1:
                        c4 += 1
                        idx -=1
                    # 0의 개수 세서 c3에 저장
                    while data[i][idx] == 0:
                        c3 += 1
                        idx -=1
                    # 1의 개수 세서 c2에 저장
                    while data[i][idx] == 1:
                        c2 += 1
                        idx -=1
                    # 0의 개수 세서 c1에 저장
                    c1 = 7-c2-c3-c4
                    idx -= c1
                    # 패턴 구했으니 >> 숫자찾기
                    password.insert(0, patterns[(c1, c2, c3, c4)])
                #print(password)
                # break
            else:
                idx-=1
        if is_find: break
    odd_sum = password[0] + password[2] + password[4] + password[6]
    even_sum = password[1] + password[3] + password[5] + password[7]
    result = 0
    if (odd_sum*3 + even_sum)%10 == 0:
        result = odd_sum + even_sum
    print(f'#{tc} {result}')



