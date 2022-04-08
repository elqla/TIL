n = int(input()) # <= 100

switch = list(map(int, input().split())) #스위치
n = len(switch)
switch = [-1] + switch
# idx를 맞춰주려고 하면 여자꺼가 0, 1인 상황에선 바꿔버릴 수 있음



num_student = int(input())
#student = [list(map(int, input().split())) for _ in range(num_student)]
for _ in range(num_student):
    gender, num = map(int, input().split())


    #남자일때는 배수를 누르고
    if gender == 1:
        for i in range(num, n+1):
            if i%num == 0:
                if switch[i] == 0:
                    switch[i] = 1
                elif switch[i] == 1:
                    switch[i] = 0
                #switch[i] = not switch[i]  #0, 1은 F, T라서 파이써닉하게 할수있다...~

    #여자일때는 대칭을 누르고
    #나 몇번이나 반복해야될지 몰라 할때는 그냥 while 쓰기
    elif gender == 2:
        switch[num] = not switch[num] #나는 나랑 대칭이니까 무조건 바꿀거야
        k = 1
        while 1:
            #if num -1 >= 0 and num +1 < n+1:
            if num -k >=1 and num +k <=n:  #1~n까지의 스위치
            #우리가 정크 데이터를 넣어놨기 때문에.. 더 복잡해질수 있음
                if switch[num-k] == switch[num+k]:
                    switch[num - k] = not switch[num-k]
                    switch[num + k] = not switch[num+k]
                else:
                    break   #달라 -1 멈춰
            else:
                break  #스위치를 벗어나면 멈춘다.

            k += 1
            print(switch, num, k, '여자 while 안쪽') #num을 기준으로 몇번째 떨어졌는지 ?
        print(switch, '여자 다음 스위치')


switch = list(map(int,switch))
print(*switch[1:])




