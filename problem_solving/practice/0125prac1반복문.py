#2차원 리스트 반복 및 합반환
#for문
def sum_list(number):
    result = 0
    for num in number:
        for n in num:
            result+=n
    return result

print(sum_list([[1, 4], [10, 5], [20, 30]]))

#index
def sum_list_index(number):
    result = 0
    for i in range(len(number)):
        for j in range(len(number[i])):
            result+=number[i][j]
    return result
print(sum_list_index([[1, 4], [10, 5], [20, 30]]))


#while
def sum_list_while(number):
    i = 0
    result = 0
    while i <len(number):
        j =0
        while j <len(number[i]):
            result +=number[i][j]
            j+=1
        i+=1
    return result
print(sum_list_while([[1, 4], [10, 5], [20, 30]]))




#2차원 배열
#각 리스트별 합 구하기
#for
students = [ [100, 80, 100], [90, 90, 60], [80, 80, 80]]
#for s in students:
#    print(sum(s))
for ss in students:
    result = 0
    for s in ss:
        result+=s
    print(result)

#index
students = [ [100, 80, 100], [90, 90, 60], [80, 80, 80]]
for i in range(len(students)):
    result = 0
    for j in range(len(students[i])):
        result +=students[i][j]
    print(result)





#각 리스트의 자리별 합 구하기
students = [ [100, 80, 100], [90, 90, 60], [80, 80, 80]]
for i in range(len(students)):
    result = 0
    for j in range(len(students[i])):
        result += students[j][i]
    print(result)





































