import re
def solution(info, query):

    l = len(info)
    q = len(query)

    lst = []
    for i in range(l):
        lst.append(info[i].split())


    q_lst = []
    for j in range(q):
        query[j] = re.sub('and|-', '', query[j])
        q_lst.append(query[j].split())

    answer = [0]*q
    # 고정시킬 것 == q_lst
    for qi in range(q):
        for ll in lst:
            if len(q_lst[qi])==1:
                if int(q_lst[qi][0]) <= int(ll[-1]):
                    answer[qi] += 1
            else:
                q_i = 0
                for qq in q_lst[qi][:-1]:
                    if qq in ll:
                        q_i += 1
                    else:
                        continue
                if q_i ==len(q_lst[qi])-1:
                    if int(q_lst[qi][-1]) <= int(ll[-1]):
                        answer[qi] += 1
                else:
                    continue

    return answer

info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

print(solution(info, query))
