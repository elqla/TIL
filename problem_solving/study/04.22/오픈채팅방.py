def solution(record):
    change = {}
    answer = []

    for cord in record:
        cord = cord.split()
        if cord[0] in ['Enter', 'Change']:
            change[cord[1]] = cord[2]

    for cord in record:
        cord = cord.split()
        if cord[0]=='Enter':
            answer.append(change[cord[1]]+'님이 들어왔습니다.')
        elif cord[0]=='Leave':
            answer.append(change[cord[1]]+'님이 나갔습니다.')


    return answer

#
#
# def solution(record):
#     change = {}
#     leave = set()
#
#     answer = []
#     for cord in record:
#         cord = cord.split()
#         if cord[0]=='Enter':
#             change[cord[1]] = cord[2]  # 나갔다 들어와도 바꿔줘야 하니까
#             leave.discard(cord[1])  # remove는 없는걸 지우려면 keyerror가 나서, discard 사용
#             answer.append(cord[1] + "님이 들어왔습니다.")
#         elif cord[0]=='Leave':
#             leave.add(cord[1])
#             answer.append(cord[1] + "님이 나갔습니다.")
#         elif cord[0]=='Change':
#             if cord[1] not in leave:
#                 change[cord[1]] = cord[2]
#
#     result = []
#     key = change.keys()
#     for ans in answer:
#         for k in key:
#             if k in ans:
#                 result.append(ans.replace(k, change[k]))
#                 break
#
#     return result




# Enter 유저아이디 닉네임
# Leave 유저아이디
# Change 유저아이디 닉네임





