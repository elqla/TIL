def solution(dartResult):

    star = [] #스타상
    acha = [] #아차상
    tmp = ''
    none = []
    dart = list(dartResult)

    tmpidx = -1
    flag = 0
    for i in range(0, len(dartResult)):
        if ord(dart[i]) in range(48, 58):
            tmp += dart[i]
        elif dart[i] in ['S', 'D', 'T']:
            if dart[i]=='S':
                tmp = int(tmp)
            elif dart[i]=='D':
                tmp = int(tmp)**2
            elif dart[i]=='T':
                tmp = int(tmp)**3
            tmpidx += 1
            none.append((tmp, tmpidx))
            tmp = ''

        elif dart[i] in ['*', '#']:
            a, ai = none.pop()
            if dart[i]=='*':
                if tmpidx != 0:
                    if none:
                        if none[-1][1]==tmpidx-1:
                            x, xi = none.pop()
                            none.append((x*2, xi))
                    if acha:
                        if acha[-1][1]==tmpidx-1:
                            pass
                    if star:
                        if star[-1][1]==tmpidx-1:
                            x, xi = star.pop()
                            star.append((x*2, xi))
                star.append((a*2, tmpidx))
                if acha:
                    flag = tmpidx


            elif dart[i]=='#':
                acha.append((-a,tmpidx))

    if flag:
        tmpacha = []
        while acha:
            x, xi = acha.pop()
            if xi < flag:
                tmpacha.append((x*2, xi))
            else:
                tmpacha.append((x, xi))
        acha = tmpacha

    ss = 0
    for s, i in star:
        ss += s
    for ac, i in acha:
        ss += ac
    for nn, i in none:
        ss += nn

    return ss


print(solution("1S2D*3T*")) # 72
# https://programmers.co.kr/learn/courses/30/lessons/17682


