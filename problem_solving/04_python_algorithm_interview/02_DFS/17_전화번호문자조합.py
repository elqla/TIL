def dfs(index, path):
    if len(digits)==len(path):
        result.append(path)
        print(path)
    # 입력된 자릿수 단위 반복
    for i in range(index, len(digits)):
        #숫자에 해당하는 모든 문자열 반복
        for j in dic[digits[i]]:
            dfs(i+1, path+j)



dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
       '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

result = []
digits = '23'
dfs(0, '')
print(result)