from collections import defaultdict
def solution(N, stages):
    answer=[]
    len_stages = len(stages)
    dic = defaultdict(set)  #  실패율: stage번호    # 스테이지 실패율을 키 값으로

    fail_zero = []
    for stage in range(1, N+1):
        cnt = 0
        for c in range(len(stages)):
            if stage == stages[c]:
                cnt += 1
        if cnt==0:
            fail_zero.append(stage)
        elif cnt==len_stages:
            fail = 1
            dic[fail].add(stage)
        else:
            fail = cnt/(len_stages-cnt)
            dic[fail].add(stage)
            len_stages -= cnt  # 현재 스테이지에 있는 사용자를 빼줌

    keylist = list(dic.keys())
    keylist.sort(reverse=True)
    for key in keylist:
        answer.extend(dic[key])

    answer.extend(fail_zero)
    return answer



# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 4
stages = [4, 4, 4, 4, 4]
print(solution(N, stages))