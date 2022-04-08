def solution(new_id):
    answer = ''
    # 1단계 소문자로 변환
    new_id = new_id.lower()


    # 2단계 소문자, 숫자, 빼기, 밑줄, 마침표 제거
    for c in new_id:
        if c.isalnum() or c in '-_.':
            answer += c
    # 3단계
    while '..' in answer:
        answer = answer.replace('..','.')

    # 4단계
    if answer[0:1]=='.':  # 슬라이싱을 쓰면, 빈 문자열이여도, 에러를 반환하지 않음/ 그냥 빈 문자열 그대로 반환
        answer = answer[1:]
    if answer and answer[-1] == '.':  # 이렇게 안쓰고 위처럼 써도됨
        answer = answer[:-1]

    # 5단계
    if not answer:  # ==''
        answer = 'a'

    # 6단계
    answer = answer[:15]
    if answer[-1]=='.':
        answer = answer[:-1]

    # 7단계
    while len(answer)<3:
        answer = answer.ljust(3, answer[-1])


    return answer
print(solution("z-+.^."))









