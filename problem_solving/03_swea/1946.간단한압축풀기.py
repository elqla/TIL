t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 문서와 숫자쌍의 개수
    print(f'#{tc}')

    lst = []
    for _ in range(n):
        char, str_k = input().split()
        k = int(str_k)
        lst.extend([char*k])
    str = ''.join(lst) #AAAAAAAAAABBBBBBBCCCCC

    for i in range(0, len(str), 10):
        print(str[i:i+10])

'''
1
3
A 10
B 7
C 5  
'''