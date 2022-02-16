T = int(input())

for tc in range(1, T + 1):
    #2개의 수
    #0~1000

    a, b = map(int, input().split())

    def test(a, b):
        if a < b:
            return '<'
        elif a == b:
            return '='
        else:
            return '>'

    result = test(a, b)
    print(f'#{tc} {result}')
