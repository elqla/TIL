t = int(input())
for tc in range(1, t+1):
    n = int(input())

    i = 1
    while 1:
        x = i**3
        if x == n:
            print(f'#{tc} {i}')
            break
        if x>n:
            print(f'#{tc} {-1}')
            break
        i += 1  # 세제곱근 자체를 하나씩 증가시켜서, x == n

# 3
# 27
# 7777
# 64