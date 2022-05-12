import re
from collections import deque, defaultdict
def solution(str1, str2):

    list_str_1 = []
    g = []

    dic = defaultdict(int)
    str_1 = list(re.sub('[^a-z, A-Z]', '',str1))
    str_2 = list(re.sub('[^a-z, A-Z]', '',str2))

    l = len(str_1) + len(str_2)

    st1 = deque([str_1[0]])
    for i in range(1, len(str_1)):
        st1.append(str_1[i])
        list_str_1.append(''.join(st1).lower())
        st1.popleft()

    # [i:i+2]

    st2 = deque([str_2[0]])
    for i in range(1, len(str_2)):
        st2.append(str_2[i])
        string2 = ''.join(st2).lower()
        if string2 in list_str_1:
            g.append(string2)
            # st2.popleft()
        st2.popleft()

    answer = 1

    # https: // programmers.co.kr / learn / courses / 30 / lessons / 17677



    print(len(g))
    print(g)
    print(l)
    if g:
        answer = len(g)/ (l-len(g))
            # len(list_str_1)/(l -len(g))
    # 교집합크기/합집합크기
    # 공집합일시, 1
    # 교집합크기/(전체길이-교집합길이)


    return answer





print(solution('FRANCE','french'))
# 16384