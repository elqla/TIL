#find
#단어 등장위치 리스트로 반환
#else: -1
def my_find(text, alphabet):
    result = []
    for idx, char in enumerate(text, 1):
        if alphabet in char:
            result.append(idx)
    return result if result else -1
print(my_find('apple', 'p'))
print(my_find('a', 'p'))




#n명의 학생 중 students는 출석한 학생(max=n)이다.
#결석한 학생을 구하라.
def check(n, students):
    students = list(map(int, students.split()))
    result = []
    for i in range(1, n+1):
        if i not in students:
            result.append(str(i))
    return ' '.join(result)

