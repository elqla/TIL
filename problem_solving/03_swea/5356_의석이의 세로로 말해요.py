for tc in range(1, int(input())+1):

    arr = [list(map(str,input())) for _ in range(5)]


    s = ''
    for i in range(15):
        for j in range(5):
            try:
                if arr[j][i]:
                    s += arr[j][i]
            except:
                pass
    print(f'#{tc} {s}')




'''
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''