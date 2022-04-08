from collections import defaultdict

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
def solution(id_list, report, k):
    answer = []
    # 신고한 아이디: [[신고된 아이디], 신고된 횟수]
    id_dic = {id:set() for id in id_list}  #신고한아이디: 신고된아이디
    cnt_dic = defaultdict(int)
    for r in report:
        id, id_r = r.split()
        id_dic[id] += id_r
        # id: 신고된 아이디

        cnt_dic[id_r] += 1
        # 신고된 아이디가 나올때마다 1추가
    res = defaultdict(int)
    for id in id_dic: # 순서대로 해주기 위함.
        for id_r in cnt_dic: # 신고된 아이디들을 하나씩 뽑아서
            if cnt_dic[id_r] >= k:  # 신고된 아이디가 k개 이상이면서
                if id_r in id_dic[id]:  # 신고한아이디: 신고된아이디<-에 있으면
                    res[id] += 1
                else:
                    break
            else:
                break
    return answer
res = solution(id_list, report, k)
print(res)
# for r in report:
#     id, id_r = r.split()
#     if id_r nor in id_dic[id]:
#         id_dic[id][0] += [id_r]
#         id_dic[id][1] += 1

def solution(id_list, report, k):
    answer = []
    id_dic = dic()
    for id in id_list:
        id_dic[id] = [set(), 0]  # 신고한 아이디:[[신고된아이디], 신고된 횟수]
    for r in report:
        id, id_r = r.split()
        id_dic[id][0] += id_r
    for id in id_list:
        if id_dic[id][]

    return answer