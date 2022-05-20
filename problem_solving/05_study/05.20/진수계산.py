from collections import deque
def els(n, t, m, p):
    a = list()
    jinsu = n
    target_list = deque([i for i in range(t*m)])
    while target_list:
        target = target_list.popleft()
        b = []
        while jinsu<=target:
            b.append(str(target%jinsu))
            target = target//jinsu
        b.append(str(target))
        b = b[::-1]
        a += b

        if len(a)>=t*m:
            break
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
    if n==16:
        answer = h(t, m, p)
    else:
        answer = els(n, t, m, p)

    return answer

print(solution(2, 4, 2, 1)) #"0111"
# n진법, 구할숫자개수t, 참가인원m, 튜브순서 p


# 16, 16, 2, 1  #"02468ACE11111111"
# 16, 16, 2, 2  #"13579BDF01234567"

# 2, 8, 10, 16
# print(bin(10)) #2
# print(oct(10)) #8
# print(10) # 10
# print(hex(10)) # 16