# 하나라도 벽이면 벽
# 둘다 공백이면 공백
def solution(n, arr1, arr2):
    answer = [[] for _ in range(n)]

    map_1 = []
    map_2 = []

    for a in arr1:
        map_1.append(list(bin(a).replace('0b','').rjust(n, '0')))

    for a2 in arr2:
        map_2.append(list(bin(a2).replace('0b','').rjust(n, '0')))

    for i in range(n):
        for j in range(n):
            if map_1[i][j]==map_2[i][j] and map_1[i][j]=='0': # 둘다 공백
                answer[i].append(' ')
            else:  # 하나라도 벽이거나 둘다 벽일때
                answer[i].append('#')
    result = []
    for a in answer:
        result.append(''.join(a))
    return result


print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
# # ["#####", "# # #", "### #", "#  ##", "#####"]
# (6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
# # ["######", "###  #", "##  ##", " #### ", " #####", "### # "]
