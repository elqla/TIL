def b(t, m, p):
    a = list()
    for i in range(t*m):
        b = list(bin(i))[2:]
        a += b

    text = ''
    idx = 0   # 튜브의 위치
    aidx = 0  # 전체 위치
    while t: # 1 1 2 3 4
        if idx+1==p:  # idx+1 == 첫번째
            text += a[aidx]
            t -= 1    # 구해야하는 개수에서 하나 줄여줌
        idx += 1
        aidx += 1
        if idx==m:  # idx가 전체 멤버수와 같아지면, 초기화해줌
            idx = 0
    return text


def o(t, m, p):
    a = list()
    for i in range(t*m):
        b = list(oct(i))[2:]
        a += b
    text = ''
    idx = 0
    aidx = 0
    while t:
        if idx+1==p:
            text += a[aidx]
            t -= 1
        idx += 1
        aidx += 1
        if idx==m:
            idx = 0
    return text


def d(t, m, p):
    a = list()
    for i in range(t*m):
        b = list(str(i))
        a += b
    text = ''
    idx = 0
    aidx = 0
    while t:
        if idx+1==p:
            text += a[aidx]
            t -= 1
        idx += 1
        aidx += 1
        if idx==m:
            idx = 0
    return text


def h(t, m, p):
    a = list()
    for i in range(t*m):
        b = list(hex(i))[2:]
        a += b
    text = ''
    idx = 0
    aidx = 0
    while t:
        if idx+1==p:
            if a[aidx].isdigit():
                text += a[aidx]
            else:
                text += a[aidx].upper()
            t -= 1
        idx += 1
        aidx += 1
        if idx==m:
            idx = 0
    return text

def solution(n, t, m, p):
    answer = ''
    if n==2:
        answer = b(t, m, p)

    elif n==8:
        answer = o(t, m, p)

    elif n==10:
        answer = d(t, m, p)

    elif n==16:
        answer = h(t, m, p)

    return answer
print(solution(10, 1, 11, 2)) #"0111"
# n진법, 구할숫자개수t, 참가인원m, 튜브순서 p


# 16, 16, 2, 1  #"02468ACE11111111"
# 16, 16, 2, 2  #"13579BDF01234567"

# 2, 8, 10, 16
# print(bin(10)) #2
# print(oct(10)) #8
# print(10) # 10
# print(hex(10)) # 16